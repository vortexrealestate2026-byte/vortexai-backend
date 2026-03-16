import time
from database import SessionLocal
from models import Property, IngestionLog
from ingestion.sources import fetch_zillow, fetch_realtor, fetch_craigslist
from ingestion.normalize import normalize_listing

POLL_INTERVAL = 10  # seconds

def ingest_source(db, source_name, fetch_fn):
    print(f"[Ingestion] Fetching from {source_name}")

    listings = fetch_fn()
    for raw in listings:
        normalized = normalize_listing(raw)

        exists = (
            db.query(Property)
            .filter(Property.address == normalized["address"])
            .first()
        )

        if exists:
            continue

        prop = Property(**normalized)
        db.add(prop)

        log = IngestionLog(
            source=source_name,
            raw_payload=raw,
            processed=True
        )
        db.add(log)

    db.commit()
    print(f"[Ingestion] Completed {source_name}")

def run_worker():
    print("[Ingestion Worker] Started")
    while True:
        db = SessionLocal()

        ingest_source(db, "zillow", fetch_zillow)
        ingest_source(db, "realtor", fetch_realtor)
        ingest_source(db, "craigslist", fetch_craigslist)

        db.close()
        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    run_worker()
