import os

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY: str = os.getenv("apiKey", "")
SUCCESS_STATUS = "ok"

DEFAULT_NEWS_PER_PAGE = 20
DEFAULT_NEWS_PER_REST_API = 100
