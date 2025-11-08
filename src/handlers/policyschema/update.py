from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class PolicySchemaUpdate:

    def __init__(self) -> None:
        pass
    
    def handle(self, json_data):
        service = GoogleService([ChromeScopes.POLICY]).chrome_policy_service()
        response = service.customers().policies().orgunits()\
            .batchModify(customer=f'customers/{ChromeConfig.CUSTOMER_ID}', body=json_data).execute()
        return response