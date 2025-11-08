from src.config import ChromeScopes, ChromeConfig
from src.credentials.google_auth import GoogleService

class CalUpdate:
    def __init__(self):
        pass
    def cal_update(self, body):
        service = GoogleService([ChromeScopes.CALENDAR]).build_service()
        response = service.resources().calendars().update(
                customer = ChromeConfig.CUSTOMER_ID,
                calendarResourceId=body['calendarResourceId'],
                body=body
            ).execute()
        return response
        
       