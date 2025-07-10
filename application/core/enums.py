from enum import Enum


class UserRole(str, Enum):
    USER = "USER"
    WORKER = "WORKER"
    ADMIN = "ADMIN"
    MODERATOR = "MODERATOR"


class UserStates(str, Enum):
    BLOCKED = "BLOCKED"
    REGISTERED = "REGISTERED"
    ORDER_PROCESSING = "ORDER_PROCESSING"