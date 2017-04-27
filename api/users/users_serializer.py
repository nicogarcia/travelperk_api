from rest_framework.serializers import ModelSerializer

from api.users.users_model import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User

        fields = (
            'email',
            'password'
        )

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        email = validated_data.get('email')
        password = validated_data.get('password')

        user = User.objects.create_user(email, password)
        return user
