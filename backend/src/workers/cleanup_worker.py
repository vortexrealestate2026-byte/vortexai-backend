import time
from datetime import datetime, timedelta
from database import SessionLocal
from models import IngestionLog, Deal

POLL_INTERVAL = 60  # run every minute

def cleanup_logs(db):
    cutoff = datetime.utcnow() - timedelta(days=7)
    deleted = (
        db.query(IngestionLog)
        .filter(IngestionLog.created_at < cutoff)
        .delete()
    )
    db.commit()
    if deleted:
        print(f"[Cleanup] Deleted {deleted} old ingestion logs")

def cleanup_expired_deals(db):
    cutoff = datetime.utcnow() - timedelta(days=30)
    expired = (
        db.query(Deal)
        .filter(Deal.created_at < cutoff)
        .filter(Deal.status == "active")
        .all()
    )

    for deal in expired:
        deal.status = "expired"

    db.commit()
    if expired:
        print(f"[Cleanup] Marked {len(expired)} deals as expired")

def run_worker():
    print("[Cleanup Worker] Started")
    while True:
        db = SessionLocal()

        cleanup_logs(db)
        cleanup_expired_deals(db)

        db.close()
        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    run_worker()
