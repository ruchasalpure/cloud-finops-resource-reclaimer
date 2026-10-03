from crewai import Agent

cloud_finops_resource_reclaimer = Agent(
    role="Cloud Finops Resource Reclaimer",
    goal="Deliver high-precision autonomous Cloud Finops Resource Reclaimer operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
