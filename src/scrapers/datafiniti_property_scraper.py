import requests
import os

API_TOKEN = os.getenv("DATAFINITI_TOKEN")

BASE_URL = "https://api.datafiniti.co/v4/properties/search"

def get_properties(city, state, limit=20):

    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "query": f"city:{city} AND province:{state}",
        "num_records": limit
    }

    response = requests.post(BASE_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json().get("records", [])

    return []
