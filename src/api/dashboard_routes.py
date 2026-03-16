from fastapi import APIRouter

router = APIRouter()


@router.get("/metrics")
def get_metrics():

    return {
        "active_agents": 50,
        "properties_scanned": 124,
        "vehicles_scanned": 83,
        "loan_applications": 12,
        "deals_found": 3
    }
