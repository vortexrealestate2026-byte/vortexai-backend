from enum import Enum


class ContractType(str, Enum):
    assignment = "assignment"
    purchase = "purchase"
    jv = "jv"


class DealStatus(str, Enum):
    active = "active"
    expired = "expired"
    sold = "sold"


class UserRole(str, Enum):
    admin = "admin"
    buyer = "buyer"
    wholesaler = "wholesaler"
