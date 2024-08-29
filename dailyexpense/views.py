from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from .serializers import DailyExpenseSerializer,CategorySerializer
from .models import DailyExpense,Category
from django.db import IntegrityError
from rest_framework.exceptions import ValidationError

# Create your views here.

@api_view(['GET'])
def home(request):
    return Response({"status":True,"message":"Hello,World!!"},status.HTTP_200_OK)


@api_view(['GET'])
def get_daily_expense_by_id(request,pk):
    try:
        daily_expense_id = DailyExpense.objects.get(pk=pk)
    except DailyExpense.DoesNotExist:
        return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = DailyExpenseSerializer(daily_expense_id)
    return Response(serializer.data, status=status.HTTP_200_OK)

class ExpenseAPI(APIView):
    def get(self,request):#DailyExpense
        try:
            daily_expense_data=DailyExpense.objects.all()
        except DailyExpense.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer=DailyExpenseSerializer(daily_expense_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        try:
            serializer=DailyExpenseSerializer(data=request.data,many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED) 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except IntegrityError:
            return Response({"error": "Database integrity error occurred."}, status=status.HTTP_400_BAD_REQUEST)
        
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
        except Exception as e:
            return Response({"error": "An unexpected error occurred.","message":{e}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self,request):
        pass

    def patch(self,request):
        try:
            daily_expense_data=request.data
            try:
                daily_expense_objs=DailyExpense.objects.get(id=daily_expense_data['id'])
            except DailyExpense.DoesNotExist:
                return Response({"error": "Daily expense not found."}, status=status.HTTP_404_NOT_FOUND)
            
            serializer=DailyExpenseSerializer(daily_expense_objs,data=daily_expense_data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except IntegrityError:
            return Response({"error": "Database integrity error occurred."}, status=status.HTTP_400_BAD_REQUEST)

        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": "An unexpected error occurred.","message":{e}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def delete(self,request,pk):
        try:
            daily_expense_id = DailyExpense.objects.get(pk=pk)
        except DailyExpense.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        daily_expense_id.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class CategoryAPI(APIView):
    def get(self,request):#Category
        try:
            category_data=Category.objects.all()
        except Category.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer=CategorySerializer(category_data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self,request):
        try:
            category_data=request.data
            serializer=CategorySerializer(data=category_data,many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED) 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except IntegrityError:
            return Response({"error": "Database integrity error occurred."}, status=status.HTTP_400_BAD_REQUEST)
        
        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
        except Exception as e:
            return Response({"error": "An unexpected error occurred.","message":{e}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
