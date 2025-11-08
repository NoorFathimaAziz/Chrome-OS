from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class PhotoGet:

    def __init__(self) -> None:
        pass

    def handle(self, userKey):
        service = GoogleService([ChromeScopes.USER_READ_ONLY]).build_service()
        reponse = service.users().photos().get(userKey=userKey).execute()
        return reponse