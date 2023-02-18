import logging
from typing import List

import requests
from django.core.management.base import BaseCommand

from config import API_KEY, NEWS_ENDPOINT, SUCCESS_STATUS
from news.models import News


class Command(BaseCommand):
    help = "Fetch news from News API and add it to the database"

    def add_arguments(self, parser):
        parser.add_argument(
            "--topic",
            "-t",
            help="Add the news of the specified topic",
        )

    def handle(self, *args, **options):
        News.objects.bulk_create(
            self._fetch_news(options["topic"]), ignore_conflicts=True
        )

    @staticmethod
    def _fetch_news(topic="japan") -> List[News]:
        response = requests.request(
            "GET", f"{NEWS_ENDPOINT}?q={topic}&apiKey={API_KEY}"
        ).json()
        if response["status"] == SUCCESS_STATUS:
            articles = response["articles"]
            return [
                News(
                    title=article["title"],
                    author=article["author"],
                    description=article["description"],
                    content=article["content"],
                    url=article["url"],
                    url_to_image=article["urlToImage"],
                    published_at=article["publishedAt"],
                    source_id=article["source"]["id"],
                    source_name=article["source"]["name"],
                )
                for article in articles
            ]
        else:
            logging.error(
                f"News API fetch failed \n "
                f"Code: {response['code']}\n"
                f"Message: {response['message']}"
            )
        return []
