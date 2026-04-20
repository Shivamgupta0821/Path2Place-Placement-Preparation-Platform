from motor.motor_asyncio import AsyncIOMotorClient
import os
import asyncio
from dotenv import load_dotenv
from pathlib import Path

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

# Sample DSA Questions
dsa_questions = [
    {
        "title": "Two Sum",
        "description": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.\n\nYou may assume that each input would have exactly one solution, and you may not use the same element twice.",
        "difficulty": "easy",
        "type": "dsa",
        "role": None,
        "topic": "Arrays",
        "constraints": [
            "2 <= nums.length <= 10^4",
            "-10^9 <= nums[i] <= 10^9",
            "Only one valid answer exists."
        ],
        "examples": [
            {"input": "nums = [2,7,11,15], target = 9", "output": "[0,1]"},
            {"input": "nums = [3,2,4], target = 6", "output": "[1,2]"}
        ],
        "test_cases": [
            {"input": "2\n7\n11\n15\n9", "expected_output": "[0, 1]"},
            {"input": "3\n2\n4\n6", "expected_output": "[1, 2]"}
        ],
        "starter_code": "def two_sum(nums, target):\n    # Write your code here\n    pass\n\n# Read input\nnums = []\nwhile True:\n    try:\n        line = input().strip()\n        nums.append(int(line))\n    except:\n        break\ntarget = nums[-1]\nnums = nums[:-1]\n\nresult = two_sum(nums, target)\nprint(result)"
    },
    {
        "title": "Reverse String",
        "description": "Write a function that reverses a string. The input string is given as an array of characters s.\n\nYou must do this by modifying the input array in-place with O(1) extra memory.",
        "difficulty": "easy",
        "type": "dsa",
        "role": None,
        "topic": "Strings",
        "constraints": [
            "1 <= s.length <= 10^5",
            "s[i] is a printable ascii character."
        ],
        "examples": [
            {"input": "s = ['h','e','l','l','o']", "output": "['o','l','l','e','h']"},
            {"input": "s = ['H','a','n','n','a','h']", "output": "['h','a','n','n','a','H']"}
        ],
        "test_cases": [
            {"input": "hello", "expected_output": "olleh"},
            {"input": "Hannah", "expected_output": "hannaH"}
        ],
        "starter_code": "def reverse_string(s):\n    # Write your code here\n    return s[::-1]\n\n# Read input\ntext = input().strip()\nresult = reverse_string(text)\nprint(result)"
    },
    {
        "title": "Valid Parentheses",
        "description": "Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.\n\nAn input string is valid if:\n1. Open brackets must be closed by the same type of brackets.\n2. Open brackets must be closed in the correct order.",
        "difficulty": "easy",
        "type": "dsa",
        "role": None,
        "topic": "Stack",
        "constraints": [
            "1 <= s.length <= 10^4",
            "s consists of parentheses only '()[]{}'"
        ],
        "examples": [
            {"input": "s = '()'", "output": "True"},
            {"input": "s = '()[]{}'", "output": "True"},
            {"input": "s = '(]'", "output": "False"}
        ],
        "test_cases": [
            {"input": "()", "expected_output": "True"},
            {"input": "()[]{}", "expected_output": "True"},
            {"input": "(]", "expected_output": "False"}
        ],
        "starter_code": "def is_valid(s):\n    # Write your code here\n    stack = []\n    mapping = {')': '(', '}': '{', ']': '['}\n    for char in s:\n        if char in mapping:\n            if not stack or stack[-1] != mapping[char]:\n                return False\n            stack.pop()\n        else:\n            stack.append(char)\n    return len(stack) == 0\n\n# Read input\ntext = input().strip()\nresult = is_valid(text)\nprint(result)"
    },
    {
        "title": "Merge Two Sorted Lists",
        "description": "You are given the heads of two sorted linked lists list1 and list2.\n\nMerge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.\n\nReturn the head of the merged linked list.",
        "difficulty": "easy",
        "type": "dsa",
        "role": None,
        "topic": "Linked Lists",
        "constraints": [
            "The number of nodes in both lists is in the range [0, 50].",
            "-100 <= Node.val <= 100"
        ],
        "examples": [
            {"input": "list1 = [1,2,4], list2 = [1,3,4]", "output": "[1,1,2,3,4,4]"}
        ],
        "test_cases": [
            {"input": "1 2 4\n1 3 4", "expected_output": "[1, 1, 2, 3, 4, 4]"}
        ],
        "starter_code": "def merge_lists(list1, list2):\n    # Write your code here\n    result = []\n    i, j = 0, 0\n    while i < len(list1) and j < len(list2):\n        if list1[i] < list2[j]:\n            result.append(list1[i])\n            i += 1\n        else:\n            result.append(list2[j])\n            j += 1\n    result.extend(list1[i:])\n    result.extend(list2[j:])\n    return result\n\n# Read input\nlist1 = list(map(int, input().split()))\nlist2 = list(map(int, input().split()))\nresult = merge_lists(list1, list2)\nprint(result)"
    },
    {
        "title": "Binary Search",
        "description": "Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.\n\nYou must write an algorithm with O(log n) runtime complexity.",
        "difficulty": "easy",
        "type": "dsa",
        "role": None,
        "topic": "Binary Search",
        "constraints": [
            "1 <= nums.length <= 10^4",
            "-10^4 < nums[i], target < 10^4"
        ],
        "examples": [
            {"input": "nums = [-1,0,3,5,9,12], target = 9", "output": "4"}
        ],
        "test_cases": [
            {"input": "-1 0 3 5 9 12\n9", "expected_output": "4"},
            {"input": "-1 0 3 5 9 12\n2", "expected_output": "-1"}
        ],
        "starter_code": "def binary_search(nums, target):\n    # Write your code here\n    left, right = 0, len(nums) - 1\n    while left <= right:\n        mid = (left + right) // 2\n        if nums[mid] == target:\n            return mid\n        elif nums[mid] < target:\n            left = mid + 1\n        else:\n            right = mid - 1\n    return -1\n\n# Read input\nnums = list(map(int, input().split()))\ntarget = int(input())\nresult = binary_search(nums, target)\nprint(result)"
    },
    {
        "title": "Maximum Subarray",
        "description": "Given an integer array nums, find the subarray with the largest sum, and return its sum.\n\nA subarray is a contiguous part of an array.",
        "difficulty": "medium",
        "type": "dsa",
        "role": None,
        "topic": "Arrays",
        "constraints": [
            "1 <= nums.length <= 10^5",
            "-10^4 <= nums[i] <= 10^4"
        ],
        "examples": [
            {"input": "nums = [-2,1,-3,4,-1,2,1,-5,4]", "output": "6"},
            {"input": "nums = [1]", "output": "1"},
            {"input": "nums = [5,4,-1,7,8]", "output": "23"}
        ],
        "test_cases": [
            {"input": "-2 1 -3 4 -1 2 1 -5 4", "expected_output": "6"},
            {"input": "5 4 -1 7 8", "expected_output": "23"}
        ],
        "starter_code": "def max_subarray(nums):\n    # Write your code here\n    pass\n\n# Read input\nnums = list(map(int, input().split()))\nresult = max_subarray(nums)\nprint(result)"
    },
    {
        "title": "Climbing Stairs",
        "description": "You are climbing a staircase. It takes n steps to reach the top.\n\nEach time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?",
        "difficulty": "easy",
        "type": "dsa",
        "role": None,
        "topic": "Dynamic Programming",
        "constraints": [
            "1 <= n <= 45"
        ],
        "examples": [
            {"input": "n = 2", "output": "2"},
            {"input": "n = 3", "output": "3"}
        ],
        "test_cases": [
            {"input": "2", "expected_output": "2"},
            {"input": "5", "expected_output": "8"}
        ],
        "starter_code": "def climb_stairs(n):\n    # Write your code here\n    pass\n\n# Read input\nn = int(input().strip())\nresult = climb_stairs(n)\nprint(result)"
    },
    {
        "title": "Best Time to Buy and Sell Stock",
        "description": "You are given an array prices where prices[i] is the price of a given stock on the ith day.\n\nYou want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.\n\nReturn the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.",
        "difficulty": "easy",
        "type": "dsa",
        "role": None,
        "topic": "Arrays",
        "constraints": [
            "1 <= prices.length <= 10^5",
            "0 <= prices[i] <= 10^4"
        ],
        "examples": [
            {"input": "prices = [7,1,5,3,6,4]", "output": "5"},
            {"input": "prices = [7,6,4,3,1]", "output": "0"}
        ],
        "test_cases": [
            {"input": "7 1 5 3 6 4", "expected_output": "5"},
            {"input": "7 6 4 3 1", "expected_output": "0"}
        ],
        "starter_code": "def max_profit(prices):\n    # Write your code here\n    pass\n\n# Read input\nprices = list(map(int, input().split()))\nresult = max_profit(prices)\nprint(result)"
    },
    {
        "title": "Contains Duplicate",
        "description": "Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.",
        "difficulty": "easy",
        "type": "dsa",
        "role": None,
        "topic": "Arrays",
        "constraints": [
            "1 <= nums.length <= 10^5",
            "-10^9 <= nums[i] <= 10^9"
        ],
        "examples": [
            {"input": "nums = [1,2,3,1]", "output": "True"},
            {"input": "nums = [1,2,3,4]", "output": "False"},
            {"input": "nums = [1,1,1,3,3,4,3,2,4,2]", "output": "True"}
        ],
        "test_cases": [
            {"input": "1 2 3 1", "expected_output": "True"},
            {"input": "1 2 3 4", "expected_output": "False"}
        ],
        "starter_code": "def contains_duplicate(nums):\n    # Write your code here\n    pass\n\n# Read input\nnums = list(map(int, input().split()))\nresult = contains_duplicate(nums)\nprint(result)"
    },
    {
        "title": "Majority Element",
        "description": "Given an array nums of size n, return the majority element.\n\nThe majority element is the element that appears more than n / 2 times. You may assume that the majority element always exists in the array.",
        "difficulty": "easy",
        "type": "dsa",
        "role": None,
        "topic": "Arrays",
        "constraints": [
            "n == nums.length",
            "1 <= n <= 5 * 10^4",
            "-10^9 <= nums[i] <= 10^9"
        ],
        "examples": [
            {"input": "nums = [3,2,3]", "output": "3"},
            {"input": "nums = [2,2,1,1,1,2,2]", "output": "2"}
        ],
        "test_cases": [
            {"input": "3 2 3", "expected_output": "3"},
            {"input": "2 2 1 1 1 2 2", "expected_output": "2"}
        ],
        "starter_code": "def majority_element(nums):\n    # Write your code here\n    pass\n\n# Read input\nnums = list(map(int, input().split()))\nresult = majority_element(nums)\nprint(result)"
    },
    {
        "title": "Move Zeroes",
        "description": "Given an integer array nums, move all 0s to the end of it while maintaining the relative order of the non-zero elements.\n\nNote that you must do this in-place without making a copy of the array.",
        "difficulty": "easy",
        "type": "dsa",
        "role": None,
        "topic": "Arrays",
        "constraints": [
            "1 <= nums.length <= 10^4",
            "-2^31 <= nums[i] <= 2^31 - 1"
        ],
        "examples": [
            {"input": "nums = [0,1,0,3,12]", "output": "[1,3,12,0,0]"},
            {"input": "nums = [0]", "output": "[0]"}
        ],
        "test_cases": [
            {"input": "0 1 0 3 12", "expected_output": "[1, 3, 12, 0, 0]"},
            {"input": "0", "expected_output": "[0]"}
        ],
        "starter_code": "def move_zeroes(nums):\n    # Write your code here\n    pass\n\n# Read input\nnums = list(map(int, input().split()))\nmove_zeroes(nums)\nprint(nums)"
    },
    {
        "title": "Palindrome Number",
        "description": "Given an integer x, return true if x is a palindrome, and false otherwise.\n\nAn integer is a palindrome when it reads the same forward and backward.",
        "difficulty": "easy",
        "type": "dsa",
        "role": None,
        "topic": "Math",
        "constraints": [
            "-2^31 <= x <= 2^31 - 1"
        ],
        "examples": [
            {"input": "x = 121", "output": "True"},
            {"input": "x = -121", "output": "False"},
            {"input": "x = 10", "output": "False"}
        ],
        "test_cases": [
            {"input": "121", "expected_output": "True"},
            {"input": "-121", "expected_output": "False"},
            {"input": "10", "expected_output": "False"}
        ],
        "starter_code": "def is_palindrome(x):\n    # Write your code here\n    pass\n\n# Read input\nx = int(input().strip())\nresult = is_palindrome(x)\nprint(result)"
    },
    {
        "title": "Linked List Cycle",
        "description": "Given head, the head of a linked list, determine if the linked list has a cycle in it.\n\nThere is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.\n\nReturn true if there is a cycle in the linked list. Otherwise, return false.",
        "difficulty": "easy",
        "type": "dsa",
        "role": None,
        "topic": "Linked Lists",
        "constraints": [
            "The number of the nodes in the list is in the range [0, 10^4].",
            "-10^5 <= Node.val <= 10^5"
        ],
        "examples": [
            {"input": "head = [3,2,0,-4], pos = 1", "output": "True"},
            {"input": "head = [1,2], pos = 0", "output": "True"},
            {"input": "head = [1], pos = -1", "output": "False"}
        ],
        "test_cases": [
            {"input": "3 2 0 -4\n1", "expected_output": "True"},
            {"input": "1\n-1", "expected_output": "False"}
        ],
        "starter_code": "def has_cycle(values, pos):\n    # Simulate cycle detection using Floyd's algorithm\n    # Write your code here\n    pass\n\n# Read input\nvalues = list(map(int, input().split()))\npos = int(input().strip())\nresult = has_cycle(values, pos)\nprint(result)"
    },
    {
        "title": "Maximum Depth of Binary Tree",
        "description": "Given the root of a binary tree, return its maximum depth.\n\nA binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.",
        "difficulty": "easy",
        "type": "dsa",
        "role": None,
        "topic": "Trees",
        "constraints": [
            "The number of nodes in the tree is in the range [0, 10^4].",
            "-100 <= Node.val <= 100"
        ],
        "examples": [
            {"input": "root = [3,9,20,null,null,15,7]", "output": "3"},
            {"input": "root = [1,null,2]", "output": "2"}
        ],
        "test_cases": [
            {"input": "3 9 20 -1 -1 15 7", "expected_output": "3"},
            {"input": "1 -1 2", "expected_output": "2"}
        ],
        "starter_code": "def max_depth(level_order):\n    # -1 represents null nodes\n    # Write your code here\n    pass\n\n# Read input\nnodes = list(map(int, input().split()))\nresult = max_depth(nodes)\nprint(result)"
    },
    {
        "title": "Invert Binary Tree",
        "description": "Given the root of a binary tree, invert the tree, and return its root.\n\nInverting a binary tree means swapping every left node with its corresponding right node.",
        "difficulty": "easy",
        "type": "dsa",
        "role": None,
        "topic": "Trees",
        "constraints": [
            "The number of nodes in the tree is in the range [0, 100].",
            "-100 <= Node.val <= 100"
        ],
        "examples": [
            {"input": "root = [4,2,7,1,3,6,9]", "output": "[4,7,2,9,6,3,1]"},
            {"input": "root = [2,1,3]", "output": "[2,3,1]"}
        ],
        "test_cases": [
            {"input": "4 2 7 1 3 6 9", "expected_output": "[4, 7, 2, 9, 6, 3, 1]"},
            {"input": "2 1 3", "expected_output": "[2, 3, 1]"}
        ],
        "starter_code": "def invert_tree(level_order):\n    # -1 represents null nodes\n    # Write your code here\n    pass\n\n# Read input\nnodes = list(map(int, input().split()))\nresult = invert_tree(nodes)\nprint(result)"
    },
    {
        "title": "Longest Common Prefix",
        "description": "Write a function to find the longest common prefix string amongst an array of strings.\n\nIf there is no common prefix, return an empty string \"\".",
        "difficulty": "easy",
        "type": "dsa",
        "role": None,
        "topic": "Strings",
        "constraints": [
            "1 <= strs.length <= 200",
            "0 <= strs[i].length <= 200",
            "strs[i] consists of only lowercase English letters."
        ],
        "examples": [
            {"input": "strs = ['flower','flow','flight']", "output": "'fl'"},
            {"input": "strs = ['dog','racecar','car']", "output": "''"}
        ],
        "test_cases": [
            {"input": "flower flow flight", "expected_output": "fl"},
            {"input": "dog racecar car", "expected_output": ""}
        ],
        "starter_code": "def longest_common_prefix(strs):\n    # Write your code here\n    pass\n\n# Read input\nstrs = input().strip().split()\nresult = longest_common_prefix(strs)\nprint(result)"
    },
    {
        "title": "3Sum",
        "description": "Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.\n\nNotice that the solution set must not contain duplicate triplets.",
        "difficulty": "medium",
        "type": "dsa",
        "role": None,
        "topic": "Arrays",
        "constraints": [
            "3 <= nums.length <= 3000",
            "-10^5 <= nums[i] <= 10^5"
        ],
        "examples": [
            {"input": "nums = [-1,0,1,2,-1,-4]", "output": "[[-1,-1,2],[-1,0,1]]"},
            {"input": "nums = [0,1,1]", "output": "[]"},
            {"input": "nums = [0,0,0]", "output": "[[0,0,0]]"}
        ],
        "test_cases": [
            {"input": "-1 0 1 2 -1 -4", "expected_output": "[[-1, -1, 2], [-1, 0, 1]]"},
            {"input": "0 0 0", "expected_output": "[[0, 0, 0]]"}
        ],
        "starter_code": "def three_sum(nums):\n    # Write your code here\n    pass\n\n# Read input\nnums = list(map(int, input().split()))\nresult = three_sum(nums)\nprint(result)"
    },
    {
        "title": "Product of Array Except Self",
        "description": "Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].\n\nYou must write an algorithm that runs in O(n) time and without using the division operation.",
        "difficulty": "medium",
        "type": "dsa",
        "role": None,
        "topic": "Arrays",
        "constraints": [
            "2 <= nums.length <= 10^5",
            "-30 <= nums[i] <= 30",
            "The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer."
        ],
        "examples": [
            {"input": "nums = [1,2,3,4]", "output": "[24,12,8,6]"},
            {"input": "nums = [-1,1,0,-3,3]", "output": "[0,0,9,0,0]"}
        ],
        "test_cases": [
            {"input": "1 2 3 4", "expected_output": "[24, 12, 8, 6]"},
            {"input": "-1 1 0 -3 3", "expected_output": "[0, 0, 9, 0, 0]"}
        ],
        "starter_code": "def product_except_self(nums):\n    # Write your code here\n    pass\n\n# Read input\nnums = list(map(int, input().split()))\nresult = product_except_self(nums)\nprint(result)"
    },
    {
        "title": "Find Minimum in Rotated Sorted Array",
        "description": "Suppose an array of length n sorted in ascending order is rotated between 1 and n times.\n\nGiven the sorted rotated array nums of unique elements, return the minimum element of this array.\n\nYou must write an algorithm that runs in O(log n) time.",
        "difficulty": "medium",
        "type": "dsa",
        "role": None,
        "topic": "Binary Search",
        "constraints": [
            "n == nums.length",
            "1 <= n <= 5000",
            "-5000 <= nums[i] <= 5000",
            "All the integers of nums are unique."
        ],
        "examples": [
            {"input": "nums = [3,4,5,1,2]", "output": "1"},
            {"input": "nums = [4,5,6,7,0,1,2]", "output": "0"},
            {"input": "nums = [11,13,15,17]", "output": "11"}
        ],
        "test_cases": [
            {"input": "3 4 5 1 2", "expected_output": "1"},
            {"input": "4 5 6 7 0 1 2", "expected_output": "0"}
        ],
        "starter_code": "def find_min(nums):\n    # Write your code here\n    pass\n\n# Read input\nnums = list(map(int, input().split()))\nresult = find_min(nums)\nprint(result)"
    },
    {
        "title": "Number of Islands",
        "description": "Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.\n\nAn island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.",
        "difficulty": "medium",
        "type": "dsa",
        "role": None,
        "topic": "Graphs",
        "constraints": [
            "m == grid.length",
            "n == grid[i].length",
            "1 <= m, n <= 300",
            "grid[i][j] is '0' or '1'."
        ],
        "examples": [
            {"input": "grid = [['1','1','1','1','0'],['1','1','0','1','0'],['1','1','0','0','0'],['0','0','0','0','0']]", "output": "1"},
            {"input": "grid = [['1','1','0','0','0'],['1','1','0','0','0'],['0','0','1','0','0'],['0','0','0','1','1']]", "output": "3"}
        ],
        "test_cases": [
            {"input": "1 1 1 1 0\n1 1 0 1 0\n1 1 0 0 0\n0 0 0 0 0", "expected_output": "1"},
            {"input": "1 1 0 0 0\n1 1 0 0 0\n0 0 1 0 0\n0 0 0 1 1", "expected_output": "3"}
        ],
        "starter_code": "def num_islands(grid):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\ngrid = [row.split() for row in lines]\nresult = num_islands(grid)\nprint(result)"
    },
    {
        "title": "Coin Change",
        "description": "You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.\n\nReturn the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.",
        "difficulty": "medium",
        "type": "dsa",
        "role": None,
        "topic": "Dynamic Programming",
        "constraints": [
            "1 <= coins.length <= 12",
            "1 <= coins[i] <= 2^31 - 1",
            "0 <= amount <= 10^4"
        ],
        "examples": [
            {"input": "coins = [1,2,5], amount = 11", "output": "3"},
            {"input": "coins = [2], amount = 3", "output": "-1"},
            {"input": "coins = [1], amount = 0", "output": "0"}
        ],
        "test_cases": [
            {"input": "1 2 5\n11", "expected_output": "3"},
            {"input": "2\n3", "expected_output": "-1"}
        ],
        "starter_code": "def coin_change(coins, amount):\n    # Write your code here\n    pass\n\n# Read input\ncoins = list(map(int, input().split()))\namount = int(input().strip())\nresult = coin_change(coins, amount)\nprint(result)"
    },
    {
        "title": "Longest Substring Without Repeating Characters",
        "description": "Given a string s, find the length of the longest substring without repeating characters.",
        "difficulty": "medium",
        "type": "dsa",
        "role": None,
        "topic": "Sliding Window",
        "constraints": [
            "0 <= s.length <= 5 * 10^4",
            "s consists of English letters, digits, symbols and spaces."
        ],
        "examples": [
            {"input": "s = 'abcabcbb'", "output": "3"},
            {"input": "s = 'bbbbb'", "output": "1"},
            {"input": "s = 'pwwkew'", "output": "3"}
        ],
        "test_cases": [
            {"input": "abcabcbb", "expected_output": "3"},
            {"input": "bbbbb", "expected_output": "1"},
            {"input": "pwwkew", "expected_output": "3"}
        ],
        "starter_code": "def length_of_longest_substring(s):\n    # Write your code here\n    pass\n\n# Read input\ns = input().strip()\nresult = length_of_longest_substring(s)\nprint(result)"
    },
    {
        "title": "Validate Binary Search Tree",
        "description": "Given the root of a binary tree, determine if it is a valid binary search tree (BST).\n\nA valid BST is defined as follows:\n- The left subtree of a node contains only nodes with keys less than the node's key.\n- The right subtree of a node contains only nodes with keys greater than the node's key.\n- Both the left and right subtrees must also be binary search trees.",
        "difficulty": "medium",
        "type": "dsa",
        "role": None,
        "topic": "Trees",
        "constraints": [
            "The number of nodes in the tree is in the range [1, 10^4].",
            "-2^31 <= Node.val <= 2^31 - 1"
        ],
        "examples": [
            {"input": "root = [2,1,3]", "output": "True"},
            {"input": "root = [5,1,4,null,null,3,6]", "output": "False"}
        ],
        "test_cases": [
            {"input": "2 1 3", "expected_output": "True"},
            {"input": "5 1 4 -1 -1 3 6", "expected_output": "False"}
        ],
        "starter_code": "def is_valid_bst(level_order):\n    # -1 represents null nodes\n    # Write your code here\n    pass\n\n# Read input\nnodes = list(map(int, input().split()))\nresult = is_valid_bst(nodes)\nprint(result)"
    },
    {
        "title": "Top K Frequent Elements",
        "description": "Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.\n\nYou must solve it in better than O(n log n) time complexity.",
        "difficulty": "medium",
        "type": "dsa",
        "role": None,
        "topic": "Heap",
        "constraints": [
            "1 <= nums.length <= 10^5",
            "-10^4 <= nums[i] <= 10^4",
            "k is in the range [1, the number of unique elements in the array]."
        ],
        "examples": [
            {"input": "nums = [1,1,1,2,2,3], k = 2", "output": "[1,2]"},
            {"input": "nums = [1], k = 1", "output": "[1]"}
        ],
        "test_cases": [
            {"input": "1 1 1 2 2 3\n2", "expected_output": "[1, 2]"},
            {"input": "1\n1", "expected_output": "[1]"}
        ],
        "starter_code": "def top_k_frequent(nums, k):\n    # Write your code here\n    pass\n\n# Read input\nnums = list(map(int, input().split()))\nk = int(input().strip())\nresult = top_k_frequent(nums, k)\nprint(result)"
    },
    {
        "title": "Course Schedule",
        "description": "There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.\n\nYou are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.\n\nReturn true if you can finish all courses. Otherwise, return false.",
        "difficulty": "medium",
        "type": "dsa",
        "role": None,
        "topic": "Graphs",
        "constraints": [
            "1 <= numCourses <= 2000",
            "0 <= prerequisites.length <= 5000",
            "prerequisites[i].length == 2",
            "0 <= ai, bi < numCourses",
            "All the pairs prerequisites[i] are unique."
        ],
        "examples": [
            {"input": "numCourses = 2, prerequisites = [[1,0]]", "output": "True"},
            {"input": "numCourses = 2, prerequisites = [[1,0],[0,1]]", "output": "False"}
        ],
        "test_cases": [
            {"input": "2\n1 0", "expected_output": "True"},
            {"input": "2\n1 0\n0 1", "expected_output": "False"}
        ],
        "starter_code": "def can_finish(numCourses, prerequisites):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nnumCourses = int(lines[0])\nprerequisites = [list(map(int, line.split())) for line in lines[1:] if line]\nresult = can_finish(numCourses, prerequisites)\nprint(result)"
    }
]


