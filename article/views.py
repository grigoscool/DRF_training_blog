from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializers import ArticleSerialize


class ArticleList(APIView):
    def get(self, request):
        queryset = Article.objects.all()
        serialize_queryset = ArticleSerialize(queryset, many=True)
        return Response({'article': serialize_queryset.data})

    def post(self, request):
        article = ArticleSerialize(data=request.data)
        article.is_valid(raise_exception=True)
        article.save()

        return Response({'article': article.data})

    def put(self, request, pk):
        article_new = get_object_or_404(Article.objects.get(pk=pk))
        data = request.data.get('article')
        serialize_art = ArticleSerialize(instance=article_new, partial=True, data=data)
        if serialize_art.is_valid(raise_exception=True):
            serialize_art.save()
        return Response({'article': serialize_art.data})
