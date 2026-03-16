from datetime import datetime


def generate_financing_application(customer_name, vehicle):

    price = vehicle["price"]

    down_payment = int(price * 0.10)
    loan_amount = price - down_payment

    application = {
        "customer_name": customer_name,
        "vehicle_make": vehicle["make"],
        "vehicle_model": vehicle["model"],
        "price": price,
        "down_payment": down_payment,
        "loan_amount": loan_amount,
        "status": "pending",
        "created_at": datetime.utcnow()
    }

    print("🚗 Financing Application Created:", application)

    return application
