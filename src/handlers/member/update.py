from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class MemberUpdate:
    def __init__(self):
        pass
    def handle(self, body):
        service = GoogleService([ChromeScopes.GROUP_MEMBER]).build_service()
        response = service.members().update(
                groupKey=body['groupKey'],
                memberKey = body['memberKey'],
                body=body['update']
            ).execute()
        return response