from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class CalDel:
    def __init__(self):   
        pass
    def cal_del(self, calendarResourceId):
        service = GoogleService([ChromeScopes.CALENDAR]).build_service()
        response = service.users().delete(calendarResourceId=calendarResourceId).execute()
        return response
           
        
        




        
       