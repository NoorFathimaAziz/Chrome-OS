from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class OrganizationUpdatePatch:

    def __init__(self) -> None:
        pass
    
    def handle(self, body):
        service = GoogleService([ChromeScopes.ORG_UNITS]).build_service()
        reponse = service.orgunits().patch(
            customerId=ChromeConfig.CUSTOMER_ID, 
            orgUnitPath=body['orgUnitId'], 
            body=body['update']
        ).execute()
        return reponse
    
