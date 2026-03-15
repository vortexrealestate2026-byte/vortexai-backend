def calculate_mao(arv: int | None, repairs: int = 20000, assignment_fee: int = 10000) -> dict:
    """
    MAO = ARV * 0.70 - repairs - assignment fee
    """

    if not arv:
        return {"mao": None, "formula": "N/A"}

    mao = arv * 0.70 - repairs - assignment_fee

    return {
        "mao": round(mao),
        "formula": f"MAO = {arv} * 0.70 - {repairs} - {assignment_fee}"
    }
