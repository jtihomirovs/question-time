from rest_framework import serializers
from users.models import CustomUser


class UserDisplaySerializer(serializers.ModelSerializer):
    """
    Provide username of user which is currently connected
    """

    class Meta:
        model = CustomUser
        fields = ['username']
