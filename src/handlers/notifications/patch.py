from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class Patchnotifi:

    def __init__(self) -> None:
        pass
    
    def patch(self,body ):
        service = GoogleService([ChromeScopes.NOTIFICATION]).build_service()
        response = service.notifications().patch( 
            customer=body['userKey'],
            notificationId=body['update'],
            body = body
        ).execute()
        return response