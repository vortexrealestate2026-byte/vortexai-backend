from pydantic import BaseModel, EmailStr
from typing import Optional, Dict


class ContractGenerateRequest(BaseModel):
    contract_type: str  # "assignment" | "purchase" | "jv"
    context: Dict
    signer_email: Optional[EmailStr] = None
    signer_name: Optional[str] = None


class ContractGenerateResponse(BaseModel):
    contract_type: str
    html: str
    signer_email: Optional[str] = None
    signer_name: Optional[str] = None
    esign_status: Optional[str] = None
