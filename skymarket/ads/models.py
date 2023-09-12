from django.db import models

from users.models import NULLABLE


class Ad(models.Model):
    """
    Модель объявления.
    Описывает объявление, содержащее изображение, название товара, цену, описание, автора и дату создания.
    """
    image = models.ImageField(upload_to='images_ad/', **NULLABLE, verbose_name='Изображение')
    title = models.CharField(max_length=255, verbose_name='Название товара')
    price = models.IntegerField(verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Автор')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Comment(models.Model):
    """
    Модель комментария.
    Описывает комментарий к объявлению, содержащий текст, автора, связь с объявлением и дату создания.
    """
    text = models.TextField(verbose_name='Текст отзыва')
    author = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='Автор')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='Объявление')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

