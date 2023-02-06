from django.urls import path

from .views import ArticleList

app_name = 'arcticle'

urlpatterns = [
    path('api/v1/', ArticleList.as_view()),
    path('api/v1/<int:pk>', ArticleList.as_view()),

]