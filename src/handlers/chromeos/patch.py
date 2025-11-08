from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService


class PatchChrome:

    def __init__(self) -> None:
        pass

    def patch(self,body):
        service = GoogleService([ChromeScopes.CHROMEOS]).build_service()

        response = service.chromeosdevices().patch(
            customerId = ChromeConfig.CUSTOMER_ID,
            deviceId = ChromeConfig.deviceId,
            body = body
            ).execute()
        
        return response