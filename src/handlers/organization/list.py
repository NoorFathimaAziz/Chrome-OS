
from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class OrganizationList:

    def __init__(self) -> None:
        pass
    
    def handle(self, type):
        service = GoogleService([ChromeScopes.ORG_UNITS_READ_ONLY]).build_service()
        reponse = service.orgunits().list(customerId=ChromeConfig.CUSTOMER_ID, type=type).execute()
        return reponse
