from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class verificationInvaild:

    def __init__(self) -> None:
        pass
    
    def handle(self,userKey):
        service = GoogleService([ChromeScopes.VERIFICATION]).build_service()
        reponse = service.verificationCodes().Invalidate(userKey = userKey).execute()
        return reponse