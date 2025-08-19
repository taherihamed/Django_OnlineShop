from .models import User
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer

class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'firstname', 'lastname']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']