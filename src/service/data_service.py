from app.database import SessionLocal
from app.models import Property, Vehicle


def save_property(city, address, price, source):

    db = SessionLocal()

    property_data = Property(
        city=city,
        address=address,
        price=price,
        source=source
    )

    db.add(property_data)
    db.commit()
    db.close()


def save_vehicle(city, make, model, price, source):

    db = SessionLocal()

    vehicle_data = Vehicle(
        city=city,
        make=make,
        model=model,
        price=price,
        source=source
    )

    db.add(vehicle_data)
    db.commit()
    db.close()
