async def find_investors():

    print("🏘 Searching for property investors")

    investors = [
        {"name": "Investor One", "city": "Atlanta"},
        {"name": "Investor Two", "city": "Dallas"}
    ]

    for investor in investors:
        print("Investor lead:", investor)
