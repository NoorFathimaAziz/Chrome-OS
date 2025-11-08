
from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class OrganizationGet:

    def __init__(self) -> None:
        pass

    def handle(self, orgUnitPath):
        service = GoogleService([ChromeScopes.ORG_UNITS_READ_ONLY]).build_service()
        reponse = service.orgunits().get(customerId=ChromeConfig.CUSTOMER_ID, orgUnitPath=orgUnitPath).execute()
        return reponse