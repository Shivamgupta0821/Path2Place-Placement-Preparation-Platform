# import re
# import sys
# from io import StringIO
# from typing import List, Dict, Any, Optional
# import traceback

# class MockCodeExecutor:
#     """Mock code execution service that simulates Judge0 behavior"""
    
#     def __init__(self):
#         self.language = "python"
    
#     def validate_syntax(self, code: str) -> tuple[bool, Optional[str]]:
#         """Check if Python code has valid syntax"""
#         try:
#             compile(code, '<string>', 'exec')
#             return True, None
#         except SyntaxError as e:
#             return False, f"Syntax Error: {str(e)}"
#         except Exception as e:
#             return False, f"Compilation Error: {str(e)}"
    
#     def execute_code(self, code: str, stdin: str = "") -> Dict[str, Any]:
#         """Execute Python code and capture output"""
#         # Check syntax first
#         is_valid, error = self.validate_syntax(code)
#         if not is_valid:
#             return {
#                 "success": False,
#                 "status": "Compilation Error",
#                 "stderr": error,
#                 "stdout": "",
#                 "execution_time": 0.0
#             }
        
#         # Execute code
#         old_stdout = sys.stdout
#         old_stdin = sys.stdin
#         sys.stdout = StringIO()
#         sys.stdin = StringIO(stdin)
        
#         try:
#             # Create a restricted execution environment
#             exec_globals = {
#                 '__builtins__': __builtins__,
#                 'print': print,
#                 'input': input,
#                 'range': range,
#                 'len': len,
#                 'str': str,
#                 'int': int,
#                 'float': float,
#                 'list': list,
#                 'dict': dict,
#                 'set': set,
#                 'tuple': tuple,
#             }
            
#             exec(code, exec_globals)
#             stdout = sys.stdout.getvalue()
            
#             return {
#                 "success": True,
#                 "status": "Accepted",
#                 "stdout": stdout,
#                 "stderr": "",
#                 "execution_time": 0.05  # Mock execution time
#             }
#         except Exception as e:
#             error_msg = traceback.format_exc()
#             return {
#                 "success": False,
#                 "status": "Runtime Error",
#                 "stdout": sys.stdout.getvalue(),
#                 "stderr": error_msg,
#                 "execution_time": 0.0
#             }
#         finally:
#             sys.stdout = old_stdout
#             sys.stdin = old_stdin
    
#     def run_test_cases(self, code: str, test_cases: List[Dict[str, Any]]) -> Dict[str, Any]:
#         """Run code against multiple test cases"""
#         results = []
#         passed = 0
#         failed = 0
        
#         for i, test_case in enumerate(test_cases):
#             test_input = test_case.get("input", "")
#             expected_output = test_case.get("expected_output", "").strip()
            
#             result = self.execute_code(code, test_input)
#             actual_output = result.get("stdout", "").strip()
            
#             test_passed = actual_output == expected_output and result["success"]
            
#             if test_passed:
#                 passed += 1
#             else:
#                 failed += 1
            
#             results.append({
#                 "test_number": i + 1,
#                 "input": test_input,
#                 "expected_output": expected_output,
#                 "actual_output": actual_output,
#                 "passed": test_passed,
#                 "status": result["status"],
#                 "stderr": result.get("stderr", ""),
#                 "execution_time": result.get("execution_time", 0.0)
#             })
        
#         return {
#             "success": passed > 0,
#             "passed": passed,
#             "failed": failed,
#             "total": len(test_cases),
#             "test_details": results,
#             "overall_status": "Accepted" if failed == 0 else "Wrong Answer"
#         }

# code_executor = MockCodeExecutor()


import subprocess
import tempfile
import os
import sys
from typing import Dict, Any, List


LANGUAGE_CONFIG = {
    "python": {
        "extension": ".py",
        "run_cmd": [sys.executable],   # uses the same venv python
    },
    "javascript": {
        "extension": ".js",
        "run_cmd": ["node"],
    },
    # Add more languages here as needed
}


class CodeExecutor:
    """Execute user-submitted code against test cases and return pass/fail results"""

    def __init__(self, timeout: int = 5):
        self.timeout = timeout  # seconds per test case

    def run_tests(
        self,
        code: str,
        test_cases: List[Dict[str, Any]],
        language: str = "python"
    ) -> Dict[str, Any]:
        """
        Run code against all test cases.

        Args:
            code:        The user's source code as a string.
            test_cases:  List of {"input": str, "expected_output": str} dicts.
            language:    "python" or "javascript" (must match LANGUAGE_CONFIG).

        Returns:
            {
                "passed": int,
                "total": int,
                "all_passed": bool,
                "results": [ {"input": ..., "expected": ..., "got": ..., "passed": bool}, ... ]
            }
        """
        language = language.lower()
        config = LANGUAGE_CONFIG.get(language)
        if not config:
            return self._error_result(f"Unsupported language: {language}", test_cases)

        results = []
        passed = 0

        for tc in test_cases:
            raw_input = str(tc.get("input", ""))
            expected = str(tc.get("expected_output", "")).strip()

            # Skip test case if expected output is missing/empty
            if not expected:
                continue

            got, error = self._execute(code, raw_input, config)

            if error:
                results.append({
                    "input": raw_input,
                    "expected": expected,
                    "got": error,
                    "passed": False
                })
                continue

            # Normalize output for comparison (strip whitespace, lowercase booleans)
            got_normalized = self._normalize(got)
            expected_normalized = self._normalize(expected)

            test_passed = got_normalized == expected_normalized
            if test_passed:
                passed += 1

            results.append({
                "input": raw_input,
                "expected": expected,
                "got": got,
                "passed": test_passed
            })

        total = len(results)
        return {
            "passed": passed,
            "total": total,
            "all_passed": passed == total and total > 0,
            "results": results
        }

    def _execute(self, code: str, stdin_input: str, config: Dict) -> tuple:
        """
        Write code to a temp file and run it with the given stdin.
        Returns (stdout_output, error_string_or_None).
        """
        try:
            with tempfile.NamedTemporaryFile(
                mode="w",
                suffix=config["extension"],
                delete=False,
                encoding="utf-8"
            ) as f:
                f.write(code)
                tmp_path = f.name

            result = subprocess.run(
                config["run_cmd"] + [tmp_path],
                input=stdin_input,
                capture_output=True,
                text=True,
                timeout=self.timeout
            )

            os.unlink(tmp_path)

            if result.returncode != 0:
                return "", f"Runtime Error: {result.stderr.strip()}"

            return result.stdout.strip(), None

        except subprocess.TimeoutExpired:
            return "", "Time Limit Exceeded"
        except FileNotFoundError as e:
            return "", f"Executor not found: {e}"
        except Exception as e:
            return "", f"Execution Error: {str(e)}"
        finally:
            # Clean up temp file if it still exists
            try:
                if 'tmp_path' in locals() and os.path.exists(tmp_path):
                    os.unlink(tmp_path)
            except Exception:
                pass

    @staticmethod
    def _normalize(value: str) -> str:
        """
        Normalize output for comparison:
        - Strip surrounding whitespace
        - Lowercase Python/JS boolean strings (True->true, False->false)
        """
        v = value.strip().lower()
        # Map Python booleans to a common form
        if v == "true":
            return "true"
        if v == "false":
            return "false"
        return v

    @staticmethod
    def _error_result(message: str, test_cases: List[Dict]) -> Dict[str, Any]:
        return {
            "passed": 0,
            "total": len(test_cases),
            "all_passed": False,
            "results": [{"error": message}]
        }