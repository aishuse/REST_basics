from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from api_basic import views
from api_basic.views import ArticleViewset

router = DefaultRouter()
router.register('article', ArticleViewset, basename='article')

urlpatterns = [
    # path("article/", views.article_list),
    # path("article/<int:pk>/", views.article_detail)
    # path("article/", views.ArticleList.as_view()),
    # path("article/<int:pk>/", views.ArticleDetail.as_view()),
    # path("generic/article/<int:id>/", views.GenericAPIView.as_view())
    path('viewset/', include(router.urls)),

]
# urlpatterns = format_suffix_patterns(urlpatterns)
