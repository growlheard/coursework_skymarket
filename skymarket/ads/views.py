from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from ads.models import Ad, Comment
from ads.serializers import AdSerializer, CommentSerializer
from ads.filters import AdFilter
from ads.pagination import AdsPagination

from ads.permissions import IsReadOnlyOrAuthenticated, IsAdminOrAuthorOrReadOnly


class AdViewSet(viewsets.ModelViewSet):
    """
    Представление для модели Ad.

    Это представление позволяет выполнять операции CRUD (создание, чтение, обновление, удаление) для модели Ad.
    """

    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdsPagination
    permission_classes = [IsReadOnlyOrAuthenticated, IsAdminOrAuthorOrReadOnly]
    filterset_class = AdFilter
    filterset_fields = ['title']

    def perform_create(self, serializer):
        """
        Выполняет действия при создании нового Ad.

        При создании нового Ad автором будет текущий пользователь.
        """
        serializer.save(author=self.request.user)

    def get_queryset(self):
        queryset = super().get_queryset()
        filterset = self.filterset_class(self.request.GET, queryset=queryset)
        print("Применяемые фильтры:", filterset.form.data)

        return filterset.qs


class CommentViewSet(viewsets.ModelViewSet):
    """
    Представление для модели Comment.

    Это представление позволяет выполнять операции CRUD (создание, чтение, обновление, удаление) для модели Comment.
    """

    serializer_class = CommentSerializer
    permission_classes = [IsReadOnlyOrAuthenticated, IsAdminOrAuthorOrReadOnly]

    def get_queryset(self):
        """
        Возвращает queryset комментариев, относящихся к определенному объявлению.

        Возвращает только комментарии, связанные с объявлением, идентификатор которого передан в URL.
        """
        ad_id = self.kwargs.get('ad_pk')
        return Comment.objects.filter(ad_id=ad_id)

    def perform_create(self, serializer):
        """
        Выполняет действия при создании нового Comment.

        При создании нового Comment автором будет текущий пользователь, а объявление будет получено из URL.
        """
        ad_id = self.kwargs.get('ad_pk')
        ad = get_object_or_404(Ad, pk=ad_id)
        serializer.save(author=self.request.user, ad=ad)
