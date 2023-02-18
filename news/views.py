from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views import generic

from news.models import News
from news.serializers import NewsSerializer
DEFAULT_NEWS_PER_PAGE = 50
DEFAULT_NEWS_PER_REST_API = 100


class LatestNewsView(generic.ListView):
    template_name = 'news.html'
    context_object_name = 'latest_news'

    def get_queryset(self):
        return News.objects.order_by('-published_at')[:DEFAULT_NEWS_PER_PAGE]


class DetailView(generic.DetailView):
    model = News
    template_name = 'details.html'


@api_view(['GET'])
def get_news(request):
    news = News.objects.all()[:DEFAULT_NEWS_PER_REST_API]
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)
