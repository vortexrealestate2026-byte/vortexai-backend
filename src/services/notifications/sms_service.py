import os
import requests

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
TWILIO_FROM = os.getenv("TWILIO_FROM")


def send_sms(to: str, message: str):
    """Send an SMS using Twilio or print to console in dev mode."""

    if not TWILIO_SID or not TWILIO_TOKEN or not TWILIO_FROM:
        # Dev mode fallback
        print(f"[SMS] (dev mode) To: {to} | Message: {message}")
        return

    url = f"https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Messages.json"

    payload = {
        "To": to,
        "From": TWILIO_FROM,
        "Body": message,
    }

    try:
        res = requests.post(url, data=payload, auth=(TWILIO_SID, TWILIO_TOKEN))

        if res.status_code >= 200 and res.status_code < 300:
            print(f"[SMS] Sent to {to}")
        else:
            print(f"[SMS] Failed: {res.text}")

    except Exception as e:
        print(f"[SMS] Error sending SMS: {e}")
