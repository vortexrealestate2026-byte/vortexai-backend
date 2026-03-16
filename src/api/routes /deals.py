from ..schemas.deal import DealCreate, DealUpdate
from ..services.ai.comps_agent import generate_comps
from ..services.ai.lead_scoring_agent import score_property
from ..services.ai.offer_calculator import calculate_mao
from ..services.ai.buyer_match_agent import match_buyers

def analyze_property_and_create_deal(db, property_obj):
    comps = db.get_comps(property_obj)
    arv_data = generate_comps(property_obj, comps)
    arv = arv_data.get("arv")

    score_data = score_property(property_obj, arv)
    mao_data = calculate_mao(arv)

    deal = db.create_deal({
        "property_id": property_obj.id,
        "arv": arv,
        "mao": mao_data["mao"],
        "score": score_data["score"]
    })

    buyers = db.get_all_buyers()
    matches = match_buyers(property_obj.dict(), buyers)
    db.update_deal(deal.id, {"buyer_matches": matches})

    return deal
