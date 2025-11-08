from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class MemberAdd:

    def __init__(self) -> None:
        pass
    
    def handle(self, body):
        service = GoogleService([ChromeScopes.GROUP_MEMBER]).build_service()
        reponse = service.members().insert(
            groupKey = body['groupKey'],
            body=body).execute()
        return reponse