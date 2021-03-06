from django.db.models import fields
from rest_framework import serializers
from .models import *

class UserTypeSerializer(serializers.ModelSerializer):

    class Meta:
        fields = {
            'id'
            'user_type'
        }
        model = UserType
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = {
            'id'
            'username'
            'first_name'
            'last_name'
            'email'
            'password'
        }
        model = User
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = {
            'id'
            'name'
            'created_by'
        }
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        fields = {
            'id'
            'name'
            'price'
            'category'
            'created_by'
            'description'
            'image'
        }
        model = Products
        fields = ['name', 'price', 'description']

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        fields = {
            'id'
            'product'
            'customer'
            'quantity'
            'price'
            'address'
            'phone'
            'date'
            'status'
        }
        model = Order
        fields = '__all__'

class AllProductSerializer(serializers.ModelSerializer):
    items = ProductSerializer(many = True, read_only=True)
    class Meta:
        model = Category
        fields = ['name', 'items', 'created_by']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        category = Category.objects.create(**validated_data)
        for item_data in items_data:
            Products.objects.create(category=category, **item_data)
        return category

# class RegistrationSerializer(serializers.ModelSerializer):

#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

#     class Meta:
#         fields = {
#             'email'
#             'username'
#             'password'
#             'password2'
#         }
#         model = User
#         extra_kwargs = {'password':{'write_only': True}
#         }
    
#     def save(self):
#         user = User(
#                     email=self.validated_data['email'],
#                     username=self.validated_data['username'],
#         )
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']

#         if password != password2:
#             raise serializers.ValidationError({'password': 'Password must match.'})
#         user.set_password(password)
#         user.save()
#         return user


