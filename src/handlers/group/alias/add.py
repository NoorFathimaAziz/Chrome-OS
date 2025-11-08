from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class AliasAddGroup:

    def __init__(self) -> None:
        pass
    
    def handle(self, body):
        service = GoogleService([ChromeScopes.GROUP]).build_service()
        reponse = service.groups().aliases().insert(
            groupKey = body['groupKey'],
            body=body).execute()
        return reponse 