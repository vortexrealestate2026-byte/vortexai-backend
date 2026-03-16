from agents.property_task import run_property_agent

def launch_agents():

    for i in range(25):

        run_property_agent.delay()
