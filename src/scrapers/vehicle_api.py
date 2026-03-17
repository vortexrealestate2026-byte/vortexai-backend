import requests

def get_vehicles():

    url = "https://api.api-ninjas.com/v1/cars?limit=10"

    headers = {
        "X-Api-Key": "YOUR_KEY"
    }

    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        return r.json()

    return []
