from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService


class CalPatch:

    def __init__(self) -> None:
        pass

    def patch(self,calendarResourceId,body):
        service = GoogleService([ChromeScopes.CALENDAR]).build_service()

        response = service.chromeosderesources().calendars().patch(
            customerId = ChromeConfig.CUSTOMER_ID,
            calendarResourceId = calendarResourceId,
            body = body
            ).execute()
        
        return response