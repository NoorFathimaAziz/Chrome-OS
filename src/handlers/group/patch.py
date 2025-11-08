from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class GroupPatch:

    def __init__(self) -> None:
        pass
    
    def handle(self, body):
        service = GoogleService([ChromeScopes.GROUP]).build_service()
        reponse = service.groups().patch( 
            groupKey=body['groupKey'], 
            body=body['update']
        ).execute()
        return reponse  