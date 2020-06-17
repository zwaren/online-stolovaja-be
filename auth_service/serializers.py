from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, 
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], 
            validated_data['email'], validated_data['password'])
        group = Group.objects.get(name='user') 
        group.user_set.add(user)
        return user

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}