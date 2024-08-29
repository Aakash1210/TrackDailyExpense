from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from .serializers import DailyExpenseSerializer,CategorySerializer
from .models import DailyExpense,Category
# Create your views here.

@api_view(['GET'])
def home(request):
    return Response({"status":True,"message":"Hello,World!!"},status.HTTP_200_OK)

class ExpenseAPI(APIView):
    def get(self,request):#DailyExpense
        try:
            daily_expense_data=DailyExpense.objects.all()
            serializer=DailyExpenseSerializer(data=daily_expense_data, many=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        except Exception as e:
            return Response({
                'status':False,
                'message':serializer.errors
            })
        
    def post(self,request):
        daily_expense_data=request.data
        serializer=DailyExpenseSerializer(data=daily_expense_data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({
                'status':serializer.data,
                'message':serializer.errors
            })
    
    def put(self,request):
        pass

    def patch(self,request):
        daily_expense_data=request.data
        daily_expense_objs=DailyExpense.objects.get(id=daily_expense_data['id'])
        serializer=DailyExpenseSerializer(daily_expense_objs,data=daily_expense_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self,request):
        daily_expense_data=request.data
        daily_expense_objs=DailyExpense.objects.get(id=daily_expense_data['id'])
        daily_expense_objs.delete()
        return Response({"message":f"Delete the data"})


class CategoryAPI(APIView):
    def get(self,request):#Category
        category_data=Category.objects.all()
        serializer=CategorySerializer(data=category_data, many=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def post(self,request):
        category_data=request.data
        serializer=CategorySerializer(data=category_data,many=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
