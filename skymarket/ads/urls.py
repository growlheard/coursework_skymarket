# TODO настройка роутов для модели


from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .apps import SalesConfig
from .views import AdViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'ads', AdViewSet, basename='ad')
router.register(r'ads/(?P<ad_pk>[^/.]+)/comments', CommentViewSet, basename='comment')


app_name = SalesConfig.name
urlpatterns = [
    path('', include(router.urls)),
]