# Sample Domain Questions (Frontend)
frontend_questions = [
    {
        "title": "Create Button Component",
        "description": "Create a Python function that generates HTML markup for a customizable button component.\n\nThe function should accept parameters for button text, color, and size, and return the HTML string.",
        "difficulty": "easy",
        "type": "domain",
        "role": "frontend",
        "topic": "HTML Components",
        "constraints": [
            "Button text should be escaped for HTML safety",
            "Valid colors: 'primary', 'secondary', 'danger'",
            "Valid sizes: 'small', 'medium', 'large'"
        ],
        "examples": [
            {"input": "text='Click Me', color='primary', size='medium'", "output": "<button class='btn-primary btn-medium'>Click Me</button>"}
        ],
        "test_cases": [
            {"input": "Click Me\nprimary\nmedium", "expected_output": "<button class='btn-primary btn-medium'>Click Me</button>"},
            {"input": "Submit\ndanger\nlarge", "expected_output": "<button class='btn-danger btn-large'>Submit</button>"}
        ],
        "starter_code": "def create_button(text, color, size):\n    # Write your code here\n    return f\"<button class='btn-{color} btn-{size}'>{text}</button>\"\n\n# Read input\ntext = input().strip()\ncolor = input().strip()\nsize = input().strip()\nresult = create_button(text, color, size)\nprint(result)"
    },
    {
        "title": "CSS Flexbox Layout",
        "description": "Write a function that generates CSS flexbox properties based on alignment requirements.\n\nGiven justify and align parameters, return a dictionary of CSS properties.",
        "difficulty": "easy",
        "type": "domain",
        "role": "frontend",
        "topic": "CSS",
        "constraints": [
            "Valid justify values: 'start', 'center', 'end', 'space-between'",
            "Valid align values: 'start', 'center', 'end', 'stretch'"
        ],
        "examples": [
            {"input": "justify='center', align='center'", "output": "{'display': 'flex', 'justify-content': 'center', 'align-items': 'center'}"}
        ],
        "test_cases": [
            {"input": "center\ncenter", "expected_output": "{'display': 'flex', 'justify-content': 'center', 'align-items': 'center'}"},
            {"input": "space-between\nstretch", "expected_output": "{'display': 'flex', 'justify-content': 'space-between', 'align-items': 'stretch'}"}
        ],
        "starter_code": "def flexbox_css(justify, align):\n    # Write your code here\n    return {\n        'display': 'flex',\n        'justify-content': justify,\n        'align-items': align\n    }\n\n# Read input\njustify = input().strip()\nalign = input().strip()\nresult = flexbox_css(justify, align)\nprint(result)"
    },

    {
        "title": "Generate Unordered List",
        "description": "Create a Python function that generates HTML markup for an unordered list.\n\nThe function should accept a list of strings and return a complete HTML <ul> element with each item wrapped in <li> tags.",
        "difficulty": "easy",
        "type": "domain",
        "role": "frontend",
        "topic": "HTML Components",
        "constraints": [
            "Each item must be wrapped in <li> tags",
            "All items must be wrapped in a single <ul> tag",
            "Empty list should return <ul></ul>"
        ],
        "examples": [
            {"input": "items = ['Apple', 'Banana', 'Cherry']", "output": "<ul><li>Apple</li><li>Banana</li><li>Cherry</li></ul>"}
        ],
        "test_cases": [
            {"input": "Apple\nBanana\nCherry", "expected_output": "<ul><li>Apple</li><li>Banana</li><li>Cherry</li></ul>"},
            {"input": "Home\nAbout\nContact", "expected_output": "<ul><li>Home</li><li>About</li><li>Contact</li></ul>"}
        ],
        "starter_code": "def generate_ul(items):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nitems = [line.strip() for line in sys.stdin.read().strip().split('\\n')]\nresult = generate_ul(items)\nprint(result)"
    },
    {
        "title": "Build Navigation Bar",
        "description": "Create a Python function that generates HTML markup for a navigation bar.\n\nThe function should accept a list of tuples (label, href) and return a <nav> element containing an <ul> with anchor links.",
        "difficulty": "easy",
        "type": "domain",
        "role": "frontend",
        "topic": "HTML Components",
        "constraints": [
            "Each link must be an <a> tag inside an <li> tag",
            "All <li> tags must be inside a <ul> tag",
            "The <ul> must be inside a <nav> tag"
        ],
        "examples": [
            {"input": "links = [('Home', '/'), ('About', '/about')]", "output": "<nav><ul><li><a href='/'>Home</a></li><li><a href='/about'>About</a></li></ul></nav>"}
        ],
        "test_cases": [
            {"input": "Home /\nAbout /about", "expected_output": "<nav><ul><li><a href='/'>Home</a></li><li><a href='/about'>About</a></li></ul></nav>"},
            {"input": "Blog /blog\nContact /contact", "expected_output": "<nav><ul><li><a href='/blog'>Blog</a></li><li><a href='/contact'>Contact</a></li></ul></nav>"}
        ],
        "starter_code": "def build_navbar(links):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nlinks = [tuple(line.strip().split()) for line in lines]\nresult = build_navbar(links)\nprint(result)"
    },
    {
        "title": "Generate Input Field",
        "description": "Create a Python function that generates HTML markup for a form input field with a label.\n\nThe function should accept a label text, input type, and placeholder, and return a <div> wrapping both the <label> and <input> elements.",
        "difficulty": "easy",
        "type": "domain",
        "role": "frontend",
        "topic": "HTML Forms",
        "constraints": [
            "Valid types: 'text', 'email', 'password', 'number'",
            "The label's 'for' attribute must match the input's 'id' attribute",
            "The id is the label text lowercased with spaces replaced by hyphens"
        ],
        "examples": [
            {"input": "label='Email Address', type='email', placeholder='Enter email'", "output": "<div><label for='email-address'>Email Address</label><input type='email' id='email-address' placeholder='Enter email'/></div>"}
        ],
        "test_cases": [
            {"input": "Email Address\nemail\nEnter email", "expected_output": "<div><label for='email-address'>Email Address</label><input type='email' id='email-address' placeholder='Enter email'/></div>"},
            {"input": "Full Name\ntext\nEnter your name", "expected_output": "<div><label for='full-name'>Full Name</label><input type='text' id='full-name' placeholder='Enter your name'/></div>"}
        ],
        "starter_code": "def generate_input(label, input_type, placeholder):\n    # Write your code here\n    pass\n\n# Read input\nlabel = input().strip()\ninput_type = input().strip()\nplaceholder = input().strip()\nresult = generate_input(label, input_type, placeholder)\nprint(result)"
    },
    {
        "title": "Build Card Component",
        "description": "Create a Python function that generates HTML markup for a card component.\n\nThe function should accept a title, description, and image URL, and return a <div class='card'> containing the image, title, and description.",
        "difficulty": "easy",
        "type": "domain",
        "role": "frontend",
        "topic": "HTML Components",
        "constraints": [
            "Image must use the provided URL as the src attribute",
            "Title must be wrapped in an <h2> tag",
            "Description must be wrapped in a <p> tag",
            "Order must be: img, h2, p"
        ],
        "examples": [
            {"input": "title='My Card', description='Some text', image_url='img.png'", "output": "<div class='card'><img src='img.png'/><h2>My Card</h2><p>Some text</p></div>"}
        ],
        "test_cases": [
            {"input": "My Card\nSome text\nimg.png", "expected_output": "<div class='card'><img src='img.png'/><h2>My Card</h2><p>Some text</p></div>"},
            {"input": "Product\nBest product ever\nproduct.jpg", "expected_output": "<div class='card'><img src='product.jpg'/><h2>Product</h2><p>Best product ever</p></div>"}
        ],
        "starter_code": "def build_card(title, description, image_url):\n    # Write your code here\n    pass\n\n# Read input\ntitle = input().strip()\ndescription = input().strip()\nimage_url = input().strip()\nresult = build_card(title, description, image_url)\nprint(result)"
    },
    {
        "title": "CSS Specificity Calculator",
        "description": "Create a Python function that calculates the CSS specificity score of a given selector string.\n\nSpecificity is calculated as: IDs count as 100, classes/attributes/pseudo-classes count as 10, and elements/pseudo-elements count as 1.",
        "difficulty": "medium",
        "type": "domain",
        "role": "frontend",
        "topic": "CSS",
        "constraints": [
            "IDs are prefixed with '#'",
            "Classes are prefixed with '.'",
            "Everything else is treated as an element selector",
            "Selector parts are separated by spaces"
        ],
        "examples": [
            {"input": "selector = '#nav .link a'", "output": "111"},
            {"input": "selector = '#header'", "output": "100"}
        ],
        "test_cases": [
            {"input": "#nav .link a", "expected_output": "111"},
            {"input": "#header .nav .item span", "expected_output": "121"}
        ],
        "starter_code": "def css_specificity(selector):\n    # Write your code here\n    pass\n\n# Read input\nselector = input().strip()\nresult = css_specificity(selector)\nprint(result)"
    },
    {
        "title": "Kebab Case Converter",
        "description": "Create a Python function that converts a camelCase or PascalCase string into kebab-case.\n\nThis is commonly used when converting JavaScript variable names into CSS class names.",
        "difficulty": "easy",
        "type": "domain",
        "role": "frontend",
        "topic": "CSS",
        "constraints": [
            "Output must be all lowercase",
            "Words must be separated by hyphens",
            "Consecutive uppercase letters should each be treated as a new word"
        ],
        "examples": [
            {"input": "s = 'backgroundColor'", "output": "background-color"},
            {"input": "s = 'MyComponentName'", "output": "my-component-name"}
        ],
        "test_cases": [
            {"input": "backgroundColor", "expected_output": "background-color"},
            {"input": "MyComponentName", "expected_output": "my-component-name"},
            {"input": "fontSize", "expected_output": "font-size"}
        ],
        "starter_code": "def to_kebab_case(s):\n    # Write your code here\n    pass\n\n# Read input\ns = input().strip()\nresult = to_kebab_case(s)\nprint(result)"
    },
    {
        "title": "Hex to RGB Converter",
        "description": "Create a Python function that converts a hex color code to its RGB representation.\n\nThe function should accept a hex string (with or without '#') and return a string in the format 'rgb(r, g, b)'.",
        "difficulty": "easy",
        "type": "domain",
        "role": "frontend",
        "topic": "CSS",
        "constraints": [
            "Input may or may not include the leading '#'",
            "Both 3-digit and 6-digit hex codes must be supported",
            "Output format must be exactly 'rgb(r, g, b)'"
        ],
        "examples": [
            {"input": "hex = '#ff5733'", "output": "rgb(255, 87, 51)"},
            {"input": "hex = 'fff'", "output": "rgb(255, 255, 255)"}
        ],
        "test_cases": [
            {"input": "#ff5733", "expected_output": "rgb(255, 87, 51)"},
            {"input": "fff", "expected_output": "rgb(255, 255, 255)"},
            {"input": "#000000", "expected_output": "rgb(0, 0, 0)"}
        ],
        "starter_code": "def hex_to_rgb(hex_color):\n    # Write your code here\n    pass\n\n# Read input\nhex_color = input().strip()\nresult = hex_to_rgb(hex_color)\nprint(result)"
    },
    {
        "title": "Build HTML Table",
        "description": "Create a Python function that generates an HTML table from a list of headers and rows.\n\nThe function should produce a <table> with a <thead> containing <th> elements and a <tbody> containing <tr> rows with <td> cells.",
        "difficulty": "medium",
        "type": "domain",
        "role": "frontend",
        "topic": "HTML Components",
        "constraints": [
            "Headers must be inside <th> tags within a <thead><tr>",
            "Data rows must be inside <td> tags within <tbody><tr>",
            "Number of columns in each row matches the number of headers"
        ],
        "examples": [
            {"input": "headers = ['Name', 'Age'], rows = [['Alice', '30'], ['Bob', '25']]", "output": "<table><thead><tr><th>Name</th><th>Age</th></tr></thead><tbody><tr><td>Alice</td><td>30</td></tr><tr><td>Bob</td><td>25</td></tr></tbody></table>"}
        ],
        "test_cases": [
            {"input": "Name Age\nAlice 30\nBob 25", "expected_output": "<table><thead><tr><th>Name</th><th>Age</th></tr></thead><tbody><tr><td>Alice</td><td>30</td></tr><tr><td>Bob</td><td>25</td></tr></tbody></table>"},
            {"input": "Product Price\nApple 1.99\nBread 2.49", "expected_output": "<table><thead><tr><th>Product</th><th>Price</th></tr></thead><tbody><tr><td>Apple</td><td>1.99</td></tr><tr><td>Bread</td><td>2.49</td></tr></tbody></table>"}
        ],
        "starter_code": "def build_table(headers, rows):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nheaders = lines[0].split()\nrows = [line.split() for line in lines[1:]]\nresult = build_table(headers, rows)\nprint(result)"
    },
    {
        "title": "Generate Breadcrumb",
        "description": "Create a Python function that generates an HTML breadcrumb navigation component.\n\nThe function accepts a list of tuples (label, url) and returns a <nav class='breadcrumb'> where each item is an <a> tag, with items separated by a <span class='separator'>></span>. The last item has no link and is wrapped in a <span class='active'> tag instead.",
        "difficulty": "medium",
        "type": "domain",
        "role": "frontend",
        "topic": "HTML Components",
        "constraints": [
            "All items except the last must be <a> tags",
            "The last item must be a <span class='active'> with no href",
            "Items must be separated by <span class='separator'>></span>"
        ],
        "examples": [
            {"input": "crumbs = [('Home', '/'), ('Products', '/products'), ('Shoes', '')]", "output": "<nav class='breadcrumb'><a href='/'>Home</a><span class='separator'>></span><a href='/products'>Products</a><span class='separator'>></span><span class='active'>Shoes</span></nav>"}
        ],
        "test_cases": [
            {"input": "Home /\nProducts /products\nShoes ", "expected_output": "<nav class='breadcrumb'><a href='/'>Home</a><span class='separator'>></span><a href='/products'>Products</a><span class='separator'>></span><span class='active'>Shoes</span></nav>"},
            {"input": "Home /\nBlog /blog\nPost ", "expected_output": "<nav class='breadcrumb'><a href='/'>Home</a><span class='separator'>></span><a href='/blog'>Blog</a><span class='separator'>></span><span class='active'>Post</span></nav>"}
        ],
        "starter_code": "def generate_breadcrumb(crumbs):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\ncrumbs = [(parts[0], parts[1] if len(parts) > 1 else '') for parts in [line.split() for line in lines]]\nresult = generate_breadcrumb(crumbs)\nprint(result)"
    },
    {
        "title": "Flatten Nested CSS Object",
        "description": "Create a Python function that takes a nested dictionary representing CSS rules and flattens it into a CSS string.\n\nEach key at the top level is a selector, and its value is a dictionary of property-value pairs.",
        "difficulty": "medium",
        "type": "domain",
        "role": "frontend",
        "topic": "CSS",
        "constraints": [
            "Each rule must end with a semicolon",
            "Properties and values are separated by ': '",
            "Format: selector { property: value; }"
        ],
        "examples": [
            {"input": "rules = {'body': {'margin': '0', 'padding': '0'}}", "output": "body { margin: 0; padding: 0; }"}
        ],
        "test_cases": [
            {"input": "body\nmargin 0\npadding 0", "expected_output": "body { margin: 0; padding: 0; }"},
            {"input": ".card\nbackground white\nborder-radius 8px", "expected_output": ".card { background: white; border-radius: 8px; }"}
        ],
        "starter_code": "def flatten_css(selector, properties):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nselector = lines[0]\nproperties = dict(line.split() for line in lines[1:])\nresult = flatten_css(selector, properties)\nprint(result)"
    },
    {
        "title": "Modal HTML Generator",
        "description": "Create a Python function that generates HTML markup for a modal dialog component.\n\nThe function should accept a title and body text and return a modal structure with an overlay, header, body, and close button.",
        "difficulty": "medium",
        "type": "domain",
        "role": "frontend",
        "topic": "HTML Components",
        "constraints": [
            "Outer wrapper must be <div class='modal-overlay'>",
            "Inner wrapper must be <div class='modal'>",
            "Header must be <div class='modal-header'> containing an <h2> and a <button class='close'>X</button>",
            "Body must be <div class='modal-body'> containing a <p> tag"
        ],
        "examples": [
            {"input": "title='Alert', body='This is a warning.'", "output": "<div class='modal-overlay'><div class='modal'><div class='modal-header'><h2>Alert</h2><button class='close'>X</button></div><div class='modal-body'><p>This is a warning.</p></div></div></div>"}
        ],
        "test_cases": [
            {"input": "Alert\nThis is a warning.", "expected_output": "<div class='modal-overlay'><div class='modal'><div class='modal-header'><h2>Alert</h2><button class='close'>X</button></div><div class='modal-body'><p>This is a warning.</p></div></div></div>"},
            {"input": "Confirm\nAre you sure?", "expected_output": "<div class='modal-overlay'><div class='modal'><div class='modal-header'><h2>Confirm</h2><button class='close'>X</button></div><div class='modal-body'><p>Are you sure?</p></div></div></div>"}
        ],
        "starter_code": "def generate_modal(title, body):\n    # Write your code here\n    pass\n\n# Read input\ntitle = input().strip()\nbody = input().strip()\nresult = generate_modal(title, body)\nprint(result)"
    },
    {
        "title": "Parse Query String",
        "description": "Create a Python function that parses a URL query string into a dictionary.\n\nThe function should accept a query string (without the leading '?') and return a dictionary of key-value pairs.",
        "difficulty": "easy",
        "type": "domain",
        "role": "frontend",
        "topic": "JavaScript Concepts",
        "constraints": [
            "Parameters are separated by '&'",
            "Key and value are separated by '='",
            "If a key has no value, its value should be an empty string",
            "Return keys in the order they appear"
        ],
        "examples": [
            {"input": "query = 'name=Alice&age=30&city=NYC'", "output": "{'name': 'Alice', 'age': '30', 'city': 'NYC'}"},
            {"input": "query = 'debug&version=2'", "output": "{'debug': '', 'version': '2'}"}
        ],
        "test_cases": [
            {"input": "name=Alice&age=30&city=NYC", "expected_output": "{'name': 'Alice', 'age': '30', 'city': 'NYC'}"},
            {"input": "debug&version=2", "expected_output": "{'debug': '', 'version': '2'}"}
        ],
        "starter_code": "def parse_query_string(query):\n    # Write your code here\n    pass\n\n# Read input\nquery = input().strip()\nresult = parse_query_string(query)\nprint(result)"
    },
    {
        "title": "Debounce Simulator",
        "description": "Create a Python function that simulates debounce behavior.\n\nGiven a list of event timestamps (in milliseconds) and a debounce delay, return only the timestamps that would actually trigger the function — i.e., timestamps where no subsequent event occurs within the delay window.",
        "difficulty": "medium",
        "type": "domain",
        "role": "frontend",
        "topic": "JavaScript Concepts",
        "constraints": [
            "Timestamps are in ascending order",
            "An event fires only if no other event occurs within 'delay' ms after it",
            "The last event always fires"
        ],
        "examples": [
            {"input": "timestamps = [100, 200, 500, 1000], delay = 150", "output": "[200, 500, 1000]"},
            {"input": "timestamps = [100, 300, 600], delay = 150", "output": "[100, 300, 600]"}
        ],
        "test_cases": [
            {"input": "100 200 500 1000\n150", "expected_output": "[200, 500, 1000]"},
            {"input": "100 300 600\n150", "expected_output": "[100, 300, 600]"}
        ],
        "starter_code": "def debounce_filter(timestamps, delay):\n    # Write your code here\n    pass\n\n# Read input\ntimestamps = list(map(int, input().split()))\ndelay = int(input().strip())\nresult = debounce_filter(timestamps, delay)\nprint(result)"
    },
    {
        "title": "Generate Pagination Component",
        "description": "Create a Python function that generates HTML markup for a pagination component.\n\nGiven the total number of pages and the current page, return a <div class='pagination'> with a button for each page. The current page's button should have class 'active'.",
        "difficulty": "medium",
        "type": "domain",
        "role": "frontend",
        "topic": "HTML Components",
        "constraints": [
            "Each page button must be a <button> tag",
            "Current page button must have class 'active'",
            "Other buttons must have class 'page'",
            "All buttons must be inside a <div class='pagination'>"
        ],
        "examples": [
            {"input": "total_pages = 3, current_page = 2", "output": "<div class='pagination'><button class='page'>1</button><button class='active'>2</button><button class='page'>3</button></div>"}
        ],
        "test_cases": [
            {"input": "3\n2", "expected_output": "<div class='pagination'><button class='page'>1</button><button class='active'>2</button><button class='page'>3</button></div>"},
            {"input": "4\n1", "expected_output": "<div class='pagination'><button class='active'>1</button><button class='page'>2</button><button class='page'>3</button><button class='page'>4</button></div>"}
        ],
        "starter_code": "def generate_pagination(total_pages, current_page):\n    # Write your code here\n    pass\n\n# Read input\ntotal_pages = int(input().strip())\ncurrent_page = int(input().strip())\nresult = generate_pagination(total_pages, current_page)\nprint(result)"
    },
    {
        "title": "Responsive Image Tag Builder",
        "description": "Create a Python function that generates an HTML <img> tag with srcset for responsive images.\n\nThe function accepts a base filename (without extension), an extension, and a list of widths. It returns an <img> tag with a srcset attribute listing each width variant.",
        "difficulty": "medium",
        "type": "domain",
        "role": "frontend",
        "topic": "HTML Components",
        "constraints": [
            "Filename pattern: baseName-{width}w.ext",
            "srcset entries are comma-separated",
            "Each srcset entry ends with '{width}w'",
            "The src attribute should point to the largest width variant"
        ],
        "examples": [
            {"input": "base='hero', ext='jpg', widths=[400, 800, 1200]", "output": "<img src='hero-1200w.jpg' srcset='hero-400w.jpg 400w, hero-800w.jpg 800w, hero-1200w.jpg 1200w'/>"}
        ],
        "test_cases": [
            {"input": "hero\njpg\n400 800 1200", "expected_output": "<img src='hero-1200w.jpg' srcset='hero-400w.jpg 400w, hero-800w.jpg 800w, hero-1200w.jpg 1200w'/>"},
            {"input": "banner\npng\n320 640", "expected_output": "<img src='banner-640w.png' srcset='banner-320w.png 320w, banner-640w.png 640w'/>"}
        ],
        "starter_code": "def build_img_tag(base, ext, widths):\n    # Write your code here\n    pass\n\n# Read input\nbase = input().strip()\next = input().strip()\nwidths = list(map(int, input().split()))\nresult = build_img_tag(base, ext, widths)\nprint(result)"
    },
    {
        "title": "Badge Notification Component",
        "description": "Create a Python function that generates HTML for an icon button with a notification badge.\n\nThe function accepts an icon name and a count. If count is 0, no badge is shown. If count is greater than 99, the badge should display '99+'.",
        "difficulty": "easy",
        "type": "domain",
        "role": "frontend",
        "topic": "HTML Components",
        "constraints": [
            "Wrapper must be <div class='icon-wrapper'>",
            "Icon must be <span class='icon'>{icon_name}</span>",
            "Badge must be <span class='badge'>{count}</span>",
            "No badge element should be rendered if count is 0"
        ],
        "examples": [
            {"input": "icon='bell', count=5", "output": "<div class='icon-wrapper'><span class='icon'>bell</span><span class='badge'>5</span></div>"},
            {"input": "icon='bell', count=0", "output": "<div class='icon-wrapper'><span class='icon'>bell</span></div>"},
            {"input": "icon='mail', count=120", "output": "<div class='icon-wrapper'><span class='icon'>mail</span><span class='badge'>99+</span></div>"}
        ],
        "test_cases": [
            {"input": "bell\n5", "expected_output": "<div class='icon-wrapper'><span class='icon'>bell</span><span class='badge'>5</span></div>"},
            {"input": "bell\n0", "expected_output": "<div class='icon-wrapper'><span class='icon'>bell</span></div>"},
            {"input": "mail\n120", "expected_output": "<div class='icon-wrapper'><span class='icon'>mail</span><span class='badge'>99+</span></div>"}
        ],
        "starter_code": "def badge_component(icon, count):\n    # Write your code here\n    pass\n\n# Read input\nicon = input().strip()\ncount = int(input().strip())\nresult = badge_component(icon, count)\nprint(result)"
    },
    {
        "title": "Truncate Text with Ellipsis",
        "description": "Create a Python function that truncates a string to a given max length and appends '...' if truncated.\n\nThis is a common UI utility used to prevent text overflow in cards, tooltips, and table cells.",
        "difficulty": "easy",
        "type": "domain",
        "role": "frontend",
        "topic": "JavaScript Concepts",
        "constraints": [
            "If text length is <= max_length, return it unchanged",
            "If truncated, the total length including '...' must equal max_length",
            "max_length is always >= 3"
        ],
        "examples": [
            {"input": "text='Hello World', max_length=8", "output": "Hello..."},
            {"input": "text='Hi', max_length=10", "output": "Hi"}
        ],
        "test_cases": [
            {"input": "Hello World\n8", "expected_output": "Hello..."},
            {"input": "Hi\n10", "expected_output": "Hi"},
            {"input": "Frontend Development\n12", "expected_output": "Frontend De..."}
        ],
        "starter_code": "def truncate_text(text, max_length):\n    # Write your code here\n    pass\n\n# Read input\ntext = input().strip()\nmax_length = int(input().strip())\nresult = trunc_text(text, max_length)\nprint(result)"
    },
    {
        "title": "Build Select Dropdown",
        "description": "Create a Python function that generates an HTML <select> dropdown element.\n\nThe function accepts a name, a list of options, and a selected value. The matching option must have the 'selected' attribute.",
        "difficulty": "easy",
        "type": "domain",
        "role": "frontend",
        "topic": "HTML Forms",
        "constraints": [
            "The outer element must be <select name='{name}'>",
            "Each option is <option value='{val}'>{val}</option>",
            "The selected option must include the 'selected' attribute",
            "If no option matches selected value, no option has 'selected'"
        ],
        "examples": [
            {"input": "name='color', options=['red','green','blue'], selected='green'", "output": "<select name='color'><option value='red'>red</option><option value='green' selected>green</option><option value='blue'>blue</option></select>"}
        ],
        "test_cases": [
            {"input": "color\nred green blue\ngreen", "expected_output": "<select name='color'><option value='red'>red</option><option value='green' selected>green</option><option value='blue'>blue</option></select>"},
            {"input": "size\nsmall medium large\nlarge", "expected_output": "<select name='size'><option value='small'>small</option><option value='medium'>medium</option><option value='large' selected>large</option></select>"}
        ],
        "starter_code": "def build_select(name, options, selected):\n    # Write your code here\n    pass\n\n# Read input\nname = input().strip()\noptions = input().strip().split()\nselected = input().strip()\nresult = build_select(name, options, selected)\nprint(result)"
    },
    {
        "title": "Calculate Rem Value",
        "description": "Create a Python function that converts a pixel value to rem units.\n\nThis is a common calculation in CSS where the base font size of the document is typically 16px. The function should return a string formatted to 4 decimal places followed by 'rem'.",
        "difficulty": "easy",
        "type": "domain",
        "role": "frontend",
        "topic": "CSS",
        "constraints": [
            "Default base font size is 16px",
            "Formula: px / base = rem",
            "Result must be formatted as '{value}rem' with up to 4 decimal places",
            "Trailing zeros after decimal should be removed"
        ],
        "examples": [
            {"input": "px=24, base=16", "output": "1.5rem"},
            {"input": "px=10, base=16", "output": "0.625rem"}
        ],
        "test_cases": [
            {"input": "24\n16", "expected_output": "1.5rem"},
            {"input": "10\n16", "expected_output": "0.625rem"},
            {"input": "32\n16", "expected_output": "2rem"}
        ],
        "starter_code": "def px_to_rem(px, base=16):\n    # Write your code here\n    pass\n\n# Read input\npx = int(input().strip())\nbase = int(input().strip())\nresult = px_to_rem(px, base)\nprint(result)"
    },
    {
        "title": "Accessibility Checker",
        "description": "Create a Python function that checks whether an HTML <img> tag string is accessible.\n\nAn image is accessible if it contains a non-empty 'alt' attribute. The function should return 'accessible' or 'not accessible'.",
        "difficulty": "easy",
        "type": "domain",
        "role": "frontend",
        "topic": "Accessibility",
        "constraints": [
            "The input is a raw HTML string of an <img> tag",
            "alt='' or missing alt counts as not accessible",
            "Whitespace-only alt values are not accessible"
        ],
        "examples": [
            {"input": "tag = \"<img src='logo.png' alt='Company Logo'/>\"", "output": "accessible"},
            {"input": "tag = \"<img src='logo.png' alt=''/>\"", "output": "not accessible"},
            {"input": "tag = \"<img src='logo.png'/>\"", "output": "not accessible"}
        ],
        "test_cases": [
            {"input": "<img src='logo.png' alt='Company Logo'/>", "expected_output": "accessible"},
            {"input": "<img src='logo.png' alt=''/>", "expected_output": "not accessible"},
            {"input": "<img src='logo.png'/>", "expected_output": "not accessible"}
        ],
        "starter_code": "def check_accessibility(tag):\n    # Write your code here\n    pass\n\n# Read input\ntag = input().strip()\nresult = check_accessibility(tag)\nprint(result)"
    },
    {
        "title": "Generate Meta Tags",
        "description": "Create a Python function that generates HTML <meta> tags for SEO from a dictionary of metadata.\n\nThe function accepts a dictionary with keys like 'description', 'keywords', and 'author', and returns the corresponding <meta> tags as a single string.",
        "difficulty": "easy",
        "type": "domain",
        "role": "frontend",
        "topic": "HTML Components",
        "constraints": [
            "Each meta tag format: <meta name='{key}' content='{value}'>",
            "Tags must appear in the same order as input",
            "No trailing spaces or newlines between tags"
        ],
        "examples": [
            {"input": "meta = {'description': 'A cool site', 'author': 'Alice'}", "output": "<meta name='description' content='A cool site'><meta name='author' content='Alice'>"}
        ],
        "test_cases": [
            {"input": "description A cool site\nauthor Alice", "expected_output": "<meta name='description' content='A cool site'><meta name='author' content='Alice'>"},
            {"input": "keywords python html css\ndescription Learn web dev", "expected_output": "<meta name='keywords' content='python html css'><meta name='description' content='Learn web dev'>"}
        ],
        "starter_code": "def generate_meta_tags(meta):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nmeta = {}\nfor line in lines:\n    parts = line.split(' ', 1)\n    meta[parts[0]] = parts[1]\nresult = generate_meta_tags(meta)\nprint(result)"
    },
    {
        "title": "Toggle Class Simulator",
        "description": "Create a Python function that simulates toggling a CSS class on an element.\n\nGiven a string of current classes and a class name to toggle, return the updated class string. If the class exists, remove it; otherwise, add it.",
        "difficulty": "easy",
        "type": "domain",
        "role": "frontend",
        "topic": "JavaScript Concepts",
        "constraints": [
            "Classes are space-separated",
            "Order of existing classes must be preserved",
            "New class is appended at the end if added",
            "Return an empty string if all classes are removed"
        ],
        "examples": [
            {"input": "classes='btn active primary', toggle='active'", "output": "btn primary"},
            {"input": "classes='btn primary', toggle='active'", "output": "btn primary active"}
        ],
        "test_cases": [
            {"input": "btn active primary\nactive", "expected_output": "btn primary"},
            {"input": "btn primary\nactive", "expected_output": "btn primary active"},
            {"input": "active\nactive", "expected_output": ""}
        ],
        "starter_code": "def toggle_class(classes, toggle):\n    # Write your code here\n    pass\n\n# Read input\nclasses = input().strip()\ntoggle = input().strip()\nresult = toggle_class(classes, toggle)\nprint(result)"
    },
    {
        "title": "Media Query Parser",
        "description": "Create a Python function that parses a CSS media query string and returns a dictionary of its conditions.\n\nThe function should handle 'min-width', 'max-width', and 'orientation' conditions.",
        "difficulty": "medium",
        "type": "domain",
        "role": "frontend",
        "topic": "CSS",
        "constraints": [
            "Input format: '@media (condition: value) and (condition: value)'",
            "Conditions and values are separated by ': '",
            "Return a dict with condition names as keys",
            "Values for widths should be returned as strings including units"
        ],
        "examples": [
            {"input": "query = '@media (min-width: 768px) and (max-width: 1024px)'", "output": "{'min-width': '768px', 'max-width': '1024px'}"},
            {"input": "query = '@media (orientation: landscape)'", "output": "{'orientation': 'landscape'}"}
        ],
        "test_cases": [
            {"input": "@media (min-width: 768px) and (max-width: 1024px)", "expected_output": "{'min-width': '768px', 'max-width': '1024px'}"},
            {"input": "@media (orientation: landscape)", "expected_output": "{'orientation': 'landscape'}"}
        ],
        "starter_code": "def parse_media_query(query):\n    # Write your code here\n    pass\n\n# Read input\nquery = input().strip()\nresult = parse_media_query(query)\nprint(result)"
    },
    {
        "title": "Build Progress Bar",
        "description": "Create a Python function that generates HTML for a progress bar component.\n\nThe function accepts a value (0-100) and returns a <div class='progress-bar'> with an inner <div class='progress-fill'> whose width style is set to the percentage value.",
        "difficulty": "easy",
        "type": "domain",
        "role": "frontend",
        "topic": "HTML Components",
        "constraints": [
            "Outer wrapper must be <div class='progress-bar'>",
            "Inner fill must be <div class='progress-fill' style='width:{value}%'>",
            "Value must be clamped between 0 and 100",
            "No spaces around the colon in the style attribute"
        ],
        "examples": [
            {"input": "value = 75", "output": "<div class='progress-bar'><div class='progress-fill' style='width:75%'></div></div>"},
            {"input": "value = 0", "output": "<div class='progress-bar'><div class='progress-fill' style='width:0%'></div></div>"}
        ],
        "test_cases": [
            {"input": "75", "expected_output": "<div class='progress-bar'><div class='progress-fill' style='width:75%'></div></div>"},
            {"input": "0", "expected_output": "<div class='progress-bar'><div class='progress-fill' style='width:0%'></div></div>"},
            {"input": "110", "expected_output": "<div class='progress-bar'><div class='progress-fill' style='width:100%'></div></div>"}
        ],
        "starter_code": "def build_progress_bar(value):\n    # Write your code here\n    pass\n\n# Read input\nvalue = int(input().strip())\nresult = build_progress_bar(value)\nprint(result)"
    },
    {
        "title": "Color Contrast Checker",
        "description": "Create a Python function that determines whether two hex colors have sufficient contrast for accessibility (WCAG AA standard).\n\nThe relative luminance formula simplifies to: return 'pass' if the contrast ratio >= 4.5, otherwise 'fail'. For simplicity, use the absolute difference of the average RGB values as a proxy: pass if difference >= 128.",
        "difficulty": "hard",
        "type": "domain",
        "role": "frontend",
        "topic": "Accessibility",
        "constraints": [
            "Both inputs are 6-digit hex color strings with '#'",
            "Use simplified contrast check: |avg1 - avg2| >= 128 => pass",
            "avg = (R + G + B) / 3 for each color"
        ],
        "examples": [
            {"input": "color1='#ffffff', color2='#000000'", "output": "pass"},
            {"input": "color1='#aaaaaa', color2='#bbbbbb'", "output": "fail"}
        ],
        "test_cases": [
            {"input": "#ffffff\n#000000", "expected_output": "pass"},
            {"input": "#aaaaaa\n#bbbbbb", "expected_output": "fail"},
            {"input": "#ff0000\n#ffffff", "expected_output": "pass"}
        ],
        "starter_code": "def check_contrast(color1, color2):\n    # Write your code here\n    pass\n\n# Read input\ncolor1 = input().strip()\ncolor2 = input().strip()\nresult = check_contrast(color1, color2)\nprint(result)"
    }
]


