from rest_framework import serializers
from .models import Category,DailyExpense
from datetime import datetime


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
         

class DailyExpenseSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category')
    class Meta:
        model=DailyExpense
        fields='__all__'
        depth=1

    # def validate(self, data):
    #     print(data)
    #     if data['income']<0 or data['expense']<0:
    #         raise serializers.ValidationError('value Should be Greater than 0')
    #     return data
    

    
        