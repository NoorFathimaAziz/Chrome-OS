from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class MemberGet:

    def __init__(self) -> None:
        pass

    def handle(self, groupKey,memberKey):
        service = GoogleService([ChromeScopes.GROUP_MEMBER_READ_ONLY]).build_service()
        reponse = service.members().get(groupKey=groupKey,memberKey = memberKey).execute()
        return reponse