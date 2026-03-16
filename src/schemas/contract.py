from pydantic import BaseModel, EmailStr


class ContractRequest(BaseModel):
    contract_type: str  # "assignment" | "purchase" | "jv"
    context: dict
    signer_email: EmailStr | None = None
    signer_name: str | None = None


class ContractResponse(BaseModel):
    html: str
    contract_type: str
    signer_email: str | None = None
    signer_name: str | None = None
    esign_status: str | None = None
