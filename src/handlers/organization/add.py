from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class OrganizationAdd:

    def __init__(self) -> None:
        pass
    
    def handle(self, body):
        service = GoogleService([ChromeScopes.ORG_UNITS]).build_service()
        reponse = service.orgunits().insert(customerId=ChromeConfig.CUSTOMER_ID, body=body).execute()
        return reponse
    