# Sample Domain Questions (Backend)
backend_questions = [
    {
        "title": "REST API Endpoint Design",
        "description": "Create a function that validates if a given API endpoint follows REST conventions.\n\nThe function should check if the endpoint uses proper HTTP methods and resource naming.",
        "difficulty": "easy",
        "type": "domain",
        "role": "backend",
        "topic": "API Design",
        "constraints": [
            "Endpoint should start with '/'",
            "Resource names should be plural",
            "No trailing slashes"
        ],
        "examples": [
            {"input": "'/api/users'", "output": "True"},
            {"input": "'/api/user'", "output": "False"}
        ],
        "test_cases": [
            {"input": "/api/users", "expected_output": "True"},
            {"input": "/api/user", "expected_output": "False"},
            {"input": "/api/products", "expected_output": "True"}
        ],
        "starter_code": "def validate_endpoint(endpoint):\n    # Write your code here\n    if not endpoint.startswith('/'):\n        return False\n    if endpoint.endswith('/'):\n        return False\n    parts = endpoint.split('/')\n    resource = parts[-1]\n    # Check if plural (simple check)\n    return resource.endswith('s')\n\n# Read input\nendpoint = input().strip()\nresult = validate_endpoint(endpoint)\nprint(result)"
    },
    {
        "title": "Database Query Builder",
        "description": "Write a function that builds a simple SQL SELECT query from given parameters.\n\nGiven table name, columns, and optional WHERE condition, return the SQL query string.",
        "difficulty": "medium",
        "type": "domain",
        "role": "backend",
        "topic": "Database",
        "constraints": [
            "Table name must be alphanumeric",
            "Columns should be comma-separated",
            "WHERE clause is optional"
        ],
        "examples": [
            {"input": "table='users', columns='id,name,email', where='age > 18'", "output": "SELECT id,name,email FROM users WHERE age > 18"}
        ],
        "test_cases": [
            {"input": "users\nid,name,email\nage > 18", "expected_output": "SELECT id,name,email FROM users WHERE age > 18"},
            {"input": "products\nid,name,price\n", "expected_output": "SELECT id,name,price FROM products"}
        ],
        "starter_code": "def build_query(table, columns, where=''):\n    # Write your code here\n    query = f\"SELECT {columns} FROM {table}\"\n    if where:\n        query += f\" WHERE {where}\"\n    return query\n\n# Read input\ntable = input().strip()\ncolumns = input().strip()\nwhere = input().strip()\nresult = build_query(table, columns, where)\nprint(result)"
    },
    {
        "title": "HTTP Status Code Classifier",
        "description": "Create a function that classifies an HTTP status code into its category.\n\nReturn the category name based on the status code range.",
        "difficulty": "easy",
        "type": "domain",
        "role": "backend",
        "topic": "API Design",
        "constraints": [
            "1xx: Informational",
            "2xx: Success",
            "3xx: Redirection",
            "4xx: Client Error",
            "5xx: Server Error",
            "Return 'Unknown' for anything outside 100-599"
        ],
        "examples": [
            {"input": "code = 200", "output": "Success"},
            {"input": "code = 404", "output": "Client Error"},
            {"input": "code = 500", "output": "Server Error"}
        ],
        "test_cases": [
            {"input": "200", "expected_output": "Success"},
            {"input": "301", "expected_output": "Redirection"},
            {"input": "404", "expected_output": "Client Error"},
            {"input": "500", "expected_output": "Server Error"},
            {"input": "102", "expected_output": "Informational"}
        ],
        "starter_code": "def classify_status_code(code):\n    # Write your code here\n    pass\n\n# Read input\ncode = int(input().strip())\nresult = classify_status_code(code)\nprint(result)"
    },
    {
        "title": "JWT Payload Decoder",
        "description": "Create a function that decodes the payload section of a JWT token.\n\nA JWT has three parts separated by '.'. The payload is the second part, encoded in Base64URL format. Decode it and return the JSON string.",
        "difficulty": "easy",
        "type": "domain",
        "role": "backend",
        "topic": "Authentication",
        "constraints": [
            "JWT format: header.payload.signature",
            "Payload is Base64URL encoded (replace '-' with '+' and '_' with '/')",
            "Add padding '=' as needed before decoding",
            "Return the decoded JSON string"
        ],
        "examples": [
            {"input": "token = 'eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWxpY2UifQ.signature'", "output": '{"user":"alice"}'}
        ],
        "test_cases": [
            {"input": "eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWxpY2UifQ.signature", "expected_output": '{"user":"alice"}'},
            {"input": "eyJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiYWRtaW4ifQ.signature", "expected_output": '{"role":"admin"}'}
        ],
        "starter_code": "import base64\nimport json\n\ndef decode_jwt_payload(token):\n    # Write your code here\n    pass\n\n# Read input\ntoken = input().strip()\nresult = decode_jwt_payload(token)\nprint(result)"
    },
    {
        "title": "Rate Limiter Checker",
        "description": "Create a function that simulates a sliding window rate limiter.\n\nGiven a list of request timestamps (in seconds), a window size (in seconds), and a max request limit, return a list of 'allowed' or 'blocked' for each request.",
        "difficulty": "medium",
        "type": "domain",
        "role": "backend",
        "topic": "API Design",
        "constraints": [
            "Timestamps are in ascending order",
            "Window is the last N seconds from the current request's timestamp",
            "Count includes the current request",
            "If count within window exceeds limit, block the request"
        ],
        "examples": [
            {"input": "timestamps=[1,1,2,3,4], window=2, limit=2", "output": "['allowed', 'allowed', 'blocked', 'allowed', 'allowed']"}
        ],
        "test_cases": [
            {"input": "1 1 2 3 4\n2\n2", "expected_output": "['allowed', 'allowed', 'blocked', 'allowed', 'allowed']"},
            {"input": "1 2 3 4 5\n3\n2", "expected_output": "['allowed', 'allowed', 'blocked', 'blocked', 'blocked']"}
        ],
        "starter_code": "def rate_limiter(timestamps, window, limit):\n    # Write your code here\n    pass\n\n# Read input\ntimestamps = list(map(int, input().split()))\nwindow = int(input().strip())\nlimit = int(input().strip())\nresult = rate_limiter(timestamps, window, limit)\nprint(result)"
    },
    {
        "title": "SQL Query Builder",
        "description": "Create a function that builds a basic SQL SELECT query from given parameters.\n\nThe function accepts a table name, list of columns, and an optional WHERE condition string.",
        "difficulty": "easy",
        "type": "domain",
        "role": "backend",
        "topic": "Databases",
        "constraints": [
            "If columns list is empty, use SELECT *",
            "If where_clause is an empty string, omit the WHERE clause",
            "Columns must be comma-separated with a space after each comma",
            "Query must end with a semicolon"
        ],
        "examples": [
            {"input": "table='users', columns=['id','name'], where='age > 18'", "output": "SELECT id, name FROM users WHERE age > 18;"},
            {"input": "table='products', columns=[], where=''", "output": "SELECT * FROM products;"}
        ],
        "test_cases": [
            {"input": "users\nid name\nage > 18", "expected_output": "SELECT id, name FROM users WHERE age > 18;"},
            {"input": "products\n\n", "expected_output": "SELECT * FROM products;"},
            {"input": "orders\nid total status\n", "expected_output": "SELECT id, total, status FROM orders;"}
        ],
        "starter_code": "def build_select_query(table, columns, where_clause):\n    # Write your code here\n    pass\n\n# Read input\ntable = input().strip()\ncolumns_input = input().strip()\ncolumns = columns_input.split() if columns_input else []\nwhere_clause = input().strip()\nresult = build_select_query(table, columns, where_clause)\nprint(result)"
    },
    {
        "title": "Password Strength Validator",
        "description": "Create a function that validates the strength of a password and returns a strength label.\n\nThe function should check for length, uppercase, lowercase, digits, and special characters.",
        "difficulty": "easy",
        "type": "domain",
        "role": "backend",
        "topic": "Authentication",
        "constraints": [
            "Weak: length < 8",
            "Medium: length >= 8 and meets 2 of the 3 criteria (uppercase, digit, special char)",
            "Strong: length >= 8 and meets all 3 criteria (uppercase, digit, special char)",
            "Special characters: !@#$%^&*()"
        ],
        "examples": [
            {"input": "password = 'abc'", "output": "Weak"},
            {"input": "password = 'Abcdefg1'", "output": "Medium"},
            {"input": "password = 'Abcdef1!'", "output": "Strong"}
        ],
        "test_cases": [
            {"input": "abc", "expected_output": "Weak"},
            {"input": "Abcdefg1", "expected_output": "Medium"},
            {"input": "Abcdef1!", "expected_output": "Strong"},
            {"input": "alllowercase", "expected_output": "Weak"}
        ],
        "starter_code": "def check_password_strength(password):\n    # Write your code here\n    pass\n\n# Read input\npassword = input().strip()\nresult = check_password_strength(password)\nprint(result)"
    },
    {
        "title": "Pagination Metadata Generator",
        "description": "Create a function that computes pagination metadata for an API response.\n\nGiven total items, page number, and page size, return a dictionary with total_pages, current_page, has_next, and has_prev.",
        "difficulty": "easy",
        "type": "domain",
        "role": "backend",
        "topic": "API Design",
        "constraints": [
            "total_pages = ceil(total_items / page_size)",
            "has_next = current_page < total_pages",
            "has_prev = current_page > 1",
            "Page numbers start at 1"
        ],
        "examples": [
            {"input": "total=50, page=2, page_size=10", "output": "{'total_pages': 5, 'current_page': 2, 'has_next': True, 'has_prev': True}"}
        ],
        "test_cases": [
            {"input": "50\n2\n10", "expected_output": "{'total_pages': 5, 'current_page': 2, 'has_next': True, 'has_prev': True}"},
            {"input": "25\n1\n10", "expected_output": "{'total_pages': 3, 'current_page': 1, 'has_next': True, 'has_prev': False}"},
            {"input": "20\n2\n10", "expected_output": "{'total_pages': 2, 'current_page': 2, 'has_next': False, 'has_prev': True}"}
        ],
        "starter_code": "import math\n\ndef pagination_metadata(total_items, page, page_size):\n    # Write your code here\n    pass\n\n# Read input\ntotal_items = int(input().strip())\npage = int(input().strip())\npage_size = int(input().strip())\nresult = pagination_metadata(total_items, page, page_size)\nprint(result)"
    },
    {
        "title": "Request Header Validator",
        "description": "Create a function that validates a set of HTTP request headers for a JSON API.\n\nThe function accepts a dictionary of headers and returns a list of missing or invalid header issues.",
        "difficulty": "medium",
        "type": "domain",
        "role": "backend",
        "topic": "API Design",
        "constraints": [
            "'Content-Type' must be 'application/json'",
            "'Authorization' must start with 'Bearer '",
            "'Accept' must be 'application/json'",
            "Return a sorted list of violated rule strings or ['valid'] if all pass"
        ],
        "examples": [
            {"input": "headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer token123', 'Accept': 'application/json'}", "output": "['valid']"},
            {"input": "headers = {'Content-Type': 'text/html', 'Authorization': 'Basic abc'}", "output": "['Accept missing', 'Authorization must be Bearer token', 'Content-Type must be application/json']"}
        ],
        "test_cases": [
            {"input": "Content-Type application/json\nAuthorization Bearer token123\nAccept application/json", "expected_output": "['valid']"},
            {"input": "Content-Type text/html\nAuthorization Basic abc", "expected_output": "['Accept missing', 'Authorization must be Bearer token', 'Content-Type must be application/json']"}
        ],
        "starter_code": "def validate_headers(headers):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nheaders = {}\nfor line in lines:\n    parts = line.split(' ', 1)\n    if len(parts) == 2:\n        headers[parts[0]] = parts[1]\nresult = validate_headers(headers)\nprint(result)"
    },
    {
        "title": "Database Index Advisor",
        "description": "Create a function that suggests whether a database column should be indexed based on query usage patterns.\n\nGiven a list of query operations on a column, return 'index recommended' or 'index not needed'.",
        "difficulty": "medium",
        "type": "domain",
        "role": "backend",
        "topic": "Databases",
        "constraints": [
            "Operations can be: 'search', 'sort', 'insert', 'update', 'delete'",
            "Recommend index if search or sort operations make up >= 60% of all operations",
            "Return 'index recommended' or 'index not needed'"
        ],
        "examples": [
            {"input": "ops = ['search', 'search', 'search', 'insert', 'update']", "output": "index recommended"},
            {"input": "ops = ['insert', 'update', 'delete', 'insert', 'delete']", "output": "index not needed"}
        ],
        "test_cases": [
            {"input": "search search search insert update", "expected_output": "index recommended"},
            {"input": "insert update delete insert delete", "expected_output": "index not needed"},
            {"input": "search sort insert search delete", "expected_output": "index recommended"}
        ],
        "starter_code": "def advise_index(operations):\n    # Write your code here\n    pass\n\n# Read input\noperations = input().strip().split()\nresult = advise_index(operations)\nprint(result)"
    },
    {
        "title": "Caching Strategy Simulator",
        "description": "Create a function that simulates a simple LRU (Least Recently Used) cache.\n\nGiven a cache capacity and a list of key access operations, return the final state of the cache (most recently used first).",
        "difficulty": "medium",
        "type": "domain",
        "role": "backend",
        "topic": "Caching",
        "constraints": [
            "Cache capacity is fixed",
            "On access, if the key exists, move it to the front (most recent)",
            "If the key does not exist, add it to the front",
            "If at capacity, evict the least recently used (last) item before adding",
            "Return cache state as a list from most to least recently used"
        ],
        "examples": [
            {"input": "capacity=3, accesses=['a','b','c','a','d']", "output": "['d', 'a', 'c']"}
        ],
        "test_cases": [
            {"input": "3\na b c a d", "expected_output": "['d', 'a', 'c']"},
            {"input": "2\nx y x z", "expected_output": "['z', 'x']"}
        ],
        "starter_code": "def lru_cache_state(capacity, accesses):\n    # Write your code here\n    pass\n\n# Read input\ncapacity = int(input().strip())\naccesses = input().strip().split()\nresult = lru_cache_state(capacity, accesses)\nprint(result)"
    },
    {
        "title": "Environment Config Parser",
        "description": "Create a function that parses a .env file content string into a dictionary.\n\nThe function should handle comments, empty lines, and quoted values.",
        "difficulty": "easy",
        "type": "domain",
        "role": "backend",
        "topic": "DevOps & Configuration",
        "constraints": [
            "Lines starting with '#' are comments and must be ignored",
            "Empty lines must be ignored",
            "Values wrapped in double quotes should have the quotes stripped",
            "Keys and values are separated by '='"
        ],
        "examples": [
            {"input": "DB_HOST=localhost\n# comment\nDB_PORT=5432\nAPP_NAME=\"MyApp\"", "output": "{'DB_HOST': 'localhost', 'DB_PORT': '5432', 'APP_NAME': 'MyApp'}"}
        ],
        "test_cases": [
            {"input": "DB_HOST=localhost\n# comment\nDB_PORT=5432\nAPP_NAME=\"MyApp\"", "expected_output": "{'DB_HOST': 'localhost', 'DB_PORT': '5432', 'APP_NAME': 'MyApp'}"},
            {"input": "SECRET_KEY=abc123\n\nDEBUG=\"false\"", "expected_output": "{'SECRET_KEY': 'abc123', 'DEBUG': 'false'}"}
        ],
        "starter_code": "def parse_env_file(content):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\ncontent = sys.stdin.read().strip()\nresult = parse_env_file(content)\nprint(result)"
    },
    {
        "title": "API Response Formatter",
        "description": "Create a function that wraps API data into a standardized response envelope.\n\nSuccessful responses include 'status', 'data', and 'message'. Error responses include 'status', 'error', and 'message'.",
        "difficulty": "easy",
        "type": "domain",
        "role": "backend",
        "topic": "API Design",
        "constraints": [
            "Success format: {'status': 'success', 'data': data, 'message': message}",
            "Error format: {'status': 'error', 'error': error_msg, 'message': message}",
            "The 'type' parameter is either 'success' or 'error'",
            "For error type, 'data' key must not be present"
        ],
        "examples": [
            {"input": "type='success', data={'id': 1}, message='User created'", "output": "{'status': 'success', 'data': {'id': 1}, 'message': 'User created'}"},
            {"input": "type='error', data='Not found', message='Resource missing'", "output": "{'status': 'error', 'error': 'Not found', 'message': 'Resource missing'}"}
        ],
        "test_cases": [
            {"input": "success\nUser created\n{\"id\": 1}", "expected_output": "{'status': 'success', 'data': {'id': 1}, 'message': 'User created'}"},
            {"input": "error\nResource missing\nNot found", "expected_output": "{'status': 'error', 'error': 'Not found', 'message': 'Resource missing'}"}
        ],
        "starter_code": "def format_response(resp_type, message, payload):\n    # Write your code here\n    pass\n\n# Read input\nimport json\nresp_type = input().strip()\nmessage = input().strip()\npayload = input().strip()\ntry:\n    payload = json.loads(payload)\nexcept:\n    pass\nresult = format_response(resp_type, message, payload)\nprint(result)"
    },
    {
        "title": "Webhook Signature Verifier",
        "description": "Create a function that verifies a webhook payload signature using HMAC-SHA256.\n\nGiven a secret key, raw payload string, and received signature (hex), return True if the computed signature matches.",
        "difficulty": "medium",
        "type": "domain",
        "role": "backend",
        "topic": "Authentication",
        "constraints": [
            "Use HMAC-SHA256 for signature computation",
            "The signature is a lowercase hex string",
            "Return True if signatures match, False otherwise",
            "Both key and payload are UTF-8 strings"
        ],
        "examples": [
            {"input": "secret='mysecret', payload='hello', signature=hmac.new('mysecret','hello',sha256).hexdigest()", "output": "True"}
        ],
        "test_cases": [
            {"input": "mysecret\nhello\n88aab3ede8d3adf94d26ab90d3bafd4a2083070c3bcce9c014ee04a443847c0b", "expected_output": "True"},
            {"input": "mysecret\nhello\nwrongsignature", "expected_output": "False"}
        ],
        "starter_code": "import hmac\nimport hashlib\n\ndef verify_webhook_signature(secret, payload, received_signature):\n    # Write your code here\n    pass\n\n# Read input\nsecret = input().strip()\npayload = input().strip()\nreceived_signature = input().strip()\nresult = verify_webhook_signature(secret, payload, received_signature)\nprint(result)"
    },
    {
        "title": "Database Connection Pool Simulator",
        "description": "Create a function that simulates a database connection pool.\n\nGiven a pool size and a list of connection requests and releases (as 'acquire' or 'release'), return the status after each operation: 'ok' if the operation succeeds, or 'pool exhausted' if a request cannot be fulfilled.",
        "difficulty": "medium",
        "type": "domain",
        "role": "backend",
        "topic": "Databases",
        "constraints": [
            "Pool starts fully available",
            "'acquire' decrements available connections; fails if 0 available",
            "'release' increments available connections; cannot exceed pool size",
            "Return a list of statuses for each operation"
        ],
        "examples": [
            {"input": "pool_size=2, ops=['acquire','acquire','acquire','release','acquire']", "output": "['ok', 'ok', 'pool exhausted', 'ok', 'ok']"}
        ],
        "test_cases": [
            {"input": "2\nacquire acquire acquire release acquire", "expected_output": "['ok', 'ok', 'pool exhausted', 'ok', 'ok']"},
            {"input": "3\nacquire acquire release release acquire acquire acquire acquire", "expected_output": "['ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'ok', 'pool exhausted']"}
        ],
        "starter_code": "def simulate_connection_pool(pool_size, operations):\n    # Write your code here\n    pass\n\n# Read input\npool_size = int(input().strip())\noperations = input().strip().split()\nresult = simulate_connection_pool(pool_size, operations)\nprint(result)"
    },
    {
        "title": "Log Level Filter",
        "description": "Create a function that filters log entries by minimum severity level.\n\nGiven a list of log lines in the format '[LEVEL] message' and a minimum level, return only the log lines at or above that level.",
        "difficulty": "easy",
        "type": "domain",
        "role": "backend",
        "topic": "Logging & Monitoring",
        "constraints": [
            "Log levels in order: DEBUG < INFO < WARNING < ERROR < CRITICAL",
            "Filter out any log whose level is below the minimum",
            "Return matching lines preserving original format",
            "Unknown levels should be excluded"
        ],
        "examples": [
            {"input": "logs=['[DEBUG] boot', '[INFO] started', '[ERROR] crash'], min_level='WARNING'", "output": "['[ERROR] crash']"}
        ],
        "test_cases": [
            {"input": "[DEBUG] boot\n[INFO] started\n[ERROR] crash\nWARNING", "expected_output": "['[ERROR] crash']"},
            {"input": "[INFO] ready\n[WARNING] slow\n[CRITICAL] down\nINFO", "expected_output": "['[INFO] ready', '[WARNING] slow', '[CRITICAL] down']"}
        ],
        "starter_code": "def filter_logs(logs, min_level):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nmin_level = lines[-1].strip()\nlogs = lines[:-1]\nresult = filter_logs(logs, min_level)\nprint(result)"
    },
    {
        "title": "Idempotency Key Validator",
        "description": "Create a function that simulates idempotency key tracking for API requests.\n\nGiven a list of (idempotency_key, payload) tuples, return 'processed' for new keys and 'duplicate' for repeated keys, regardless of payload.",
        "difficulty": "easy",
        "type": "domain",
        "role": "backend",
        "topic": "API Design",
        "constraints": [
            "Keys are case-sensitive strings",
            "Same key always returns 'duplicate' after first use",
            "Payload content does not affect duplicate detection",
            "Return a list of statuses in order"
        ],
        "examples": [
            {"input": "requests = [('key1','pay1'),('key2','pay2'),('key1','pay3')]", "output": "['processed', 'processed', 'duplicate']"}
        ],
        "test_cases": [
            {"input": "key1 pay1\nkey2 pay2\nkey1 pay3", "expected_output": "['processed', 'processed', 'duplicate']"},
            {"input": "abc data1\nabc data2\ndef data3\ndef data4", "expected_output": "['processed', 'duplicate', 'processed', 'duplicate']"}
        ],
        "starter_code": "def track_idempotency(requests):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nrequests = [tuple(line.split(' ', 1)) for line in lines]\nresult = track_idempotency(requests)\nprint(result)"
    },
    {
        "title": "CORS Policy Checker",
        "description": "Create a function that validates whether an incoming request origin is allowed by a CORS policy.\n\nGiven an allowed origins list and a request origin, determine if the request should be allowed.",
        "difficulty": "medium",
        "type": "domain",
        "role": "backend",
        "topic": "API Design",
        "constraints": [
            "If allowed_origins contains '*', all origins are permitted",
            "Exact string match is required otherwise",
            "Origin comparison is case-insensitive",
            "Return 'allowed' or 'blocked'"
        ],
        "examples": [
            {"input": "allowed=['https://example.com','https://app.io'], origin='https://app.io'", "output": "allowed"},
            {"input": "allowed=['https://example.com'], origin='https://evil.com'", "output": "blocked"}
        ],
        "test_cases": [
            {"input": "https://example.com https://app.io\nhttps://app.io", "expected_output": "allowed"},
            {"input": "https://example.com\nhttps://evil.com", "expected_output": "blocked"},
            {"input": "*\nhttps://anything.com", "expected_output": "allowed"}
        ],
        "starter_code": "def check_cors(allowed_origins, request_origin):\n    # Write your code here\n    pass\n\n# Read input\nallowed_origins = input().strip().split()\nrequest_origin = input().strip()\nresult = check_cors(allowed_origins, request_origin)\nprint(result)"
    },
    {
        "title": "Database Query Cost Estimator",
        "description": "Create a function that estimates the relative cost of a SQL query based on its clauses.\n\nAssign cost scores to SQL keywords and return the total cost score along with a label.",
        "difficulty": "medium",
        "type": "domain",
        "role": "backend",
        "topic": "Databases",
        "constraints": [
            "Keyword costs: SELECT=1, WHERE=2, JOIN=5, GROUP BY=4, ORDER BY=3, DISTINCT=3, SUBQUERY (nested SELECT)=8",
            "Case-insensitive keyword detection",
            "Total cost < 5: 'cheap', 5-10: 'moderate', > 10: 'expensive'",
            "Count each keyword occurrence separately"
        ],
        "examples": [
            {"input": "query = 'SELECT * FROM users WHERE id = 1'", "output": "cost=3, moderate"},
            {"input": "query = 'SELECT DISTINCT name FROM orders JOIN users ON orders.user_id = users.id GROUP BY name ORDER BY name'", "output": "cost=17, expensive"}
        ],
        "test_cases": [
            {"input": "SELECT * FROM users WHERE id = 1", "expected_output": "cost=3, moderate"},
            {"input": "SELECT name FROM users", "expected_output": "cost=1, cheap"},
            {"input": "SELECT DISTINCT name FROM orders JOIN users ON orders.user_id = users.id GROUP BY name ORDER BY name", "expected_output": "cost=17, expensive"}
        ],
        "starter_code": "def estimate_query_cost(query):\n    # Write your code here\n    pass\n\n# Read input\nquery = input().strip()\nresult = estimate_query_cost(query)\nprint(result)"
    },
    {
        "title": "Retry Logic Simulator",
        "description": "Create a function that simulates an exponential backoff retry mechanism.\n\nGiven a list of operation outcomes ('success' or 'failure') and a base delay, return a list of (attempt, delay_before_attempt) tuples, stopping at the first success or after max retries.",
        "difficulty": "medium",
        "type": "domain",
        "role": "backend",
        "topic": "Distributed Systems",
        "constraints": [
            "First attempt has 0 delay",
            "Delay for attempt n (0-indexed): base_delay * 2^(n-1) for n >= 1",
            "Max retries is 5 (including first attempt)",
            "Stop immediately on 'success'",
            "Return list of (attempt_number, delay) tuples"
        ],
        "examples": [
            {"input": "outcomes=['failure','failure','success'], base_delay=1", "output": "[(1, 0), (2, 1), (3, 2)]"}
        ],
        "test_cases": [
            {"input": "failure failure success\n1", "expected_output": "[(1, 0), (2, 1), (3, 2)]"},
            {"input": "failure failure failure failure failure\n2", "expected_output": "[(1, 0), (2, 2), (3, 4), (4, 8), (5, 16)]"}
        ],
        "starter_code": "def simulate_retry(outcomes, base_delay):\n    # Write your code here\n    pass\n\n# Read input\noutcomes = input().strip().split()\nbase_delay = int(input().strip())\nresult = simulate_retry(outcomes, base_delay)\nprint(result)"
    },
    {
        "title": "Microservice Health Aggregator",
        "description": "Create a function that aggregates health check results from multiple microservices.\n\nGiven a dictionary of service names to their health statuses, return the overall system health.",
        "difficulty": "medium",
        "type": "domain",
        "role": "backend",
        "topic": "Distributed Systems",
        "constraints": [
            "Statuses: 'healthy', 'degraded', 'down'",
            "If all services are healthy: return 'healthy'",
            "If any service is 'down': return 'critical'",
            "If any service is 'degraded' but none is 'down': return 'degraded'",
            "Return a dict: {'overall': status, 'services': original_dict}"
        ],
        "examples": [
            {"input": "services = {'auth': 'healthy', 'db': 'degraded', 'cache': 'healthy'}", "output": "{'overall': 'degraded', 'services': {'auth': 'healthy', 'db': 'degraded', 'cache': 'healthy'}}"}
        ],
        "test_cases": [
            {"input": "auth healthy\ndb degraded\ncache healthy", "expected_output": "{'overall': 'degraded', 'services': {'auth': 'healthy', 'db': 'degraded', 'cache': 'healthy'}}"},
            {"input": "auth healthy\ndb down\ncache healthy", "expected_output": "{'overall': 'critical', 'services': {'auth': 'healthy', 'db': 'down', 'cache': 'healthy'}}"},
            {"input": "auth healthy\ndb healthy", "expected_output": "{'overall': 'healthy', 'services': {'auth': 'healthy', 'db': 'healthy'}}"}
        ],
        "starter_code": "def aggregate_health(services):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nservices = {}\nfor line in lines:\n    parts = line.split()\n    services[parts[0]] = parts[1]\nresult = aggregate_health(services)\nprint(result)"
    },
    {
        "title": "Distributed Lock Simulator",
        "description": "Create a function that simulates a distributed lock (like Redis SETNX) for preventing race conditions.\n\nGiven a sequence of lock operations (lock_name, action, owner), simulate the lock state and return the result of each operation.",
        "difficulty": "hard",
        "type": "domain",
        "role": "backend",
        "topic": "Distributed Systems",
        "constraints": [
            "Actions: 'acquire' or 'release'",
            "'acquire' succeeds only if the lock is not held; returns 'acquired' or 'locked'",
            "'release' succeeds only if the owner matches; returns 'released' or 'unauthorized'",
            "Multiple distinct locks can be tracked simultaneously"
        ],
        "examples": [
            {"input": "ops = [('res1','acquire','alice'),('res1','acquire','bob'),('res1','release','alice'),('res1','acquire','bob')]", "output": "['acquired', 'locked', 'released', 'acquired']"}
        ],
        "test_cases": [
            {"input": "res1 acquire alice\nres1 acquire bob\nres1 release alice\nres1 acquire bob", "expected_output": "['acquired', 'locked', 'released', 'acquired']"},
            {"input": "res1 acquire alice\nres1 release bob\nres1 release alice\nres2 acquire bob", "expected_output": "['acquired', 'unauthorized', 'released', 'acquired']"}
        ],
        "starter_code": "def simulate_distributed_lock(operations):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\noperations = [tuple(line.split()) for line in lines]\nresult = simulate_distributed_lock(operations)\nprint(result)"
    },
    {
        "title": "Event Sourcing Replay",
        "description": "Create a function that rebuilds the current state of an entity by replaying a list of events.\n\nEach event is a tuple of (event_type, payload). Supported events modify a user account state.",
        "difficulty": "hard",
        "type": "domain",
        "role": "backend",
        "topic": "Distributed Systems",
        "constraints": [
            "Start with state: {'name': '', 'email': '', 'active': False, 'balance': 0}",
            "'USER_CREATED' payload: 'name email' — sets name and email, active=True",
            "'BALANCE_UPDATED' payload: integer — sets balance to that value",
            "'ACCOUNT_DEACTIVATED' payload: none — sets active=False",
            "Return the final state dictionary"
        ],
        "examples": [
            {"input": "events = [('USER_CREATED','alice alice@mail.com'),('BALANCE_UPDATED','500'),('ACCOUNT_DEACTIVATED','')]", "output": "{'name': 'alice', 'email': 'alice@mail.com', 'active': False, 'balance': 500}"}
        ],
        "test_cases": [
            {"input": "USER_CREATED alice alice@mail.com\nBALANCE_UPDATED 500\nACCOUNT_DEACTIVATED", "expected_output": "{'name': 'alice', 'email': 'alice@mail.com', 'active': False, 'balance': 500}"},
            {"input": "USER_CREATED bob bob@mail.com\nBALANCE_UPDATED 200\nBALANCE_UPDATED 350", "expected_output": "{'name': 'bob', 'email': 'bob@mail.com', 'active': True, 'balance': 350}"}
        ],
        "starter_code": "def replay_events(events):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nevents = []\nfor line in lines:\n    parts = line.split(' ', 1)\n    event_type = parts[0]\n    payload = parts[1] if len(parts) > 1 else ''\n    events.append((event_type, payload))\nresult = replay_events(events)\nprint(result)"
    },
    {
        "title": "Token Bucket Rate Limiter",
        "description": "Create a function that implements a token bucket rate limiting algorithm.\n\nThe bucket has a max capacity and refills at a given rate (tokens per second). Given a list of (timestamp, tokens_requested) tuples, determine if each request is allowed.",
        "difficulty": "hard",
        "type": "domain",
        "role": "backend",
        "topic": "API Design",
        "constraints": [
            "Bucket starts full at max_capacity",
            "Tokens refill continuously at refill_rate per second based on elapsed time since last request",
            "Bucket cannot exceed max_capacity",
            "A request is 'allowed' if available tokens >= requested; otherwise 'blocked'",
            "Tokens are only consumed for allowed requests"
        ],
        "examples": [
            {"input": "max_capacity=10, refill_rate=2, requests=[(0,3),(1,3),(2,9)]", "output": "['allowed', 'allowed', 'blocked']"}
        ],
        "test_cases": [
            {"input": "10\n2\n0 3\n1 3\n2 9", "expected_output": "['allowed', 'allowed', 'blocked']"},
            {"input": "5\n5\n0 5\n1 5\n2 5", "expected_output": "['allowed', 'allowed', 'allowed']"}
        ],
        "starter_code": "def token_bucket(max_capacity, refill_rate, requests):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nmax_capacity = int(lines[0])\nrefill_rate = int(lines[1])\nrequests = [tuple(map(int, line.split())) for line in lines[2:]]\nresult = token_bucket(max_capacity, refill_rate, requests)\nprint(result)"
    },
    {
        "title": "Circuit Breaker Simulator",
        "description": "Create a function that simulates a circuit breaker pattern used in resilient backend systems.\n\nThe circuit breaker has three states: CLOSED (normal), OPEN (failing, reject all), and HALF-OPEN (testing recovery). Simulate state transitions based on outcomes.",
        "difficulty": "hard",
        "type": "domain",
        "role": "backend",
        "topic": "Distributed Systems",
        "constraints": [
            "Start in CLOSED state",
            "CLOSED: track consecutive failures; after failure_threshold consecutive failures, switch to OPEN",
            "OPEN: reject all requests as 'rejected'; switch to HALF-OPEN after cooldown_period requests",
            "HALF-OPEN: allow one request; if 'success' switch to CLOSED (reset failures); if 'failure' switch back to OPEN",
            "Return list of ('state_at_time_of_request', 'outcome') tuples"
        ],
        "examples": [
            {"input": "failure_threshold=2, cooldown=2, outcomes=['success','failure','failure','success','success','success']", "output": "[('CLOSED','success'),('CLOSED','failure'),('OPEN','rejected'),('OPEN','rejected'),('HALF-OPEN','success'),('CLOSED','success')]"}
        ],
        "test_cases": [
            {"input": "2\n2\nsuccess failure failure success success success", "expected_output": "[('CLOSED', 'success'), ('CLOSED', 'failure'), ('OPEN', 'rejected'), ('OPEN', 'rejected'), ('HALF-OPEN', 'success'), ('CLOSED', 'success')]"},
            {"input": "2\n1\nfailure failure success failure", "expected_output": "[('CLOSED', 'failure'), ('OPEN', 'rejected'), ('HALF-OPEN', 'success'), ('CLOSED', 'failure')]"}
        ],
        "starter_code": "def circuit_breaker(failure_threshold, cooldown, outcomes):\n    # Write your code here\n    pass\n\n# Read input\nfailure_threshold = int(input().strip())\ncooldown = int(input().strip())\noutcomes = input().strip().split()\nresult = circuit_breaker(failure_threshold, cooldown, outcomes)\nprint(result)"
    },
    {
        "title": "GraphQL Query Depth Limiter",
        "description": "Create a function that calculates the nesting depth of a simplified GraphQL query string and determines if it exceeds a maximum allowed depth.\n\nNesting is determined by counting opening and closing braces.",
        "difficulty": "hard",
        "type": "domain",
        "role": "backend",
        "topic": "API Design",
        "constraints": [
            "Count depth by tracking opening '{' and closing '}'",
            "Maximum depth is the highest concurrent nesting level reached",
            "Return a tuple: (max_depth_reached, 'allowed' if <= limit else 'rejected')",
            "Malformed queries (unmatched braces) should return (-1, 'invalid')"
        ],
        "examples": [
            {"input": "query='{ user { posts { comments { text } } } }', limit=3", "output": "(3, 'allowed')"},
            {"input": "query='{ user { posts { comments { likes { count } } } } }', limit=3", "output": "(4, 'rejected')"}
        ],
        "test_cases": [
            {"input": "{ user { posts { comments { text } } } }\n3", "expected_output": "(3, 'allowed')"},
            {"input": "{ user { posts { comments { likes { count } } } } }\n3", "expected_output": "(4, 'rejected')"},
            {"input": "{ user { name }\n3", "expected_output": "(-1, 'invalid')"}
        ],
        "starter_code": "def check_query_depth(query, limit):\n    # Write your code here\n    pass\n\n# Read input\nquery = input().strip()\nlimit = int(input().strip())\nresult = check_query_depth(query, limit)\nprint(result)"
    }
]
    


