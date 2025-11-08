from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService



class UpdateChrome:

    def __init__(self) ->None:
        pass

    def update(self,body):
        service = GoogleService([ChromeScopes.CHROMEOS]).build_service()
        response = service.chromeosdevices().update(
            customerId = ChromeConfig.CUSTOMER_ID,
            deviceId = ChromeConfig.deviceId,
            body = body
        ).execute()

        return response
    