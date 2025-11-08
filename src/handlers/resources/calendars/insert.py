from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService
# from src.utils.sha1 import generate_sha1

class CalAdd:

    def __init__(self) -> None:
        pass
    
    def caladd(self, body):
        service = GoogleService([ChromeScopes.CALENDAR]).build_service()
        response = service.resources().calendars().insert(customer = ChromeConfig.CUSTOMER_ID,body=body).execute()
        return response
    