# Sample Domain Questions (Full Stack)
fullstack_questions = [
    {
        "title": "JWT Token Validator",
        "description": "Create a function that validates a JWT token structure (without actual verification).\n\nCheck if the token has three parts separated by dots and each part is base64-encoded.",
        "difficulty": "medium",
        "type": "domain",
        "role": "fullstack",
        "topic": "Authentication",
        "constraints": [
            "Token must have exactly 3 parts",
            "Parts must be separated by '.'"
        ],
        "examples": [
            {"input": "'eyJhbG.eyJzdWI.SflKxw'", "output": "True"}
        ],
        "test_cases": [
            {"input": "eyJhbG.eyJzdWI.SflKxw", "expected_output": "True"},
            {"input": "invalid.token", "expected_output": "False"}
        ],
        "starter_code": "def validate_jwt_structure(token):\n    # Write your code here\n    parts = token.split('.')\n    return len(parts) == 3\n\n# Read input\ntoken = input().strip()\nresult = validate_jwt_structure(token)\nprint(result)"
    },

    {
        "title": "Mean, Median, Mode Calculator",
        "description": "Create a function that computes the mean, median, and mode of a list of numbers.\n\nReturn all three values as a dictionary. If multiple modes exist, return the smallest one.",
        "difficulty": "easy",
        "type": "domain",
        "role": "datascience",
        "topic": "Statistics",
        "constraints": [
            "List has at least one element",
            "Mean rounded to 2 decimal places",
            "Median is the middle value for odd length, average of two middle for even",
            "If multiple modes, return the smallest"
        ],
        "examples": [
            {"input": "nums = [1, 2, 2, 3, 4]", "output": "{'mean': 2.4, 'median': 2, 'mode': 2}"},
            {"input": "nums = [1, 1, 2, 2, 3]", "output": "{'mean': 1.8, 'median': 2, 'mode': 1}"}
        ],
        "test_cases": [
            {"input": "1 2 2 3 4", "expected_output": "{'mean': 2.4, 'median': 2, 'mode': 2}"},
            {"input": "1 1 2 2 3", "expected_output": "{'mean': 1.8, 'median': 2, 'mode': 1}"},
            {"input": "5 5 5 5", "expected_output": "{'mean': 5.0, 'median': 5.0, 'mode': 5}"}
        ],
        "starter_code": "def descriptive_stats(nums):\n    # Write your code here\n    pass\n\n# Read input\nnums = list(map(float, input().split()))\nresult = descriptive_stats(nums)\nprint(result)"
    },
    {
        "title": "Z-Score Normalizer",
        "description": "Create a function that normalizes a list of numbers using Z-score standardization.\n\nFor each value, compute (x - mean) / std and return the normalized list rounded to 4 decimal places.",
        "difficulty": "easy",
        "type": "domain",
        "role": "datascience",
        "topic": "Data Preprocessing",
        "constraints": [
            "Standard deviation must be population std (divide by N)",
            "If std is 0, return list of all zeros",
            "Round each value to 4 decimal places"
        ],
        "examples": [
            {"input": "nums = [2, 4, 4, 4, 5, 5, 7, 9]", "output": "[-1.5, -0.5, -0.5, -0.5, 0.0, 0.0, 1.0, 2.0]"}
        ],
        "test_cases": [
            {"input": "2 4 4 4 5 5 7 9", "expected_output": "[-1.5, -0.5, -0.5, -0.5, 0.0, 0.0, 1.0, 2.0]"},
            {"input": "10 10 10", "expected_output": "[0.0, 0.0, 0.0]"},
            {"input": "0 5 10", "expected_output": "[-1.2247, 0.0, 1.2247]"}
        ],
        "starter_code": "def z_score_normalize(nums):\n    # Write your code here\n    pass\n\n# Read input\nnums = list(map(float, input().split()))\nresult = z_score_normalize(nums)\nprint(result)"
    },
    {
        "title": "Train-Test Splitter",
        "description": "Create a function that splits a dataset (list of rows) into training and test sets.\n\nGiven a list of items and a split ratio, return the first portion as train and the remainder as test without shuffling.",
        "difficulty": "easy",
        "type": "domain",
        "role": "datascience",
        "topic": "Data Preprocessing",
        "constraints": [
            "Split ratio is a float between 0 and 1 representing the train proportion",
            "Train size = floor(len(data) * ratio)",
            "No shuffling — preserve original order",
            "Return dict: {'train': [...], 'test': [...]}"
        ],
        "examples": [
            {"input": "data=[1,2,3,4,5,6,7,8,9,10], ratio=0.8", "output": "{'train': [1,2,3,4,5,6,7,8], 'test': [9,10]}"}
        ],
        "test_cases": [
            {"input": "1 2 3 4 5 6 7 8 9 10\n0.8", "expected_output": "{'train': [1, 2, 3, 4, 5, 6, 7, 8], 'test': [9, 10]}"},
            {"input": "10 20 30 40 50\n0.6", "expected_output": "{'train': [10, 20, 30], 'test': [40, 50]}"}
        ],
        "starter_code": "import math\n\ndef train_test_split(data, ratio):\n    # Write your code here\n    pass\n\n# Read input\ndata = list(map(int, input().split()))\nratio = float(input().strip())\nresult = train_test_split(data, ratio)\nprint(result)"
    },
    {
        "title": "Min-Max Scaler",
        "description": "Create a function that scales a list of numbers to the range [0, 1] using Min-Max normalization.\n\nFormula: (x - min) / (max - min). If all values are equal, return a list of zeros.",
        "difficulty": "easy",
        "type": "domain",
        "role": "datascience",
        "topic": "Data Preprocessing",
        "constraints": [
            "If max == min, return all zeros",
            "Round each result to 4 decimal places",
            "Output values must be between 0.0 and 1.0 inclusive"
        ],
        "examples": [
            {"input": "nums = [10, 20, 30, 40, 50]", "output": "[0.0, 0.25, 0.5, 0.75, 1.0]"}
        ],
        "test_cases": [
            {"input": "10 20 30 40 50", "expected_output": "[0.0, 0.25, 0.5, 0.75, 1.0]"},
            {"input": "5 5 5", "expected_output": "[0.0, 0.0, 0.0]"},
            {"input": "0 100", "expected_output": "[0.0, 1.0]"}
        ],
        "starter_code": "def min_max_scale(nums):\n    # Write your code here\n    pass\n\n# Read input\nnums = list(map(float, input().split()))\nresult = min_max_scale(nums)\nprint(result)"
    },
    {
        "title": "Confusion Matrix Calculator",
        "description": "Create a function that computes a confusion matrix from actual and predicted binary labels.\n\nReturn a dictionary with TP, FP, TN, FN counts.",
        "difficulty": "easy",
        "type": "domain",
        "role": "datascience",
        "topic": "Model Evaluation",
        "constraints": [
            "Labels are binary: 0 or 1",
            "Positive class is 1",
            "Return dict: {'TP': int, 'FP': int, 'TN': int, 'FN': int}",
            "Both lists are the same length"
        ],
        "examples": [
            {"input": "actual=[1,0,1,1,0,0], predicted=[1,0,0,1,0,1]", "output": "{'TP': 2, 'FP': 1, 'TN': 2, 'FN': 1}"}
        ],
        "test_cases": [
            {"input": "1 0 1 1 0 0\n1 0 0 1 0 1", "expected_output": "{'TP': 2, 'FP': 1, 'TN': 2, 'FN': 1}"},
            {"input": "1 1 0 0\n1 0 1 0", "expected_output": "{'TP': 1, 'FP': 1, 'TN': 1, 'FN': 1}"}
        ],
        "starter_code": "def confusion_matrix(actual, predicted):\n    # Write your code here\n    pass\n\n# Read input\nactual = list(map(int, input().split()))\npredicted = list(map(int, input().split()))\nresult = confusion_matrix(actual, predicted)\nprint(result)"
    },
    {
        "title": "Precision, Recall and F1 Score",
        "description": "Create a function that computes precision, recall, and F1 score from TP, FP, and FN values.\n\nReturn all three as a dictionary rounded to 4 decimal places.",
        "difficulty": "easy",
        "type": "domain",
        "role": "datascience",
        "topic": "Model Evaluation",
        "constraints": [
            "Precision = TP / (TP + FP); 0 if denominator is 0",
            "Recall = TP / (TP + FN); 0 if denominator is 0",
            "F1 = 2 * (precision * recall) / (precision + recall); 0 if denominator is 0",
            "Round to 4 decimal places"
        ],
        "examples": [
            {"input": "TP=2, FP=1, FN=1", "output": "{'precision': 0.6667, 'recall': 0.6667, 'f1': 0.6667}"}
        ],
        "test_cases": [
            {"input": "2\n1\n1", "expected_output": "{'precision': 0.6667, 'recall': 0.6667, 'f1': 0.6667}"},
            {"input": "10\n2\n3", "expected_output": "{'precision': 0.8333, 'recall': 0.7692, 'f1': 0.8}"},
            {"input": "0\n5\n5", "expected_output": "{'precision': 0.0, 'recall': 0.0, 'f1': 0.0}"}
        ],
        "starter_code": "def precision_recall_f1(tp, fp, fn):\n    # Write your code here\n    pass\n\n# Read input\ntp = int(input().strip())\nfp = int(input().strip())\nfn = int(input().strip())\nresult = precision_recall_f1(tp, fp, fn)\nprint(result)"
    },
    {
        "title": "Pearson Correlation Coefficient",
        "description": "Create a function that computes the Pearson correlation coefficient between two numerical lists.\n\nReturn the value rounded to 4 decimal places.",
        "difficulty": "medium",
        "type": "domain",
        "role": "datascience",
        "topic": "Statistics",
        "constraints": [
            "Both lists are the same length",
            "If either list has zero variance, return 0.0",
            "Formula: cov(X,Y) / (std(X) * std(Y))",
            "Use population standard deviation"
        ],
        "examples": [
            {"input": "x=[1,2,3,4,5], y=[2,4,5,4,5]", "output": "0.8321"}
        ],
        "test_cases": [
            {"input": "1 2 3 4 5\n2 4 5 4 5", "expected_output": "0.8321"},
            {"input": "1 2 3\n1 2 3", "expected_output": "1.0"},
            {"input": "1 2 3\n3 2 1", "expected_output": "-1.0"}
        ],
        "starter_code": "def pearson_correlation(x, y):\n    # Write your code here\n    pass\n\n# Read input\nx = list(map(float, input().split()))\ny = list(map(float, input().split()))\nresult = pearson_correlation(x, y)\nprint(result)"
    },
    {
        "title": "Missing Value Imputer",
        "description": "Create a function that imputes missing values in a dataset column.\n\nGiven a list where missing values are represented as None, fill them using the specified strategy.",
        "difficulty": "easy",
        "type": "domain",
        "role": "datascience",
        "topic": "Data Preprocessing",
        "constraints": [
            "Strategies: 'mean', 'median', 'mode'",
            "Compute statistics only from non-None values",
            "Return the filled list with values rounded to 2 decimal places",
            "If all values are None, return list of zeros"
        ],
        "examples": [
            {"input": "data=[1, None, 3, None, 5], strategy='mean'", "output": "[1, 3.0, 3, 3.0, 5]"}
        ],
        "test_cases": [
            {"input": "1 None 3 None 5\nmean", "expected_output": "[1, 3.0, 3, 3.0, 5]"},
            {"input": "2 4 None 4 6\nmedian", "expected_output": "[2, 4, 4.0, 4, 6]"},
            {"input": "1 2 None 2 3\nmode", "expected_output": "[1, 2, 2, 2, 3]"}
        ],
        "starter_code": "def impute_missing(data, strategy):\n    # Write your code here\n    pass\n\n# Read input\nraw = input().split()\ndata = [None if x == 'None' else float(x) for x in raw]\nstrategy = input().strip()\nresult = impute_missing(data, strategy)\nprint(result)"
    },
    {
        "title": "Euclidean Distance Calculator",
        "description": "Create a function that computes the Euclidean distance between two points in N-dimensional space.\n\nThis is the core distance metric used in KNN and K-Means algorithms.",
        "difficulty": "easy",
        "type": "domain",
        "role": "datascience",
        "topic": "Machine Learning Algorithms",
        "constraints": [
            "Both points must have the same number of dimensions",
            "Formula: sqrt(sum((a_i - b_i)^2))",
            "Return rounded to 4 decimal places"
        ],
        "examples": [
            {"input": "a=[1, 2, 3], b=[4, 5, 6]", "output": "5.1962"}
        ],
        "test_cases": [
            {"input": "1 2 3\n4 5 6", "expected_output": "5.1962"},
            {"input": "0 0\n3 4", "expected_output": "5.0"},
            {"input": "1 1 1 1\n2 2 2 2", "expected_output": "2.0"}
        ],
        "starter_code": "import math\n\ndef euclidean_distance(a, b):\n    # Write your code here\n    pass\n\n# Read input\na = list(map(float, input().split()))\nb = list(map(float, input().split()))\nresult = euclidean_distance(a, b)\nprint(result)"
    },
    {
        "title": "Label Encoder",
        "description": "Create a function that encodes categorical labels into integer indices.\n\nAssign indices based on first occurrence order and return both the encoded list and the mapping dictionary.",
        "difficulty": "easy",
        "type": "domain",
        "role": "datascience",
        "topic": "Data Preprocessing",
        "constraints": [
            "Assign integer indices starting from 0 in order of first appearance",
            "Return dict: {'encoded': [int], 'mapping': {label: int}}",
            "Consistent encoding — same label always gets the same integer"
        ],
        "examples": [
            {"input": "labels = ['cat','dog','cat','bird','dog']", "output": "{'encoded': [0, 1, 0, 2, 1], 'mapping': {'cat': 0, 'dog': 1, 'bird': 2}}"}
        ],
        "test_cases": [
            {"input": "cat dog cat bird dog", "expected_output": "{'encoded': [0, 1, 0, 2, 1], 'mapping': {'cat': 0, 'dog': 1, 'bird': 2}}"},
            {"input": "red blue red green blue blue", "expected_output": "{'encoded': [0, 1, 0, 2, 1, 1], 'mapping': {'red': 0, 'blue': 1, 'green': 2}}"}
        ],
        "starter_code": "def label_encode(labels):\n    # Write your code here\n    pass\n\n# Read input\nlabels = input().strip().split()\nresult = label_encode(labels)\nprint(result)"
    },
    {
        "title": "Outlier Detector (IQR Method)",
        "description": "Create a function that detects outliers in a dataset using the Interquartile Range (IQR) method.\n\nReturn the list of values that are outliers.",
        "difficulty": "medium",
        "type": "domain",
        "role": "datascience",
        "topic": "Data Preprocessing",
        "constraints": [
            "Q1 = 25th percentile, Q3 = 75th percentile",
            "IQR = Q3 - Q1",
            "Outlier if value < Q1 - 1.5*IQR or value > Q3 + 1.5*IQR",
            "Use linear interpolation for percentiles",
            "Return sorted list of outlier values"
        ],
        "examples": [
            {"input": "data = [10, 12, 11, 14, 300, 9, 8, 13, 200, 11]", "output": "[200, 300]"}
        ],
        "test_cases": [
            {"input": "10 12 11 14 300 9 8 13 200 11", "expected_output": "[200, 300]"},
            {"input": "1 2 3 4 5 6 7 8 9 10", "expected_output": "[]"},
            {"input": "100 1 2 3 4 5 6 7 8 9 -100", "expected_output": "[-100, 100]"}
        ],
        "starter_code": "def detect_outliers(data):\n    # Write your code here\n    pass\n\n# Read input\ndata = list(map(float, input().split()))\nresult = detect_outliers(data)\nprint(result)"
    },
    {
        "title": "Simple Linear Regression",
        "description": "Create a function that computes the slope and intercept of a simple linear regression line using the least squares method.\n\nReturn the coefficients and predict a given x value.",
        "difficulty": "medium",
        "type": "domain",
        "role": "datascience",
        "topic": "Machine Learning Algorithms",
        "constraints": [
            "Formula: slope = cov(x,y) / var(x), intercept = mean(y) - slope * mean(x)",
            "Use population variance",
            "Round slope, intercept, and prediction to 4 decimal places",
            "Return dict: {'slope': float, 'intercept': float, 'prediction': float}"
        ],
        "examples": [
            {"input": "x=[1,2,3,4,5], y=[2,4,5,4,5], predict_x=6", "output": "{'slope': 0.6, 'intercept': 2.2, 'prediction': 5.8}"}
        ],
        "test_cases": [
            {"input": "1 2 3 4 5\n2 4 5 4 5\n6", "expected_output": "{'slope': 0.6, 'intercept': 2.2, 'prediction': 5.8}"},
            {"input": "1 2 3\n2 4 6\n4", "expected_output": "{'slope': 2.0, 'intercept': 0.0, 'prediction': 8.0}"}
        ],
        "starter_code": "def linear_regression(x, y, predict_x):\n    # Write your code here\n    pass\n\n# Read input\nx = list(map(float, input().split()))\ny = list(map(float, input().split()))\npredict_x = float(input().strip())\nresult = linear_regression(x, y, predict_x)\nprint(result)"
    },
    {
        "title": "KNN Classifier (1D)",
        "description": "Create a function that implements a K-Nearest Neighbors classifier for 1D data.\n\nGiven labeled training points and a query point, return the predicted label using majority vote among the K nearest neighbors.",
        "difficulty": "medium",
        "type": "domain",
        "role": "datascience",
        "topic": "Machine Learning Algorithms",
        "constraints": [
            "Distance metric: absolute difference (1D)",
            "In case of tie in votes, return the label of the closest neighbor",
            "K is always odd to avoid ties in voting",
            "Training data: list of (value, label) tuples"
        ],
        "examples": [
            {"input": "train=[(1,'A'),(2,'A'),(3,'B'),(6,'B'),(7,'B')], k=3, query=4", "output": "B"}
        ],
        "test_cases": [
            {"input": "1 A\n2 A\n3 B\n6 B\n7 B\n3\n4", "expected_output": "B"},
            {"input": "1 A\n2 A\n4 A\n7 B\n8 B\n3\n3", "expected_output": "A"}
        ],
        "starter_code": "def knn_classify(train, k, query):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nk = int(lines[-2])\nquery = float(lines[-1])\ntrain = [(float(l.split()[0]), l.split()[1]) for l in lines[:-2]]\nresult = knn_classify(train, k, query)\nprint(result)"
    },
    {
        "title": "Entropy and Information Gain Calculator",
        "description": "Create a function that calculates the entropy of a label distribution and the information gain of a binary split.\n\nUsed in Decision Tree construction.",
        "difficulty": "medium",
        "type": "domain",
        "role": "datascience",
        "topic": "Machine Learning Algorithms",
        "constraints": [
            "Entropy = -sum(p * log2(p)) for each class probability p",
            "Information Gain = parent entropy - weighted avg of child entropies",
            "Round entropy and information gain to 4 decimal places",
            "Return dict: {'parent_entropy': float, 'information_gain': float}"
        ],
        "examples": [
            {"input": "parent=[1,1,0,0,0], left=[1,1], right=[0,0,0]", "output": "{'parent_entropy': 0.9710, 'information_gain': 0.9710}"}
        ],
        "test_cases": [
            {"input": "1 1 0 0 0\n1 1\n0 0 0", "expected_output": "{'parent_entropy': 0.9710, 'information_gain': 0.9710}"},
            {"input": "1 1 1 0 0 0\n1 1 1\n0 0 0", "expected_output": "{'parent_entropy': 1.0, 'information_gain': 1.0}"}
        ],
        "starter_code": "import math\n\ndef entropy_info_gain(parent, left, right):\n    # Write your code here\n    pass\n\n# Read input\nparent = list(map(int, input().split()))\nleft = list(map(int, input().split()))\nright = list(map(int, input().split()))\nresult = entropy_info_gain(parent, left, right)\nprint(result)"
    },
    {
        "title": "Cosine Similarity Calculator",
        "description": "Create a function that computes the cosine similarity between two vectors.\n\nThis is widely used in NLP for comparing document embeddings.",
        "difficulty": "easy",
        "type": "domain",
        "role": "datascience",
        "topic": "Machine Learning Algorithms",
        "constraints": [
            "Formula: dot(A, B) / (||A|| * ||B||)",
            "If either vector is a zero vector, return 0.0",
            "Round to 4 decimal places"
        ],
        "examples": [
            {"input": "a=[1, 2, 3], b=[4, 5, 6]", "output": "0.9746"}
        ],
        "test_cases": [
            {"input": "1 2 3\n4 5 6", "expected_output": "0.9746"},
            {"input": "1 0 0\n0 1 0", "expected_output": "0.0"},
            {"input": "3 4\n6 8", "expected_output": "1.0"}
        ],
        "starter_code": "import math\n\ndef cosine_similarity(a, b):\n    # Write your code here\n    pass\n\n# Read input\na = list(map(float, input().split()))\nb = list(map(float, input().split()))\nresult = cosine_similarity(a, b)\nprint(result)"
    },
    {
        "title": "Bag of Words Vectorizer",
        "description": "Create a function that converts a list of text documents into a Bag-of-Words matrix.\n\nEach row represents a document, each column a unique word, and each value the word count.",
        "difficulty": "medium",
        "type": "domain",
        "role": "datascience",
        "topic": "NLP",
        "constraints": [
            "Vocabulary is built from all words across all documents",
            "Vocabulary is sorted alphabetically",
            "Words are lowercased and split by spaces",
            "Return dict: {'vocabulary': [str], 'matrix': [[int]]}"
        ],
        "examples": [
            {"input": "docs=['cat sat', 'cat ate rat']", "output": "{'vocabulary': ['ate', 'cat', 'rat', 'sat'], 'matrix': [[0,1,0,1],[1,1,1,0]]}"}
        ],
        "test_cases": [
            {"input": "cat sat\ncat ate rat", "expected_output": "{'vocabulary': ['ate', 'cat', 'rat', 'sat'], 'matrix': [[0, 1, 0, 1], [1, 1, 1, 0]]}"},
            {"input": "hello world\nhello python\nworld python", "expected_output": "{'vocabulary': ['hello', 'python', 'world'], 'matrix': [[1, 0, 1], [1, 1, 0], [0, 1, 1]]}"}
        ],
        "starter_code": "def bag_of_words(docs):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\ndocs = sys.stdin.read().strip().split('\\n')\nresult = bag_of_words(docs)\nprint(result)"
    },
    {
        "title": "TF-IDF Score Calculator",
        "description": "Create a function that computes the TF-IDF score for a specific word in a specific document.\n\nTF-IDF is the core weighting scheme used in document retrieval and NLP.",
        "difficulty": "medium",
        "type": "domain",
        "role": "datascience",
        "topic": "NLP",
        "constraints": [
            "TF = count of word in document / total words in document",
            "IDF = log(total documents / number of documents containing word)",
            "Use natural log (math.log)",
            "TF-IDF = TF * IDF",
            "Round to 4 decimal places"
        ],
        "examples": [
            {"input": "word='cat', doc_index=0, docs=['cat sat on mat', 'dog ate cat', 'bird flew']", "output": "0.1014"}
        ],
        "test_cases": [
            {"input": "cat\n0\ncat sat on mat\ndog ate cat\nbird flew", "expected_output": "0.1014"},
            {"input": "bird\n2\ncat sat on mat\ndog ate cat\nbird flew", "expected_output": "0.2746"}
        ],
        "starter_code": "import math\n\ndef tf_idf(word, doc_index, docs):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nword = lines[0].strip()\ndoc_index = int(lines[1].strip())\ndocs = lines[2:]\nresult = tf_idf(word, doc_index, docs)\nprint(result)"
    },
    {
        "title": "K-Means Iteration Simulator",
        "description": "Create a function that performs one iteration of the K-Means clustering algorithm.\n\nGiven data points and initial centroids, assign each point to the nearest centroid and return the new centroids.",
        "difficulty": "medium",
        "type": "domain",
        "role": "datascience",
        "topic": "Machine Learning Algorithms",
        "constraints": [
            "Use Euclidean distance for 1D points",
            "New centroid = mean of assigned points",
            "If a centroid has no points, keep it unchanged",
            "Return new centroids rounded to 4 decimal places as a list"
        ],
        "examples": [
            {"input": "data=[1,2,3,8,9,10], centroids=[2,9]", "output": "[2.0, 9.0]"}
        ],
        "test_cases": [
            {"input": "1 2 3 8 9 10\n2 9", "expected_output": "[2.0, 9.0]"},
            {"input": "1 2 10 11 20 21\n5 15", "expected_output": "[1.5, 10.5]"}
        ],
        "starter_code": "def kmeans_iteration(data, centroids):\n    # Write your code here\n    pass\n\n# Read input\ndata = list(map(float, input().split()))\ncentroids = list(map(float, input().split()))\nresult = kmeans_iteration(data, centroids)\nprint(result)"
    },
    {
        "title": "ROC AUC Estimator",
        "description": "Create a function that computes the AUC (Area Under the ROC Curve) using the trapezoidal rule.\n\nGiven a list of (threshold, TPR, FPR) tuples sorted by threshold descending, compute the AUC.",
        "difficulty": "medium",
        "type": "domain",
        "role": "datascience",
        "topic": "Model Evaluation",
        "constraints": [
            "Use trapezoidal rule: sum of (FPR[i] - FPR[i-1]) * (TPR[i] + TPR[i-1]) / 2",
            "Points are already sorted",
            "Round AUC to 4 decimal places",
            "AUC should be between 0.0 and 1.0"
        ],
        "examples": [
            {"input": "points=[(1.0,1.0,1.0),(0.5,0.75,0.25),(0.0,0.0,0.0)]", "output": "0.625"}
        ],
        "test_cases": [
            {"input": "1.0 1.0 1.0\n0.5 0.75 0.25\n0.0 0.0 0.0", "expected_output": "0.625"},
            {"input": "1.0 1.0 1.0\n0.0 0.0 0.0", "expected_output": "0.5"}
        ],
        "starter_code": "def compute_auc(points):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\npoints = [tuple(map(float, line.split())) for line in lines]\nresult = compute_auc(points)\nprint(result)"
    },
    {
        "title": "Gradient Descent Step Simulator",
        "description": "Create a function that performs a single gradient descent update step for linear regression.\n\nGiven current weights [w0, w1], a dataset of (x, y) pairs, and a learning rate, return the updated weights after one step.",
        "difficulty": "hard",
        "type": "domain",
        "role": "datascience",
        "topic": "Machine Learning Algorithms",
        "constraints": [
            "Model: y_hat = w0 + w1 * x",
            "Loss: MSE = mean((y_hat - y)^2)",
            "Gradient w.r.t. w0: mean(2 * (y_hat - y))",
            "Gradient w.r.t. w1: mean(2 * (y_hat - y) * x)",
            "Update: w = w - lr * gradient",
            "Round updated weights to 4 decimal places"
        ],
        "examples": [
            {"input": "w0=0, w1=0, lr=0.1, data=[(1,2),(2,4),(3,6)]", "output": "[0.8, 1.8667]"}
        ],
        "test_cases": [
            {"input": "0 0\n0.1\n1 2\n2 4\n3 6", "expected_output": "[0.8, 1.8667]"},
            {"input": "1 1\n0.01\n1 3\n2 5\n3 7", "expected_output": "[1.02, 1.0533]"}
        ],
        "starter_code": "def gradient_descent_step(w0, w1, lr, data):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nw0, w1 = map(float, lines[0].split())\nlr = float(lines[1])\ndata = [tuple(map(float, line.split())) for line in lines[2:]]\nresult = gradient_descent_step(w0, w1, lr, data)\nprint(result)"
    },
    {
        "title": "Naive Bayes Classifier",
        "description": "Create a function that implements a Gaussian Naive Bayes classifier.\n\nGiven labeled training data (1D feature), compute class-wise mean and variance, then predict the class of a new sample.",
        "difficulty": "hard",
        "type": "domain",
        "role": "datascience",
        "topic": "Machine Learning Algorithms",
        "constraints": [
            "Use Gaussian probability density: P(x|class) = (1/sqrt(2*pi*var)) * exp(-(x-mean)^2 / (2*var))",
            "Prior = count(class) / total samples",
            "Posterior ∝ prior * likelihood",
            "Return the class with the highest posterior",
            "Use population variance"
        ],
        "examples": [
            {"input": "train=[(1,'A'),(2,'A'),(5,'B'),(6,'B')], query=3", "output": "A"}
        ],
        "test_cases": [
            {"input": "1 A\n2 A\n5 B\n6 B\n3", "expected_output": "A"},
            {"input": "1 A\n2 A\n3 A\n7 B\n8 B\n9 B\n5", "expected_output": "A"},
            {"input": "1 A\n2 A\n3 A\n7 B\n8 B\n9 B\n6", "expected_output": "B"}
        ],
        "starter_code": "import math\n\ndef naive_bayes(train, query):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nquery = float(lines[-1])\ntrain = [(float(l.split()[0]), l.split()[1]) for l in lines[:-1]]\nresult = naive_bayes(train, query)\nprint(result)"
    },
    {
        "title": "PCA Variance Explainer",
        "description": "Create a function that computes the explained variance ratio for each principal component.\n\nGiven a list of eigenvalues (already computed), return the explained variance ratio list and the number of components needed to explain at least a given threshold of variance.",
        "difficulty": "hard",
        "type": "domain",
        "role": "datascience",
        "topic": "Dimensionality Reduction",
        "constraints": [
            "Explained variance ratio = eigenvalue / sum(eigenvalues)",
            "Components needed = smallest k where cumulative explained variance >= threshold",
            "Round ratios to 4 decimal places",
            "Return dict: {'ratios': [float], 'components_needed': int}"
        ],
        "examples": [
            {"input": "eigenvalues=[4.0, 2.0, 1.0, 0.5, 0.5], threshold=0.9", "output": "{'ratios': [0.5, 0.25, 0.125, 0.0625, 0.0625], 'components_needed': 3}"}
        ],
        "test_cases": [
            {"input": "4.0 2.0 1.0 0.5 0.5\n0.9", "expected_output": "{'ratios': [0.5, 0.25, 0.125, 0.0625, 0.0625], 'components_needed': 3}"},
            {"input": "9.0 1.0\n0.8", "expected_output": "{'ratios': [0.9, 0.1], 'components_needed': 1}"}
        ],
        "starter_code": "def pca_variance(eigenvalues, threshold):\n    # Write your code here\n    pass\n\n# Read input\neigenvalues = list(map(float, input().split()))\nthreshold = float(input().strip())\nresult = pca_variance(eigenvalues, threshold)\nprint(result)"
    },
    {
        "title": "Cross-Validation Score Aggregator",
        "description": "Create a function that simulates K-Fold cross-validation and aggregates results.\n\nGiven a dataset, number of folds, and a scoring function name, split the data into folds, simulate fold scores, and return aggregated statistics.",
        "difficulty": "hard",
        "type": "domain",
        "role": "datascience",
        "topic": "Model Evaluation",
        "constraints": [
            "Split data into K equal folds (last fold may be larger if uneven)",
            "For each fold: test = fold[i], train = remaining folds",
            "Simulate score as: mean(test_fold) / mean(train_fold), rounded to 4 decimal places",
            "Return dict: {'fold_scores': [float], 'mean': float, 'std': float}",
            "Round mean and std to 4 decimal places"
        ],
        "examples": [
            {"input": "data=[10,20,30,40,50,60], k=3", "output": "{'fold_scores': [0.2857, 1.0, 3.5], 'mean': 1.6286, 'std': 1.3484}"}
        ],
        "test_cases": [
            {"input": "10 20 30 40 50 60\n3", "expected_output": "{'fold_scores': [0.2857, 1.0, 3.5], 'mean': 1.6286, 'std': 1.3484}"},
            {"input": "5 10 15 20\n2", "expected_output": "{'fold_scores': [0.4286, 2.3333], 'mean': 1.381, 'std': 0.9524}"}
        ],
        "starter_code": "import math\n\ndef cross_validate(data, k):\n    # Write your code here\n    pass\n\n# Read input\ndata = list(map(float, input().split()))\nk = int(input().strip())\nresult = cross_validate(data, k)\nprint(result)"
    },
    {
        "title": "Anomaly Detection with Z-Score",
        "description": "Create a function that detects anomalies in a time series using a rolling Z-score window.\n\nGiven a list of values, a window size, and a Z-score threshold, return the indices of anomalous points.",
        "difficulty": "hard",
        "type": "domain",
        "role": "datascience",
        "topic": "Statistics",
        "constraints": [
            "For each point i >= window-1, compute Z-score using the previous 'window' values including itself",
            "Z-score = (value - window_mean) / window_std (population std)",
            "If window_std == 0, skip the point (not anomalous)",
            "A point is anomalous if abs(Z-score) > threshold",
            "Return sorted list of 0-indexed positions"
        ],
        "examples": [
            {"input": "data=[10,11,10,12,100,11,10], window=3, threshold=2.0", "output": "[4]"}
        ],
        "test_cases": [
            {"input": "10 11 10 12 100 11 10\n3\n2.0", "expected_output": "[4]"},
            {"input": "1 1 1 1 100 1 1 1 200\n3\n1.5", "expected_output": "[4, 8]"}
        ],
        "starter_code": "def rolling_zscore_anomaly(data, window, threshold):\n    # Write your code here\n    pass\n\n# Read input\ndata = list(map(float, input().split()))\nwindow = int(input().strip())\nthreshold = float(input().strip())\nresult = rolling_zscore_anomaly(data, window, threshold)\nprint(result)"
    },
    {
        "title": "Decision Tree Gini Impurity Calculator",
        "description": "Create a function that computes the Gini impurity of a node split and selects the best threshold for a 1D feature.\n\nGiven a list of (feature_value, label) pairs, find the threshold that minimizes weighted Gini impurity.",
        "difficulty": "hard",
        "type": "domain",
        "role": "datascience",
        "topic": "Machine Learning Algorithms",
        "constraints": [
            "Gini impurity = 1 - sum(p_i^2) for each class proportion p_i",
            "Try all midpoints between consecutive sorted unique feature values as thresholds",
            "Weighted Gini = (n_left/n)*gini_left + (n_right/n)*gini_right",
            "Return dict: {'best_threshold': float, 'best_gini': float}",
            "Round to 4 decimal places; on tie, pick smallest threshold"
        ],
        "examples": [
            {"input": "data=[(2,'A'),(3,'A'),(5,'B'),(7,'B'),(9,'B')]", "output": "{'best_threshold': 4.0, 'best_gini': 0.0}"}
        ],
        "test_cases": [
            {"input": "2 A\n3 A\n5 B\n7 B\n9 B", "expected_output": "{'best_threshold': 4.0, 'best_gini': 0.0}"},
            {"input": "1 A\n2 B\n3 A\n4 B", "expected_output": "{'best_threshold': 1.5, 'best_gini': 0.5}"}
        ],
        "starter_code": "def best_gini_split(data):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\ndata = [(float(l.split()[0]), l.split()[1]) for l in lines]\nresult = best_gini_split(data)\nprint(result)"
    }
]


