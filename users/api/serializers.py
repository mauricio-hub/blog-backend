from rest_framework import serializers
from users.models import User

# este serializador crea un usuario
class UserRegisterSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','username','password']
    #     extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
class UserSerializer(serializers.ModelSerializer):
       class Meta:
        model = User
        fields = ['id','email','username','password']
        

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name']
        
        
           