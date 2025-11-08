from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class MemberDelete:
    def __init__(self):   
        pass
    def handle(self, groupKey,memberKey):
        service = GoogleService([ChromeScopes.GROUP_MEMBER]).build_service()
        response = service.members().delete(
                groupKey=groupKey,
                memberKey= memberKey 
            ).execute()
        return response 