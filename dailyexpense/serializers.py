from rest_framework import serializers
from .models import Category,DailyExpense
from datetime import datetime


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id', 'category_name']

class DailyExpenseSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category')
    class Meta:
        model=DailyExpense
        fields='__all__'
        depth=1

class MonthlyWiseExpenseSerializer(serializers.ModelSerializer):
    # category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category')
    # category=CategorySerializer()
    monthly_expense = serializers.DecimalField(max_digits=10, decimal_places=2)
    month=serializers.SerializerMethodField()
    class Meta:
        model=DailyExpense
        fields=['monthly_expense','month','category']
        depth=1

    def get_month(self, obj):
        return obj['month'].strftime('%y-%b-%d')
        

class DailyWiseExpenseSerializer(serializers.ModelSerializer):
    # category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category')
    daily_expense = serializers.DecimalField(max_digits=10, decimal_places=2)
    daily_income=serializers.DecimalField(max_digits=10, decimal_places=2)
    daily_savings=serializers.DecimalField(max_digits=10, decimal_places=2)
    daily=serializers.SerializerMethodField()

    class Meta:
        model=DailyExpense
        fields=['daily_income','daily_expense','daily_savings','daily']
    
    def get_daily(self, obj):
        return obj['daily'].strftime('%d')
    # def validate(self, data):
    #     print(data)
    #     if data['income']<0 or data['expense']<0:
    #         raise serializers.ValidationError('value Should be Greater than 0')
    #     return data
class yearlyWiseExpenseSerializer(serializers.ModelSerializer):
    # category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category')
    yearly_expense = serializers.DecimalField(max_digits=10, decimal_places=2)
    yearly_income=serializers.DecimalField(max_digits=10, decimal_places=2)
    yearly_savings=serializers.DecimalField(max_digits=10, decimal_places=2)
    year=serializers.SerializerMethodField()
    id=serializers.SerializerMethodField()

    class Meta:
        model=DailyExpense
        fields=['id','yearly_income','yearly_expense','yearly_savings','year']
    
    def get_year(self, obj):
        return obj['year'].strftime('%Y')
    def get_id(self, obj):
        return obj['id']


class DateWiseIncomeSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    # total_income= serializers.SerializerMethodField()

    class Meta:
        model=DailyExpense
        fields=['id','purpose','income','category_name']
    

    
    def get_category_name(self, obj):
        return obj.category.category_name if obj.category else None
    
class DateWiseExpenseSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model=DailyExpense
        fields=['id','purpose','expense','category_name']
    
    def get_category_name(self, obj):
        return obj.category.category_name if obj.category else None
    


class YearlyCountIncomeSerializer(serializers.ModelSerializer):
    total_yearly_income = serializers.DecimalField(max_digits=10, decimal_places=2)
    yearly=serializers.SerializerMethodField()

    class Meta:
        model=DailyExpense
        fields=['total_yearly_income','yearly']
    
    def get_total_yearly_income(self, obj):
        print(obj)
        # return obj.category.category_name if obj.category else None
    def get_yearly(self, obj):
        return obj['yearly'].strftime('%Y')
    

    
        