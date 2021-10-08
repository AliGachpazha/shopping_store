from rest_framework import serializers
# from customer.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'phone', 'email', 'password', 'first_name', 'last_name',)


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    # confirm_password = serializers.CharField()
    class Meta:
        model = User
        fields = ('id', 'username', 'phone', 'email', 'password', 'first_name', 'last_name', 'user_type')
        extra_kwargs = {'password': {'write_only': True}}

    # def clean(self):
    #     self.data['password']

    def create(self, validated_data):
        user = User(username=validated_data['username'], phone=validated_data['phone'], email=validated_data['email'],
                    first_name=validated_data['first_name'], last_name=validated_data['last_name']
                    , password=validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class ChangeCustomerPasswordSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(max_length=100)
    password2 = serializers.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['password', 'password1', 'password2']


class CustomerEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()


class ResetPasswordCodeSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50, min_length=30)
    password1 = serializers.CharField(max_length=50)
    password2 = serializers.CharField(max_length=50)