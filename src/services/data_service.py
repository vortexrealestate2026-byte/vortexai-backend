from database import SessionLocal
from models import Property, Vehicle


def save_property(city, address, price, source):

    db = SessionLocal()

    item = Property(
        city=city,
        address=address,
        price=price,
        source=source
    )

    db.add(item)
    db.commit()
    db.close()


def save_vehicle(city, make, model, price, source):

    db = SessionLocal()

    item = Vehicle(
        city=city,
        make=make,
        model=model,
        price=price,
        source=source
    )

    db.add(item)
    db.commit()
    db.close()
