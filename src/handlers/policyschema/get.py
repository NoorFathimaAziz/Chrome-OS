from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class PolicySchemaGet:
    def __init__(self) -> None:
        pass


    def policy_get(self, schemakey):
        service = GoogleService([ChromeScopes.POLICY_READ_ONLY]).chrome_policy_service()
        response = service.customers().policySchemas().get(name=f'customers/{ChromeConfig.CUSTOMER_ID}/policySchemas/{schemakey}').execute()

        return response