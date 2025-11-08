
from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class OrganizationDelete:

    def __init__(self) -> None:
        pass

    def handle(self, orgUnitPath):
        service = GoogleService([ChromeScopes.ORG_UNITS]).build_service()
        reponse = service.orgunits().delete(customerId=ChromeConfig.CUSTOMER_ID, orgUnitPath=orgUnitPath).execute()
        return reponse