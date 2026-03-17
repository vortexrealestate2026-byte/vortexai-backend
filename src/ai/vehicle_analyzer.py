import logging

logger = logging.getLogger("vortex-ai")


def analyze_vehicle(vehicle):

    price = vehicle.get("price", 0)
    year = vehicle.get("year", 2020)
    mileage = vehicle.get("mileage", 0)

    score = 0

    # Cheap car
    if price < 15000:
        score += 3

    # Low mileage
    if mileage < 80000:
        score += 3

    # Newer vehicle
    if year > 2018:
        score += 2

    return {
        "price": price,
        "year": year,
        "mileage": mileage,
        "deal_score": score
    }
