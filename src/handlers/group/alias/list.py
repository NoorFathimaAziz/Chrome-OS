from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class AliasListGroup:

    def __init__(self) -> None:
        pass
    
    def handle(self,groupKey):
        service = GoogleService([ChromeScopes.GROUP_READ_ONLY]).build_service()
        reponse = service.groups().aliases().list(
           groupKey = groupKey,
        ).execute()
        return reponse 