from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class MemberPatch:

    def __init__(self) -> None:
        pass
    
    def handle(self, body):
        service = GoogleService([ChromeScopes.GROUP_MEMBER]).build_service()
        reponse = service.members().patch( 
            groupKey=body['groupKey'], 
            memberKey = body['memberKey'],
            body=body['update']
        ).execute()
        return reponse