# from pydantic import BaseModel, Field, EmailStr, ConfigDict
# from typing import Optional, List, Dict, Any
# from datetime import datetime, timezone
# from enum import Enum

# class Role(str, Enum):
#     FRONTEND = "frontend"
#     BACKEND = "backend"
#     FULLSTACK = "fullstack"
#     JAVA = "java"

# class Experience(str, Enum):
#     BEGINNER = "beginner"
#     INTERMEDIATE = "intermediate"
#     PLACEMENT_READY = "placement_ready"

# class TargetCompany(str, Enum):
#     SERVICE = "service"
#     PRODUCT = "product"
#     BOTH = "both"

# class DailyTime(int, Enum):
#     THIRTY = 30
#     SIXTY = 60
#     NINETY = 90

# class Difficulty(str, Enum):
#     EASY = "easy"
#     MEDIUM = "medium"
#     HARD = "hard"

# class QuestionType(str, Enum):
#     DSA = "dsa"
#     DOMAIN = "domain"

# # Request/Response Models
# class SignupRequest(BaseModel):
#     email: EmailStr
#     password: str = Field(..., min_length=6)
#     name: str = Field(..., min_length=2)

# class LoginRequest(BaseModel):
#     email: EmailStr
#     password: str

# class OnboardingRequest(BaseModel):
#     role: Role
#     username : str
#     focus_area: str
#     experience: Experience
#     target_companies: TargetCompany
#     daily_time: DailyTime
#     prep_duration: int = Field(..., ge=15, le=90)

# class CodeSubmissionRequest(BaseModel):
#     question_id: str
#     code: str
#     language: str = "python"

# class AuthResponse(BaseModel):
#     access_token: str
#     token_type: str = "bearer"
#     user: Dict[str, Any]

# class UserResponse(BaseModel):
#     model_config = ConfigDict(extra="ignore")
#     id: str
#     email: str
#     name: str
#     role: Optional[str] = None
#     experience: Optional[str] = None
#     current_streak: int = 0
#     longest_streak: int = 0
#     onboarded: bool = False

# # Database Models
# class User(BaseModel):
#     model_config = ConfigDict(extra="ignore")
#     email: EmailStr
#     password_hash: str
#     name: str
#     role: Optional[Role] = None
#     experience: Optional[Experience] = None
#     target_companies: Optional[TargetCompany] = None
#     daily_time: Optional[DailyTime] = None
#     prep_duration: Optional[int] = None
#     current_streak: int = 0
#     longest_streak: int = 0
#     total_tasks_completed: int = 0
#     total_dsa_solved: int = 0
#     total_domain_solved: int = 0
#     onboarded: bool = False
#     created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
#     last_active: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

# class Question(BaseModel):
#     model_config = ConfigDict(extra="ignore")
#     title: str
#     description: str
#     difficulty: Difficulty
#     type: QuestionType
#     role: Optional[Role] = None
#     topic: str
#     constraints: List[str] = []
#     examples: List[Dict[str, str]] = []
#     test_cases: List[Dict[str, Any]] = []
#     starter_code: str = ""
#     created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

# class DailyTask(BaseModel):
#     model_config = ConfigDict(extra="ignore")
#     user_id: str
#     date: str
#     dsa_question_id: str
#     domain_question_id: str
#     dsa_completed: bool = False
#     domain_completed: bool = False
#     dsa_completed_at: Optional[datetime] = None
#     domain_completed_at: Optional[datetime] = None
#     created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

# class Submission(BaseModel):
#     model_config = ConfigDict(extra="ignore")
#     user_id: str
#     question_id: str
#     code: str
#     language: str = "python"
#     status: str
#     test_results: List[Dict[str, Any]] = []
#     passed: int = 0
#     total: int = 0
#     execution_time: Optional[float] = None
#     created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

# class TaskResponse(BaseModel):
#     dsa_task: Dict[str, Any]
#     domain_task: Dict[str, Any]
#     date: str
#     dsa_completed: bool
#     domain_completed: bool

