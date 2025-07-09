from enum import Enum

class UserRole(str, Enum):
    USER = "user"
    WORKER = "worker"
    ADMIN = "admin"
    MODERATOR = "moderator"