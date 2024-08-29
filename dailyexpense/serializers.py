from rest_framework import serializers
from .models import Category,DailyExpense


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
         

class DailyExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=DailyExpense
        fields='__all__'
        depth=1
    def validate(self, data):
        if data['income']<0 or data['expense']<0:
            raise serializers.ValidationError('value Should be Greater than 0')
        return data

    
        