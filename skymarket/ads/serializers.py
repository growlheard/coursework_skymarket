from rest_framework import serializers

from ads.models import Ad, Comment

from users.models import User


class CommentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для комментариев.
    """

    author_first_name = serializers.ReadOnlyField(source='author.first_name')
    author_last_name = serializers.ReadOnlyField(source='author.last_name')

    class Meta:
        model = Comment
        fields = ['id', 'text', 'created_at', 'author_first_name', 'author_last_name']


class AdSerializer(serializers.ModelSerializer):
    """
    Сериализатор для объявлений.
    """

    author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для деталей объявлений.
    """

    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'
