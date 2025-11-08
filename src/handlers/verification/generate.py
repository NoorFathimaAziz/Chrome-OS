from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class  verificationGenerate:

    def __init__(self) -> None:
        pass
    
    def handle(self,userKey):
        service = GoogleService([ChromeScopes.VERIFICATION]).build_service()
        reponse = service.verificationCodes().generate(userKey = userKey).execute()
        return reponse 