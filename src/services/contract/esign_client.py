import os
import requests

ESIGN_API_URL = os.getenv("ESIGN_API_URL", "https://api.esign-provider.com")
ESIGN_API_KEY = os.getenv("ESIGN_API_KEY", "")


def send_for_signature(
    signer_email: str,
    signer_name: str,
    html_document: str,
    subject: str = "Please sign your document",
):
    """
    Generic e-sign client placeholder.
    In production, adapt this to DocuSign, HelloSign, etc.
    """
    if not ESIGN_API_KEY:
        print("[eSign] No API key configured, dev mode only.")
        print(f"[eSign] Would send to {signer_email} | Subject: {subject}")
        return {"status": "dev_mode", "signer_email": signer_email}

    payload = {
        "signer_email": signer_email,
        "signer_name": signer_name,
        "subject": subject,
        "document_html": html_document,
    }

    headers = {
        "Authorization": f"Bearer {ESIGN_API_KEY}",
        "Content-Type": "application/json",
    }

    try:
        res = requests.post(f"{ESIGN_API_URL}/envelopes", json=payload, headers=headers)
        if 200 <= res.status_code < 300:
            print(f"[eSign] Envelope created for {signer_email}")
            return res.json()
        else:
            print(f"[eSign] Failed: {res.status_code} {res.text}")
            return {"error": res.text, "status_code": res.status_code}
    except Exception as e:
        print(f"[eSign] Error: {e}")
        return {"error": str(e)}
