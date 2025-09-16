from rest_framework import serializers
from .models import Category, Expense
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username']
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields='__all__'

