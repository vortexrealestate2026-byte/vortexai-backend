def score_property(property_data: dict, arv: int | None) -> dict:
    """
    Basic lead scoring model.
    Score is based on spread, condition keywords, and price-to-ARV ratio.
    """

    price = property_data.get("price", 0)
    description = property_data.get("description", "").lower()

    distress_keywords = ["as-is", "needs work", "fixer", "handyman", "motivated"]
    distress_hits = sum(1 for k in distress_keywords if k in description)

    if arv:
        spread = arv - price
        ratio = price / arv
    else:
        spread = 0
        ratio = 1

    score = 0

    # Spread scoring
    if spread > 50000:
        score += 40
    elif spread > 30000:
        score += 25
    elif spread > 15000:
        score += 10

    # Ratio scoring
    if ratio < 0.65:
        score += 40
    elif ratio < 0.75:
        score += 25
    elif ratio < 0.85:
        score += 10

    # Distress scoring
    score += distress_hits * 5

    return {
        "score": min(score, 100),
        "spread": spread,
        "distress_hits": distress_hits
    }
