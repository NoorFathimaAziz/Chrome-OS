from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class CalGet:

    def __init__(self) -> None:
        pass

    def calget(self,calendarResourceId ):
        service = GoogleService([ChromeScopes.CALANDER_READ_ONLY]).build_service()
        response = service.resources().calendars().get(customer =ChromeConfig.CUSTOMER_ID, calendarResourceId = calendarResourceId).execute()
        return response