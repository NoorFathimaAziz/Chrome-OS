from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class GroupGet:

    def __init__(self) -> None:
        pass

    def handle(self, groupKey):
        service = GoogleService([ChromeScopes.GROUP]).build_service()
        reponse = service.groups().get(groupKey=groupKey).execute()
        return reponse