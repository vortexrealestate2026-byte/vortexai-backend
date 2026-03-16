async def send_investor_alert(property_data, score):

    if score > 80:

        print("📩 Sending investor alert")
        print(property_data)
