from django_filters import rest_framework as filters
from .models import Ad


class AdFilter(filters.FilterSet):
    """
        Фильтр по названию товара.
        Позволяет выполнять фильтрацию объявлений по названию товара, игнорируя регистр.
    """
    title = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Ad
        fields = ['title']
