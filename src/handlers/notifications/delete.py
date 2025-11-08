from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class DeleteNotifi:
    def __init__(self):   
        pass
    def delete(self,customer,notificationID ):
        service = GoogleService([ChromeScopes.NOTIFICATION]).build_service()
        response = service.users().delete(
                customer = customer,
                notificationID = notificationID
            ).execute()
            
           
        
        




        
       