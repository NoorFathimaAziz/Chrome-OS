from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class AliasAdd:

    def __init__(self) -> None:
        pass
    
    def handle(self, body):
        service = GoogleService([ChromeScopes.USER_ALIAS]).build_service()
        reponse = service.users().aliases().insert(
            userKey = body['userKey'],
            body=body).execute()
        return reponse 