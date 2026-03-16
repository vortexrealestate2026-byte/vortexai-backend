from src.agents.finance.loan_agent import generate_financing_application
from src.agents.finance.bank_submission import submit_to_bank


async def run_finance_agents():

    print("💰 Running Finance Agents")

    vehicle = {
        "make": "Toyota",
        "model": "Camry",
        "price": 24000
    }

    customer = "John Doe"

    application = generate_financing_application(customer, vehicle)

    result = submit_to_bank(application)

    print("✅ Financing process complete:", result)
