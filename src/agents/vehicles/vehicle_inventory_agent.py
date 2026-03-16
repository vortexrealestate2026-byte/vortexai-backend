import random


async def run_vehicle_inventory():

    print("🚗 Vehicle scanner running")

    vehicles = []

    for i in range(5):

        vehicle = {
            "make": "Toyota",
            "model": "Camry",
            "price": random.randint(15000, 30000)
        }

        vehicles.append(vehicle)

    print("🚗 Vehicles found:", vehicles)

    return vehicles
