from .models.TLAccount_frequest import TLAccount
from rest_framework import serializers


class TLAccountDetailSerializer(serializers.ModelSerializer):
    qualities = serializers.SlugRelatedField(slug_field="quality", many=True,
                                             read_only=True)

    class Meta:
        model = TLAccount
        exclude = ['last_login', 'password', 'twitter', 'facebook',
                   'friends', 'followers', 'people_which_follow',
                   'can_get_message_from', 'strangers', 'date_joined',
                   'is_superuser', 'is_admin', 'is_active', 'is_staff',
                   'groups', 'user_permissions']