# Sample Domain Questions (Java)
java_questions = [
    {
        "title": "Java Class Structure",
        "description": "Write a Python function that generates a basic Java class template.\n\nGiven a class name and list of field names, return the Java class code as a string.",
        "difficulty": "easy",
        "type": "domain",
        "role": "java",
        "topic": "OOP",
        "constraints": [
            "Class name should be PascalCase",
            "Fields should be private with String type"
        ],
        "examples": [
            {"input": "class_name='User', fields=['name', 'email']", "output": "public class User { private String name; private String email; }"}
        ],
        "test_cases": [
            {"input": "User\nname,email", "expected_output": "public class User { private String name; private String email; }"}
        ],
        "starter_code": "def generate_java_class(class_name, fields):\n    # Write your code here\n    fields_code = ' '.join([f'private String {f};' for f in fields])\n    return f'public class {class_name} {{ {fields_code} }}'\n\n# Read input\nclass_name = input().strip()\nfields = input().strip().split(',')\nresult = generate_java_class(class_name, fields)\nprint(result)"
    },
    {
        "title": "Java Getter and Setter Generator",
        "description": "Write a Python function that generates Java getter and setter methods for a list of private fields.\n\nEach field is a String type. Return all methods as a single formatted string.",
        "difficulty": "easy",
        "type": "domain",
        "role": "java",
        "topic": "OOP",
        "constraints": [
            "Getter format: 'public String get{Field}() { return {field}; }'",
            "Setter format: 'public void set{Field}(String {field}) { this.{field} = {field}; }'",
            "Field name in method is capitalized (PascalCase for method name)",
            "Methods are separated by a single space"
        ],
        "examples": [
            {"input": "fields = ['name', 'email']", "output": "public String getName() { return name; } public void setName(String name) { this.name = name; } public String getEmail() { return email; } public void setEmail(String email) { this.email = email; }"}
        ],
        "test_cases": [
            {"input": "name,email", "expected_output": "public String getName() { return name; } public void setName(String name) { this.name = name; } public String getEmail() { return email; } public void setEmail(String email) { this.email = email; }"},
            {"input": "age", "expected_output": "public String getAge() { return age; } public void setAge(String age) { this.age = age; }"}
        ],
        "starter_code": "def generate_getters_setters(fields):\n    # Write your code here\n    pass\n\n# Read input\nfields = input().strip().split(',')\nresult = generate_getters_setters(fields)\nprint(result)"
    },
    {
        "title": "Java Interface Generator",
        "description": "Write a Python function that generates a Java interface definition.\n\nGiven an interface name and a list of method signatures (name and return type), return the Java interface code as a string.",
        "difficulty": "easy",
        "type": "domain",
        "role": "java",
        "topic": "OOP",
        "constraints": [
            "Interface format: 'public interface {Name} { {methods} }'",
            "Each method: '{returnType} {methodName}();'",
            "Methods are separated by a single space",
            "No method body in interface"
        ],
        "examples": [
            {"input": "name='Animal', methods=[('void','speak'),('String','getName')]", "output": "public interface Animal { void speak(); String getName(); }"}
        ],
        "test_cases": [
            {"input": "Animal\nvoid,speak\nString,getName", "expected_output": "public interface Animal { void speak(); String getName(); }"},
            {"input": "Repository\nList,findAll\nvoid,save\nboolean,deleteById", "expected_output": "public interface Repository { List findAll(); void save(); boolean deleteById(); }"}
        ],
        "starter_code": "def generate_interface(name, methods):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nname = lines[0].strip()\nmethods = [tuple(line.split(',')) for line in lines[1:]]\nresult = generate_interface(name, methods)\nprint(result)"
    },
    {
        "title": "Java Access Modifier Validator",
        "description": "Write a Python function that validates whether a Java field declaration follows proper encapsulation rules.\n\nA valid field declaration must be private, have a known Java type, and a valid camelCase identifier.",
        "difficulty": "easy",
        "type": "domain",
        "role": "java",
        "topic": "OOP",
        "constraints": [
            "Valid access modifier: 'private' only",
            "Valid types: 'int', 'double', 'boolean', 'String', 'long', 'float', 'char'",
            "Field name must start with a lowercase letter",
            "Return 'valid' or 'invalid'"
        ],
        "examples": [
            {"input": "declaration = 'private String userName'", "output": "valid"},
            {"input": "declaration = 'public int Age'", "output": "invalid"}
        ],
        "test_cases": [
            {"input": "private String userName", "expected_output": "valid"},
            {"input": "public int Age", "expected_output": "invalid"},
            {"input": "private boolean isActive", "expected_output": "valid"},
            {"input": "private Object data", "expected_output": "invalid"}
        ],
        "starter_code": "def validate_field(declaration):\n    # Write your code here\n    pass\n\n# Read input\ndeclaration = input().strip()\nresult = validate_field(declaration)\nprint(result)"
    },
    {
        "title": "Java Constructor Generator",
        "description": "Write a Python function that generates a Java constructor for a class with given fields.\n\nThe constructor should accept all fields as parameters and assign them using 'this.field = field'.",
        "difficulty": "easy",
        "type": "domain",
        "role": "java",
        "topic": "OOP",
        "constraints": [
            "Constructor format: 'public {ClassName}({params}) { {assignments} }'",
            "All fields are of type String",
            "Parameters are comma-separated",
            "Each assignment: 'this.{field} = {field};' separated by spaces"
        ],
        "examples": [
            {"input": "class_name='User', fields=['name','email']", "output": "public User(String name, String email) { this.name = name; this.email = email; }"}
        ],
        "test_cases": [
            {"input": "User\nname,email", "expected_output": "public User(String name, String email) { this.name = name; this.email = email; }"},
            {"input": "Product\ntitle,price,category", "expected_output": "public Product(String title, String price, String category) { this.title = title; this.price = price; this.category = category; }"}
        ],
        "starter_code": "def generate_constructor(class_name, fields):\n    # Write your code here\n    pass\n\n# Read input\nclass_name = input().strip()\nfields = input().strip().split(',')\nresult = generate_constructor(class_name, fields)\nprint(result)"
    },
    {
        "title": "Java Exception Class Generator",
        "description": "Write a Python function that generates a custom Java exception class.\n\nThe exception class should extend RuntimeException and include a constructor that accepts a message.",
        "difficulty": "easy",
        "type": "domain",
        "role": "java",
        "topic": "Exception Handling",
        "constraints": [
            "Class must extend RuntimeException",
            "Constructor calls super(message)",
            "Format: 'public class {Name}Exception extends RuntimeException { public {Name}Exception(String message) { super(message); } }'"
        ],
        "examples": [
            {"input": "name = 'UserNotFound'", "output": "public class UserNotFoundException extends RuntimeException { public UserNotFoundException(String message) { super(message); } }"}
        ],
        "test_cases": [
            {"input": "UserNotFound", "expected_output": "public class UserNotFoundException extends RuntimeException { public UserNotFoundException(String message) { super(message); } }"},
            {"input": "InvalidToken", "expected_output": "public class InvalidTokenException extends RuntimeException { public InvalidTokenException(String message) { super(message); } }"}
        ],
        "starter_code": "def generate_exception_class(name):\n    # Write your code here\n    pass\n\n# Read input\nname = input().strip()\nresult = generate_exception_class(name)\nprint(result)"
    },
    {
        "title": "Java Annotation Parser",
        "description": "Write a Python function that parses Java annotations from a code snippet and returns a list of annotation names with their attributes.\n\nAnnotations start with '@' and may have attributes in parentheses.",
        "difficulty": "medium",
        "type": "domain",
        "role": "java",
        "topic": "Annotations",
        "constraints": [
            "Annotation format: '@Name' or '@Name(key=value)'",
            "Return list of dicts: {'name': str, 'attributes': dict}",
            "Attributes are key=value pairs separated by ','",
            "If no attributes, return empty dict for attributes"
        ],
        "examples": [
            {"input": "code = '@Override\\n@Column(name=email,nullable=false)'", "output": "[{'name': 'Override', 'attributes': {}}, {'name': 'Column', 'attributes': {'name': 'email', 'nullable': 'false'}}]"}
        ],
        "test_cases": [
            {"input": "@Override\n@Column(name=email,nullable=false)", "expected_output": "[{'name': 'Override', 'attributes': {}}, {'name': 'Column', 'attributes': {'name': 'email', 'nullable': 'false'}}]"},
            {"input": "@Entity\n@Table(name=users)\n@Id", "expected_output": "[{'name': 'Entity', 'attributes': {}}, {'name': 'Table', 'attributes': {'name': 'users'}}, {'name': 'Id', 'attributes': {}}]"}
        ],
        "starter_code": "def parse_annotations(code):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\ncode = sys.stdin.read().strip()\nresult = parse_annotations(code)\nprint(result)"
    },
    {
        "title": "Java Method Signature Parser",
        "description": "Write a Python function that parses a Java method signature string and returns its components.\n\nExtract access modifier, return type, method name, and parameter types.",
        "difficulty": "medium",
        "type": "domain",
        "role": "java",
        "topic": "OOP",
        "constraints": [
            "Format: '{modifier} {returnType} {methodName}({type1} {param1}, ...)'",
            "Return dict: {'modifier': str, 'return_type': str, 'name': str, 'params': [type strings]}",
            "If no parameters, return empty list for params",
            "Valid modifiers: public, private, protected"
        ],
        "examples": [
            {"input": "public String getUserById(int id, String token)", "output": "{'modifier': 'public', 'return_type': 'String', 'name': 'getUserById', 'params': ['int', 'String']}"}
        ],
        "test_cases": [
            {"input": "public String getUserById(int id, String token)", "expected_output": "{'modifier': 'public', 'return_type': 'String', 'name': 'getUserById', 'params': ['int', 'String']}"},
            {"input": "private void resetPassword(String email)", "expected_output": "{'modifier': 'private', 'return_type': 'void', 'name': 'resetPassword', 'params': ['String']}"},
            {"input": "protected boolean isValid()", "expected_output": "{'modifier': 'protected', 'return_type': 'boolean', 'name': 'isValid', 'params': []}"}
        ],
        "starter_code": "def parse_method_signature(signature):\n    # Write your code here\n    pass\n\n# Read input\nsignature = input().strip()\nresult = parse_method_signature(signature)\nprint(result)"
    },
    {
        "title": "Java Inheritance Chain Validator",
        "description": "Write a Python function that validates a Java class inheritance chain.\n\nGiven a dictionary of class-to-parent mappings, detect if any circular inheritance exists.",
        "difficulty": "medium",
        "type": "domain",
        "role": "java",
        "topic": "OOP",
        "constraints": [
            "A class with no parent maps to None",
            "Return 'valid' if no circular inheritance, 'circular: {ClassName}' for the first detected cycle",
            "Java does not support multiple inheritance (each class has at most one parent)",
            "Detection order follows input order"
        ],
        "examples": [
            {"input": "hierarchy = {'Dog': 'Animal', 'Animal': 'Object', 'Object': None}", "output": "valid"},
            {"input": "hierarchy = {'A': 'B', 'B': 'C', 'C': 'A'}", "output": "circular: A"}
        ],
        "test_cases": [
            {"input": "Dog Animal\nAnimal Object\nObject None", "expected_output": "valid"},
            {"input": "A B\nB C\nC A", "expected_output": "circular: A"},
            {"input": "Cat Animal\nAnimal None", "expected_output": "valid"}
        ],
        "starter_code": "def validate_inheritance(hierarchy):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nhierarchy = {}\nfor line in lines:\n    parts = line.split()\n    hierarchy[parts[0]] = None if parts[1] == 'None' else parts[1]\nresult = validate_inheritance(hierarchy)\nprint(result)"
    },
    {
        "title": "Java Spring Bean Scope Resolver",
        "description": "Write a Python function that resolves the appropriate Spring bean scope for a given service description.\n\nBased on keywords in the description, return the correct Spring scope annotation.",
        "difficulty": "medium",
        "type": "domain",
        "role": "java",
        "topic": "Spring Framework",
        "constraints": [
            "If description contains 'stateful' or 'user session': return '@Scope(\"session\")'",
            "If description contains 'per request' or 'http request': return '@Scope(\"request\")'",
            "If description contains 'new instance each time' or 'prototype': return '@Scope(\"prototype\")'",
            "Default (singleton): return '@Scope(\"singleton\")'",
            "Check keywords case-insensitively"
        ],
        "examples": [
            {"input": "description = 'Manages user session data and stateful interactions'", "output": "@Scope(\"session\")"},
            {"input": "description = 'A shared configuration service used across the application'", "output": "@Scope(\"singleton\")"}
        ],
        "test_cases": [
            {"input": "Manages user session data and stateful interactions", "expected_output": "@Scope(\"session\")"},
            {"input": "Creates a new instance each time it is requested", "expected_output": "@Scope(\"prototype\")"},
            {"input": "Handles data processing per request lifecycle", "expected_output": "@Scope(\"request\")"},
            {"input": "Global configuration shared across all components", "expected_output": "@Scope(\"singleton\")"}
        ],
        "starter_code": "def resolve_bean_scope(description):\n    # Write your code here\n    pass\n\n# Read input\ndescription = input().strip()\nresult = resolve_bean_scope(description)\nprint(result)"
    },
    {
        "title": "Java Stream Pipeline Simulator",
        "description": "Write a Python function that simulates a Java Stream pipeline on a list of integers.\n\nGiven a list of operations in order, apply them and return the result.",
        "difficulty": "medium",
        "type": "domain",
        "role": "java",
        "topic": "Java Streams",
        "constraints": [
            "Supported operations: 'filter>N' (keep values > N), 'map*N' (multiply each by N), 'sorted' (ascending), 'distinct' (remove duplicates), 'limit:N' (take first N)",
            "Operations are applied in order",
            "Return the final list"
        ],
        "examples": [
            {"input": "data=[5,3,8,1,3,9], ops=['filter>3','map*2','sorted']", "output": "[10, 16, 18]"}
        ],
        "test_cases": [
            {"input": "5 3 8 1 3 9\nfilter>3\nmap*2\nsorted", "expected_output": "[10, 16, 18]"},
            {"input": "1 2 2 3 4 4 5\ndistinct\nfilter>2\nlimit:2", "expected_output": "[3, 4]"}
        ],
        "starter_code": "def stream_pipeline(data, ops):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\ndata = list(map(int, lines[0].split()))\nops = [line.strip() for line in lines[1:]]\nresult = stream_pipeline(data, ops)\nprint(result)"
    },
    {
        "title": "Java Enum Generator",
        "description": "Write a Python function that generates a Java enum definition.\n\nGiven the enum name and a list of constant names with optional integer values, return the Java enum code.",
        "difficulty": "easy",
        "type": "domain",
        "role": "java",
        "topic": "OOP",
        "constraints": [
            "Format: 'public enum {Name} { {CONSTANTS} }'",
            "Constants are comma-separated",
            "If a constant has a value, format as 'CONSTANT(value)'",
            "If no value, just 'CONSTANT'"
        ],
        "examples": [
            {"input": "name='Status', constants=[('ACTIVE','1'),('INACTIVE','0'),('PENDING','')]", "output": "public enum Status { ACTIVE(1), INACTIVE(0), PENDING }"}
        ],
        "test_cases": [
            {"input": "Status\nACTIVE,1\nINACTIVE,0\nPENDING,", "expected_output": "public enum Status { ACTIVE(1), INACTIVE(0), PENDING }"},
            {"input": "Day\nMONDAY,\nTUESDAY,\nWEDNESDAY,", "expected_output": "public enum Day { MONDAY, TUESDAY, WEDNESDAY }"}
        ],
        "starter_code": "def generate_enum(name, constants):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nname = lines[0].strip()\nconstants = [tuple(line.split(',')) for line in lines[1:]]\nresult = generate_enum(name, constants)\nprint(result)"
    },
    {
        "title": "Java JPA Repository Method Namer",
        "description": "Write a Python function that generates a valid Spring Data JPA repository method name from a query description.\n\nConvert a structured query description into the correct derived method name.",
        "difficulty": "medium",
        "type": "domain",
        "role": "java",
        "topic": "Spring Framework",
        "constraints": [
            "Format: 'findBy{Field}' for single field lookup",
            "'findBy{Field1}And{Field2}' for AND conditions",
            "'findBy{Field}OrderBy{SortField}Asc' or 'Desc'",
            "Field names in PascalCase in the method name",
            "Return only the method name string"
        ],
        "examples": [
            {"input": "find by email", "output": "findByEmail"},
            {"input": "find by status and role", "output": "findByStatusAndRole"},
            {"input": "find by department order by salary desc", "output": "findByDepartmentOrderBySalaryDesc"}
        ],
        "test_cases": [
            {"input": "find by email", "expected_output": "findByEmail"},
            {"input": "find by status and role", "expected_output": "findByStatusAndRole"},
            {"input": "find by department order by salary desc", "expected_output": "findByDepartmentOrderBySalaryDesc"},
            {"input": "find by country order by name asc", "expected_output": "findByCountryOrderByNameAsc"}
        ],
        "starter_code": "def generate_jpa_method(description):\n    # Write your code here\n    pass\n\n# Read input\ndescription = input().strip()\nresult = generate_jpa_method(description)\nprint(result)"
    },
    {
        "title": "Java Generics Type Checker",
        "description": "Write a Python function that validates a Java generic type declaration string.\n\nCheck that the generic declaration is correctly structured with proper type bounds.",
        "difficulty": "medium",
        "type": "domain",
        "role": "java",
        "topic": "Generics",
        "constraints": [
            "Valid formats: 'T', 'T extends ClassName', 'T super ClassName'",
            "Type parameter must be a single uppercase letter",
            "ClassName must start with an uppercase letter",
            "Return 'valid' or 'invalid'"
        ],
        "examples": [
            {"input": "T extends Comparable", "output": "valid"},
            {"input": "t extends Number", "output": "invalid"},
            {"input": "T", "output": "valid"},
            {"input": "T extends number", "output": "invalid"}
        ],
        "test_cases": [
            {"input": "T extends Comparable", "expected_output": "valid"},
            {"input": "t extends Number", "expected_output": "invalid"},
            {"input": "T", "expected_output": "valid"},
            {"input": "E super Object", "expected_output": "valid"},
            {"input": "T extends number", "expected_output": "invalid"}
        ],
        "starter_code": "def validate_generic(declaration):\n    # Write your code here\n    pass\n\n# Read input\ndeclaration = input().strip()\nresult = validate_generic(declaration)\nprint(result)"
    },
    {
        "title": "Java Thread Safety Analyzer",
        "description": "Write a Python function that analyzes a simplified Java class description and determines if it is thread-safe.\n\nA class is thread-safe if all its mutable fields are either final, volatile, or accessed only through synchronized methods.",
        "difficulty": "medium",
        "type": "domain",
        "role": "java",
        "topic": "Concurrency",
        "constraints": [
            "Input: list of field descriptors like 'private int count' or 'private final String name' or 'private volatile boolean flag'",
            "And list of method descriptors like 'synchronized void increment()' or 'void reset()'",
            "A mutable non-final, non-volatile field is safe only if ALL methods are synchronized",
            "Return 'thread-safe' or 'not thread-safe'"
        ],
        "examples": [
            {"input": "fields=['private int count'], methods=['synchronized void increment()', 'synchronized int get()']", "output": "thread-safe"},
            {"input": "fields=['private int count'], methods=['synchronized void increment()', 'void get()']", "output": "not thread-safe"}
        ],
        "test_cases": [
            {"input": "FIELDS\nprivate int count\nMETHODS\nsynchronized void increment()\nsynchronized int get()", "expected_output": "thread-safe"},
            {"input": "FIELDS\nprivate int count\nMETHODS\nsynchronized void increment()\nvoid get()", "expected_output": "not thread-safe"},
            {"input": "FIELDS\nprivate final String name\nMETHODS\nvoid print()", "expected_output": "thread-safe"}
        ],
        "starter_code": "def analyze_thread_safety(fields, methods):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nfields_start = lines.index('FIELDS') + 1\nmethods_start = lines.index('METHODS') + 1\nfields = lines[fields_start:lines.index('METHODS')]\nmethods = lines[methods_start:]\nresult = analyze_thread_safety(fields, methods)\nprint(result)"
    },
    {
        "title": "Java Optional Chain Simulator",
        "description": "Write a Python function that simulates Java's Optional chaining behavior.\n\nGiven a chain of operations and an initial value (or None), simulate the Optional pipeline and return the final result.",
        "difficulty": "medium",
        "type": "domain",
        "role": "java",
        "topic": "Java Streams",
        "constraints": [
            "Operations: 'map:{suffix}' appends suffix to string value, 'filter:{value}' keeps value only if it equals the value, 'orElse:{default}' returns default if empty",
            "Start with Optional.of(value) or Optional.empty() if value is 'empty'",
            "Once empty, stays empty unless orElse is used",
            "Return the final string result"
        ],
        "examples": [
            {"input": "value='hello', ops=['map:_world','filter:hello_world','orElse:none']", "output": "hello_world"},
            {"input": "value='empty', ops=['map:_world','orElse:default']", "output": "default"}
        ],
        "test_cases": [
            {"input": "hello\nmap:_world\nfilter:hello_world\norElse:none", "expected_output": "hello_world"},
            {"input": "empty\nmap:_world\norElse:default", "expected_output": "default"},
            {"input": "java\nfilter:python\norElse:not_found", "expected_output": "not_found"}
        ],
        "starter_code": "def simulate_optional(value, ops):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nvalue = lines[0].strip()\nops = lines[1:]\nresult = simulate_optional(value, ops)\nprint(result)"
    },
    {
        "title": "Java Design Pattern Identifier",
        "description": "Write a Python function that identifies which design pattern is being described based on keywords in the description.\n\nReturn the pattern name.",
        "difficulty": "easy",
        "type": "domain",
        "role": "java",
        "topic": "Design Patterns",
        "constraints": [
            "'single instance', 'only one object': Singleton",
            "'create objects', 'factory method', 'subclass decides': Factory",
            "'add behavior', 'wraps object', 'decorator': Decorator",
            "'notify observers', 'event', 'subscribe': Observer",
            "'blueprint', 'copy existing', 'clone': Prototype",
            "Return 'Unknown' if no pattern matches"
        ],
        "examples": [
            {"input": "description = 'Ensures only one instance of the class exists in the system'", "output": "Singleton"},
            {"input": "description = 'Objects subscribe and get notified when an event occurs'", "output": "Observer"}
        ],
        "test_cases": [
            {"input": "Ensures only one instance of the class exists in the system", "expected_output": "Singleton"},
            {"input": "Objects subscribe and get notified when an event occurs", "expected_output": "Observer"},
            {"input": "Wraps an object to add new behavior dynamically", "expected_output": "Decorator"},
            {"input": "Subclass decides which class to instantiate using factory method", "expected_output": "Factory"},
            {"input": "Creates new objects by cloning an existing prototype blueprint", "expected_output": "Prototype"}
        ],
        "starter_code": "def identify_pattern(description):\n    # Write your code here\n    pass\n\n# Read input\ndescription = input().strip()\nresult = identify_pattern(description)\nprint(result)"
    },
    {
        "title": "Java Checked vs Unchecked Exception Classifier",
        "description": "Write a Python function that classifies a list of Java exception class names as 'checked' or 'unchecked'.\n\nReturn a dictionary mapping each exception name to its classification.",
        "difficulty": "easy",
        "type": "domain",
        "role": "java",
        "topic": "Exception Handling",
        "constraints": [
            "Unchecked exceptions extend RuntimeException: NullPointerException, ArrayIndexOutOfBoundsException, IllegalArgumentException, ClassCastException, ArithmeticException, StackOverflowError, OutOfMemoryError",
            "All others are checked exceptions",
            "Return dict: {exception_name: 'checked' or 'unchecked'}"
        ],
        "examples": [
            {"input": "exceptions = ['IOException', 'NullPointerException', 'SQLException']", "output": "{'IOException': 'checked', 'NullPointerException': 'unchecked', 'SQLException': 'checked'}"}
        ],
        "test_cases": [
            {"input": "IOException\nNullPointerException\nSQLException", "expected_output": "{'IOException': 'checked', 'NullPointerException': 'unchecked', 'SQLException': 'checked'}"},
            {"input": "ArithmeticException\nFileNotFoundException\nClassCastException", "expected_output": "{'ArithmeticException': 'unchecked', 'FileNotFoundException': 'checked', 'ClassCastException': 'unchecked'}"}
        ],
        "starter_code": "def classify_exceptions(exceptions):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nexceptions = sys.stdin.read().strip().split('\\n')\nresult = classify_exceptions(exceptions)\nprint(result)"
    },
    {
        "title": "Java Builder Pattern Generator",
        "description": "Write a Python function that generates a Java Builder pattern class for a given class name and list of String fields.\n\nThe builder must have a method for each field and a build() method.",
        "difficulty": "medium",
        "type": "domain",
        "role": "java",
        "topic": "Design Patterns",
        "constraints": [
            "Builder class is a static nested class named 'Builder'",
            "Each field method: 'public Builder {field}(String {field}) { this.{field} = {field}; return this; }'",
            "build() method: 'public {ClassName} build() { return new {ClassName}(this); }'",
            "Format: 'public static class Builder { {methods} {build} }'"
        ],
        "examples": [
            {"input": "class_name='User', fields=['name','email']", "output": "public static class Builder { public Builder name(String name) { this.name = name; return this; } public Builder email(String email) { this.email = email; return this; } public User build() { return new User(this); } }"}
        ],
        "test_cases": [
            {"input": "User\nname,email", "expected_output": "public static class Builder { public Builder name(String name) { this.name = name; return this; } public Builder email(String email) { this.email = email; return this; } public User build() { return new User(this); } }"},
            {"input": "Order\nid,product,quantity", "expected_output": "public static class Builder { public Builder id(String id) { this.id = id; return this; } public Builder product(String product) { this.product = product; return this; } public Builder quantity(String quantity) { this.quantity = quantity; return this; } public Order build() { return new Order(this); } }"}
        ],
        "starter_code": "def generate_builder(class_name, fields):\n    # Write your code here\n    pass\n\n# Read input\nclass_name = input().strip()\nfields = input().strip().split(',')\nresult = generate_builder(class_name, fields)\nprint(result)"
    },
    {
        "title": "Java Memory Model — Stack vs Heap Classifier",
        "description": "Write a Python function that classifies Java variable declarations as stored on the 'stack' or 'heap'.\n\nPrimitive local variables go on the stack; object references and their instances go on the heap.",
        "difficulty": "easy",
        "type": "domain",
        "role": "java",
        "topic": "Java Internals",
        "constraints": [
            "Primitive types: int, double, float, boolean, char, long, short, byte → stack",
            "Reference types (String, any class name starting with uppercase, arrays with []) → heap",
            "Return dict: {variable_name: 'stack' or 'heap'}"
        ],
        "examples": [
            {"input": "declarations = ['int count', 'String name', 'boolean flag', 'User user']", "output": "{'count': 'stack', 'name': 'heap', 'flag': 'stack', 'user': 'heap'}"}
        ],
        "test_cases": [
            {"input": "int count\nString name\nboolean flag\nUser user", "expected_output": "{'count': 'stack', 'name': 'heap', 'flag': 'stack', 'user': 'heap'}"},
            {"input": "double salary\nList items\nchar grade\nint[] scores", "expected_output": "{'salary': 'stack', 'items': 'heap', 'grade': 'stack', 'scores': 'heap'}"}
        ],
        "starter_code": "def classify_memory(declarations):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\ndeclarations = sys.stdin.read().strip().split('\\n')\nresult = classify_memory(declarations)\nprint(result)"
    },
    {
        "title": "Java Deadlock Detector",
        "description": "Write a Python function that detects potential deadlocks in a multi-threaded Java program.\n\nGiven a list of (thread, lock_held, lock_waiting_for) tuples, detect if a circular wait exists.",
        "difficulty": "hard",
        "type": "domain",
        "role": "java",
        "topic": "Concurrency",
        "constraints": [
            "A deadlock exists if there is a cycle in the wait-for graph",
            "Each thread holds one lock and waits for another",
            "Return 'deadlock detected: {thread1} -> ... -> {thread1}' for the cycle, or 'no deadlock'",
            "Report the shortest cycle found"
        ],
        "examples": [
            {"input": "threads=[('T1','L1','L2'),('T2','L2','L1')]", "output": "deadlock detected: T1 -> T2 -> T1"},
            {"input": "threads=[('T1','L1','L2'),('T2','L3','L4')]", "output": "no deadlock"}
        ],
        "test_cases": [
            {"input": "T1 L1 L2\nT2 L2 L1", "expected_output": "deadlock detected: T1 -> T2 -> T1"},
            {"input": "T1 L1 L2\nT2 L3 L4", "expected_output": "no deadlock"},
            {"input": "T1 L1 L2\nT2 L2 L3\nT3 L3 L1", "expected_output": "deadlock detected: T1 -> T2 -> T3 -> T1"}
        ],
        "starter_code": "def detect_deadlock(threads):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nthreads = [tuple(line.split()) for line in lines]\nresult = detect_deadlock(threads)\nprint(result)"
    },
    {
        "title": "Java Garbage Collection Root Tracer",
        "description": "Write a Python function that simulates Java's garbage collection reachability analysis.\n\nGiven a set of GC roots and an object reference graph, determine which objects are reachable and which are eligible for garbage collection.",
        "difficulty": "hard",
        "type": "domain",
        "role": "java",
        "topic": "Java Internals",
        "constraints": [
            "GC roots are always reachable",
            "An object is reachable if it can be reached from any GC root via references",
            "Return dict: {'reachable': sorted list, 'garbage': sorted list}",
            "Unreachable objects are garbage collected"
        ],
        "examples": [
            {"input": "roots=['A'], refs={'A':['B','C'],'B':['D'],'C':[],'D':[],'E':['F'],'F':[]}", "output": "{'reachable': ['A', 'B', 'C', 'D'], 'garbage': ['E', 'F']}"}
        ],
        "test_cases": [
            {"input": "ROOTS\nA\nREFS\nA B C\nB D\nC\nD\nE F\nF", "expected_output": "{'reachable': ['A', 'B', 'C', 'D'], 'garbage': ['E', 'F']}"},
            {"input": "ROOTS\nMain\nREFS\nMain Service Repo\nService Cache\nCache\nRepo\nOrphan", "expected_output": "{'reachable': ['Cache', 'Main', 'Repo', 'Service'], 'garbage': ['Orphan']}"}
        ],
        "starter_code": "def trace_gc_roots(roots, refs):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nroots_start = lines.index('ROOTS') + 1\nrefs_start = lines.index('REFS') + 1\nroots = lines[roots_start:lines.index('REFS')]\nrefs = {}\nfor line in lines[refs_start:]:\n    parts = line.split()\n    refs[parts[0]] = parts[1:] if len(parts) > 1 else []\nresult = trace_gc_roots(roots, refs)\nprint(result)"
    },
    {
        "title": "Java Reflection Method Finder",
        "description": "Write a Python function that simulates Java Reflection by finding methods that match a given filter from a list of method descriptors.\n\nReturn all matching method signatures.",
        "difficulty": "medium",
        "type": "domain",
        "role": "java",
        "topic": "Java Internals",
        "constraints": [
            "Filter fields: 'modifier' (public/private/protected), 'return_type', 'annotation' (optional)",
            "A method matches if ALL provided filter fields match",
            "Return sorted list of matching method name strings",
            "If no filter field provided, return all methods"
        ],
        "examples": [
            {"input": "methods=['public String findById()', 'private void reset()', 'public List findAll()'], filter={'modifier':'public'}", "output": "['findAll', 'findById']"}
        ],
        "test_cases": [
            {"input": "public String findById()\nprivate void reset()\npublic List findAll()\nFILTER\nmodifier public", "expected_output": "['findAll', 'findById']"},
            {"input": "public String getName()\npublic void setName()\nprivate int count()\nFILTER\nmodifier public\nreturn_type void", "expected_output": "['setName']"}
        ],
        "starter_code": "def find_methods(methods, filter_criteria):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nfilter_start = lines.index('FILTER') + 1\nmethods = lines[:lines.index('FILTER')]\nfilter_criteria = {}\nfor line in lines[filter_start:]:\n    k, v = line.split()\n    filter_criteria[k] = v\nresult = find_methods(methods, filter_criteria)\nprint(result)"
    },
    {
        "title": "Java Reactive Stream Backpressure Simulator",
        "description": "Write a Python function that simulates backpressure handling in a reactive Java stream (Project Reactor style).\n\nGiven a producer emission rate, consumer processing rate (items/tick), and buffer size, simulate N ticks and return the count of dropped items.",
        "difficulty": "hard",
        "type": "domain",
        "role": "java",
        "topic": "Reactive Programming",
        "constraints": [
            "Each tick: producer emits 'emission_rate' items into buffer",
            "Consumer then processes min(processing_rate, buffer_size_current) items",
            "Buffer capacity is fixed; items exceeding capacity are dropped",
            "Return total dropped item count after N ticks"
        ],
        "examples": [
            {"input": "emission_rate=5, processing_rate=2, buffer_size=6, ticks=4", "output": "6"}
        ],
        "test_cases": [
            {"input": "5\n2\n6\n4", "expected_output": "6"},
            {"input": "3\n3\n10\n5", "expected_output": "0"},
            {"input": "10\n1\n5\n3", "expected_output": "22"}
        ],
        "starter_code": "def simulate_backpressure(emission_rate, processing_rate, buffer_size, ticks):\n    # Write your code here\n    pass\n\n# Read input\nemission_rate = int(input().strip())\nprocessing_rate = int(input().strip())\nbuffer_size = int(input().strip())\nticks = int(input().strip())\nresult = simulate_backpressure(emission_rate, processing_rate, buffer_size, ticks)\nprint(result)"
    },
    {
        "title": "Java Dependency Injection Container",
        "description": "Write a Python function that simulates a basic Java Dependency Injection container.\n\nGiven bean definitions (name, class, dependencies), resolve the instantiation order using topological sort and return the order beans should be created.",
        "difficulty": "hard",
        "type": "domain",
        "role": "java",
        "topic": "Spring Framework",
        "constraints": [
            "A bean must be created after all its dependencies",
            "Return the valid creation order as a list",
            "If circular dependency exists, return ['circular dependency']",
            "Beans with no dependencies are created first"
        ],
        "examples": [
            {"input": "beans={'userService':['userRepo','emailService'],'userRepo':[],'emailService':[]}", "output": "['emailService', 'userRepo', 'userService']"}
        ],
        "test_cases": [
            {"input": "userService userRepo emailService\nuserRepo\nemailService", "expected_output": "['emailService', 'userRepo', 'userService']"},
            {"input": "A B\nB C\nC A", "expected_output": "['circular dependency']"},
            {"input": "controller service\nservice repository cache\nrepository\ncache", "expected_output": "['cache', 'repository', 'service', 'controller']"}
        ],
        "starter_code": "def resolve_di_container(beans):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nbeans = {}\nfor line in lines:\n    parts = line.split()\n    beans[parts[0]] = parts[1:] if len(parts) > 1 else []\nresult = resolve_di_container(beans)\nprint(result)"
    },
    {
        "title": "Java Bytecode Instruction Estimator",
        "description": "Write a Python function that estimates the number of JVM bytecode instructions for simplified Java expressions.\n\nEach operation type has a known instruction cost; return the total estimated instruction count.",
        "difficulty": "hard",
        "type": "domain",
        "role": "java",
        "topic": "Java Internals",
        "constraints": [
            "Costs: variable_load=1, variable_store=1, int_add=1, int_multiply=3, method_call=5, object_create=7, array_access=2, string_concat=10",
            "Input is a list of operation names",
            "Return total instruction count"
        ],
        "examples": [
            {"input": "ops=['variable_load','int_add','variable_store']", "output": "3"},
            {"input": "ops=['object_create','method_call','string_concat']", "output": "22"}
        ],
        "test_cases": [
            {"input": "variable_load\nint_add\nvariable_store", "expected_output": "3"},
            {"input": "object_create\nmethod_call\nstring_concat", "expected_output": "22"},
            {"input": "variable_load\nint_multiply\narray_access\nmethod_call\nvariable_store", "expected_output": "12"}
        ],
        "starter_code": "def estimate_bytecode(ops):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nops = sys.stdin.read().strip().split('\\n')\nresult = estimate_bytecode(ops)\nprint(result)"
    },
    {
        "title": "Java ClassLoader Hierarchy Resolver",
        "description": "Write a Python function that simulates Java's ClassLoader delegation model.\n\nGiven a list of class loaders with their parent and the classes they can load, resolve which ClassLoader actually loads a requested class.",
        "difficulty": "hard",
        "type": "domain",
        "role": "java",
        "topic": "Java Internals",
        "constraints": [
            "ClassLoader delegation: always delegate to parent first before trying itself",
            "Bootstrap ClassLoader has no parent (parent='none')",
            "If parent can load the class, parent loads it; otherwise try self",
            "Return the name of the ClassLoader that loads the class, or 'ClassNotFoundException'"
        ],
        "examples": [
            {"input": "loaders={'App':{'parent':'Ext','classes':['MyApp']},'Ext':{'parent':'Bootstrap','classes':['javax']},'Bootstrap':{'parent':'none','classes':['java.lang']}}, request='MyApp'", "output": "App"},
            {"input": "same loaders, request='java.lang'", "output": "Bootstrap"}
        ],
        "test_cases": [
            {"input": "Bootstrap none java.lang java.util\nExt Bootstrap javax.xml\nApp Ext MyApp MyService\nREQUEST\nMyApp", "expected_output": "App"},
            {"input": "Bootstrap none java.lang java.util\nExt Bootstrap javax.xml\nApp Ext MyApp MyService\nREQUEST\njava.lang", "expected_output": "Bootstrap"},
            {"input": "Bootstrap none java.lang\nExt Bootstrap javax.xml\nApp Ext MyApp\nREQUEST\nUnknownClass", "expected_output": "ClassNotFoundException"}
        ],
        "starter_code": "def resolve_classloader(loaders, request):\n    # Write your code here\n    pass\n\n# Read input\nimport sys\nlines = sys.stdin.read().strip().split('\\n')\nrequest_idx = lines.index('REQUEST') + 1\nrequest = lines[request_idx].strip()\nloaders = {}\nfor line in lines[:lines.index('REQUEST')]:\n    parts = line.split()\n    loaders[parts[0]] = {'parent': parts[1], 'classes': parts[2:]}\nresult = resolve_classloader(loaders, request)\nprint(result)"
    }
]


async def seed_questions():
    """Seed the database with sample questions"""
    # Clear existing questions
    await db.questions.delete_many({})
    
    # Insert all questions
    all_questions = (
        dsa_questions + 
        frontend_questions + 
        backend_questions + 
        fullstack_questions + 
        java_questions
    )
    
    if all_questions:
        result = await db.questions.insert_many(all_questions)
        print(f"Seeded {len(result.inserted_ids)} questions")
    else:
        print("No questions to seed")

if __name__ == "__main__":
    print("Seeding database...")
    asyncio.run(seed_questions())
    print("Database seeded successfully!")
    client.close()
