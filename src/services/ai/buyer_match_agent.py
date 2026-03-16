from typing import List, Dict
from .text_utils import normalize_text


def match_buyers(property_data: dict, buyers: List[dict]) -> List[Dict]:
    """
    Simple buyer matching engine using keyword + criteria similarity.
    """

    prop_str = normalize_text(
        f"{property_data.get('address', '')} "
        f"{property_data.get('description', '')} "
        f"{property_data.get('beds', '')}bd "
        f"{property_data.get('baths', '')}ba "
        f"{property_data.get('price', '')}"
    )

    matches = []

    for buyer in buyers:
        criteria = " ".join(buyer.get("criteria", []))
        criteria_norm = normalize_text(criteria)

        score = 0
        for word in criteria_norm.split():
            if word in prop_str:
                score += 1

        matches.append({
            "buyer_id": buyer["id"],
            "buyer_name": buyer["name"],
            "match_score": score,
            "reason": f"{score} keyword matches"
        })

    matches.sort(key=lambda x: x["match_score"], reverse=True)
    return matches
