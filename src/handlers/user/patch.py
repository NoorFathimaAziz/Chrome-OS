from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class UserPatch:

    def __init__(self) -> None:
        pass
    
    def handle(self, body):
        service = GoogleService([ChromeScopes.USER]).build_service()
        reponse = service.users().patch( 
            userKey=body['userKey'], 
            body=body['update']
        ).execute()
        return reponse