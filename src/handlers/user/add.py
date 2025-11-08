from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService
from src.utils.sha1 import generate_sha1

class UserAdd:

    def __init__(self) -> None:
        pass
    
    def handle(self, body):
        body['password'] = generate_sha1(body['password'])
        service = GoogleService([ChromeScopes.USER]).build_service()
        reponse = service.users().insert(body=body).execute()
        return reponse
    
