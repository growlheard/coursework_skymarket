from djoser.views import UserViewSet as DjoserUserViewSet

from users.serializers import CurrentUserSerializer, UserRegistrationSerializer


class UserViewSet(DjoserUserViewSet):
    """
       Класс представления для пользователей.
    """
    serializer_class = UserRegistrationSerializer

    def get_serializer_class(self):
        if self.action == 'me':
            return CurrentUserSerializer
        return super().get_serializer_class()
