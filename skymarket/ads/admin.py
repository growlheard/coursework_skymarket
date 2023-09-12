from django.contrib import admin

from ads.models import Ad, Comment


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    """
       Административная панель для модели Ad.
       Определяет настройки отображения и фильтрации для модели Ad в административной панели Django.
    """
    list_display = ('title', 'price', 'author', 'created_at')
    list_filter = ('author', 'created_at')
    search_fields = ('title', 'description')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
        Административная панель для модели Comment.
        Определяет настройки отображения и фильтрации для модели Comment в административной панели Django.
    """
    list_display = ('text', 'author', 'ad', 'created_at')
    list_filter = ('author', 'ad', 'created_at')
    search_fields = ('text',)
