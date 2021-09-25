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
        fields = ('id' ,'username','phone', 'email', 'password', 'first_name', 'last_name','user_type')
        extra_kwargs = {'password': {'write_only': True}}

    # def clean(self):
    #     self.data['password']

    def create(self, validated_data):
        user = User(username=validated_data['username'],phone=validated_data['phone'], email=validated_data['email'],
                    first_name=validated_data['first_name'], last_name=validated_data['last_name']
                    , password=validated_data['password'])
        user.set_password(validated_data['password'])
        user.save()
        return user
