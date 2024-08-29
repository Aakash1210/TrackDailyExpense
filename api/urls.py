from dailyexpense.views import home,ExpenseAPI,CategoryAPI,get_daily_expense_by_id
from django.urls import path

urlpatterns = [
    path('', home),
    path('daily_expense/',ExpenseAPI.as_view(),name='all_daily_expense'),
    path('categories/', CategoryAPI.as_view(), name='all_category'),
    path('daily_expense/id/<int:pk>/',get_daily_expense_by_id,name='daily_expense_id'),
    path('daily_expense/delete/<int:pk>/',ExpenseAPI.as_view(),name='daily_expense_del_id')

]