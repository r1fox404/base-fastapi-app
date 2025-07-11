from enum import Enum


class UserRoleType(str, Enum):
    USER = "USER"
    ADMIN = "ADMIN"
    WORKER = "WORKER"
    MODERATOR = "MODERATOR"


class UserStateType(str, Enum):
    BLOCKED = "BLOCKED"
    REGISTERED = "REGISTERED"
    ORDER_PROCESSING = "ORDER_PROCESSING"


class EventStateType(str, Enum):
    SOLD_OUT = "SOLD_OUT"
    COMPLETED = "COMPLETED"
    REGISTRATION = "REGISTRATION"


class ContractStateType(str, Enum):
    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    INSPECTED = "INSPECTED"


class ContractRejectType(str, Enum):
    USER = "BY_USER"
    ADMIN = "BY_ADMIN"
    SYSTEM = "BY_SYSTEM"