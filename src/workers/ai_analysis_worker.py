import time
import json
from database import SessionLocal
from models import Property, Deal
from ai.lead_scoring import score_property
from ai.comps import generate_comps
from ai.offer_calc import calculate_mao
from ai.buyer_match import match_buyers

POLL_INTERVAL = 5  # seconds

def process_property(db, property_obj):
    print(f"[AI] Processing property {property_obj.id}")

    comps = generate_comps(property_obj)
    score = score_property(property_obj, comps)
    mao = calculate_mao(score["arv"], score["repairs"])
    matches = match_buyers(property_obj)

    deal = Deal(
        property_id=property_obj.id,
        arv=score["arv"],
        score=score["score"],
        status="active",
        mao=mao,
    )

    db.add(deal)
    db.commit()

    print(f"[AI] Deal created for property {property_obj.id} with score {score['score']}")

def run_worker():
    print("[AI Worker] Started")
    while True:
        db = SessionLocal()

        unprocessed = (
            db.query(Property)
            .filter(Property.processed == False)
            .all()
        )

        for prop in unprocessed:
            process_property(db, prop)
            prop.processed = True
            db.commit()

        db.close()
        time.sleep(POLL_INTERVAL)

if __name__ == "__main__":
    run_worker()
