from dailyexpense.views import home,ExpenseAPI,CategoryAPI
from django.urls import path

urlpatterns = [
    path('', home),
    path('daily_expense/',ExpenseAPI.as_view(),name='daily_expense'),
    path('categories/', CategoryAPI.as_view(), name='get_category'),

]