from src.security.authentication.api_key import CustomAPIKeyCookie, CustomAPIKeyHeader, CustomAPIKeyQuery

CustomAPIKey = CustomAPIKeyCookie | CustomAPIKeyHeader | CustomAPIKeyQuery