# class ProgressResponse(BaseModel):
#     total_days: int
#     days_completed: int
#     tasks_completed: int
#     dsa_solved: int
#     domain_solved: int
#     current_streak: int
#     longest_streak: int
#     accuracy: float
#     readiness_score: int

# class LeaderboardEntry(BaseModel):
#     rank: int
#     name: str
#     current_streak: int
#     tasks_completed: int
#     points: int             
#     is_current_user: bool



from pydantic import BaseModel, Field, EmailStr, ConfigDict
from typing import Optional, List, Dict, Any
from datetime import datetime, timezone
from enum import Enum

class Role(str, Enum):
    FRONTEND = "frontend"
    BACKEND = "backend"
    FULLSTACK = "fullstack"
    JAVA = "java"

class Experience(str, Enum):
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    PLACEMENT_READY = "placement_ready"

class TargetCompany(str, Enum):
    SERVICE = "service"
    PRODUCT = "product"
    BOTH = "both"

class DailyTime(int, Enum):
    THIRTY = 30
    SIXTY = 60
    NINETY = 90

class Difficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"

class QuestionType(str, Enum):
    DSA = "dsa"
    DOMAIN = "domain"

# Request/Response Models
class SignupRequest(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=6)
    name: str = Field(..., min_length=2)

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class OnboardingRequest(BaseModel):
    role: Role
    username: str
    focus_area: str
    experience: Experience
    target_companies: TargetCompany
    daily_time: DailyTime
    prep_duration: int = Field(..., ge=15, le=90)

class CodeSubmissionRequest(BaseModel):
    question_id: str
    code: str
    language: str = "python"

class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: Dict[str, Any]

class UserResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: str
    email: str
    name: str
    role: Optional[str] = None
    experience: Optional[str] = None
    current_streak: int = 0
    longest_streak: int = 0
    total_tasks_completed: int = 0
    points: int = 0
    onboarded: bool = False

# Database Models
class User(BaseModel):
    model_config = ConfigDict(extra="ignore")
    email: EmailStr
    password_hash: str
    name: str
    role: Optional[Role] = None
    experience: Optional[Experience] = None
    target_companies: Optional[TargetCompany] = None
    daily_time: Optional[DailyTime] = None
    prep_duration: Optional[int] = None
    current_streak: int = 0
    longest_streak: int = 0
    total_tasks_completed: int = 0
    total_dsa_solved: int = 0
    total_domain_solved: int = 0
    points: int = 0          # FIX: added points field
    onboarded: bool = False
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    last_active: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Question(BaseModel):
    model_config = ConfigDict(extra="ignore")
    title: str
    description: str
    difficulty: Difficulty
    type: QuestionType
    role: Optional[Role] = None
    topic: str
    constraints: List[str] = []
    examples: List[Dict[str, str]] = []
    test_cases: List[Dict[str, Any]] = []
    starter_code: str = ""
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class DailyTask(BaseModel):
    model_config = ConfigDict(extra="ignore")
    user_id: str
    date: str
    dsa_question_id: str
    domain_question_id: str
    dsa_completed: bool = False
    domain_completed: bool = False
    dsa_completed_at: Optional[datetime] = None
    domain_completed_at: Optional[datetime] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Submission(BaseModel):
    model_config = ConfigDict(extra="ignore")
    user_id: str
    question_id: str
    code: str
    language: str = "python"
    status: str = "attempted"
    all_passed: bool = False      # FIX: added all_passed for accurate tracking
    test_results: List[Dict[str, Any]] = []
    passed: int = 0
    total: int = 0
    execution_time: Optional[float] = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class TaskResponse(BaseModel):
    dsa_task: Dict[str, Any]
    domain_task: Dict[str, Any]
    date: str
    dsa_completed: bool
    domain_completed: bool

class ProgressResponse(BaseModel):
    total_days: int
    days_completed: int
    tasks_completed: int
    dsa_solved: int
    domain_solved: int
    current_streak: int
    longest_streak: int
    accuracy: float
    readiness_score: int
    rank: int = 0        # FIX: added rank
    points: int = 0      # FIX: added points

class LeaderboardEntry(BaseModel):
    rank: int
    name: str
    current_streak: int
    tasks_completed: int
    points: int
    is_current_user: bool