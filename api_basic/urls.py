from django.urls import  path
from rest_framework.urlpatterns import format_suffix_patterns

from api_basic import views

urlpatterns = [
    # path("article/", views.article_list),
    # path("article/<int:pk>/", views.article_detail)
    path("article/", views.ArticleList.as_view()),
    path("article/<int:pk>/", views.ArticleDetail.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
