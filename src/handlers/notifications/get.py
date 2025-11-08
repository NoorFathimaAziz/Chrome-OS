from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class GetNotifi:

    def __init__(self) -> None:
        pass

    def get(self,customer, notificationId):
        service = GoogleService([ChromeScopes.NOTIFICATION]).build_service()
        reponse = service.notifications().get(
            customer = customer,
            notificationId= notificationId
        ).execute()
        return reponse