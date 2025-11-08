from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class GroupAdd:

    def __init__(self) -> None:
        pass
    
    def handle(self, body):
        service = GoogleService([ChromeScopes.GROUP]).build_service()
        reponse = service.groups().insert(body=body).execute()
        return reponse