from typing import List, Dict


def generate_comps(property_data: dict, comps: List[dict]) -> Dict:
    """
    Computes ARV using simple weighted average of comps.
    """

    if not comps:
        return {"arv": None, "comps_used": []}

    prices = [c["price"] for c in comps if c.get("price")]
    if not prices:
        return {"arv": None, "comps_used": []}

    avg_price = sum(prices) / len(prices)

    return {
        "arv": round(avg_price),
        "comps_used": comps
    }
