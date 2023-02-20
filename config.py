import os

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
API_KEY: str = os.getenv("NEWS_API_KEY", "af92652e76b745a6bde8dd2fc5739bfd")
SUCCESS_STATUS = "ok"

DEFAULT_NEWS_PER_PAGE = 20
DEFAULT_NEWS_PER_REST_API = 100
