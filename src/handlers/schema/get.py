from src.config import ChromeConfig
from src.config import ChromeScopes
from src.credentials.google_auth import GoogleService

class SchemaGet:

    def __init__(self) -> None:
        pass

    def handle(self, schemaKey):
        service = GoogleService([ChromeScopes.SCHEMAS_READ_ONLY]).build_service()
        reponse = service.schemas().get(customerId=ChromeConfig.CUSTOMER_ID, schemaKey = schemaKey).execute()
        return reponse