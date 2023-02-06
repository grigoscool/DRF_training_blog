from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializers import ArticleSerialize


class ArticleList(APIView):
    def get(self, request):
        queryset = Article.objects.all()
        serialize_queryset = ArticleSerialize(queryset, many=True)
        return Response(serialize_queryset.data)
