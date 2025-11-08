from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class ActionHandler:
    def __init__(self) -> None:
        pass

    def chromeaction(self, body):
        service = GoogleService([ChromeScopes.CHROMEOS]).build_service()
        
        response = service.chromeosdevices().action(
            customerId=ChromeConfig.CUSTOMER_ID,
            resourceId=body['resourceId'][0],  # Take first resourceId
            body={
                "action": body['action']
            }
        ).execute()
        
        return response