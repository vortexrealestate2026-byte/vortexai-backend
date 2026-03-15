def handle_esign_webhook(payload: dict):
    print("[Webhook] eSign event received:", payload)
    # TODO: update contract status in DB

def handle_ingestion_webhook(payload: dict):
    print("[Webhook] Ingestion event:", payload)
    # TODO: trigger ingestion worker or update logs
