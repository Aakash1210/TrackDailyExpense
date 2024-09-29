from dailyexpense.views import home,ExpenseAPI,CategoryAPI,get_daily_expense_by_id,get_monthlywise_expense,get_dailywise_expense,get_yearlywise_expense,get_Datewise_income,get_YearlyTotalCount
from django.urls import path

urlpatterns = [
    path('', home),
    path('daily_expense/',ExpenseAPI.as_view(),name='all_daily_expense'),
    path('categories/', CategoryAPI.as_view(), name='all_category'),
    path('daily_expense/id/<int:pk>/',get_daily_expense_by_id,name='daily_expense_id'),
    path('daily_expense/delete/<int:pk>/',ExpenseAPI.as_view(),name='daily_expense_del_id'),
    path('daily_expense/monthly/',get_monthlywise_expense,name='get_monthlywise_expense'),
    path('daily_expense/daily/',get_dailywise_expense,name='get_dailywise_expense'),
    path('daily_expense/yearly/',get_yearlywise_expense,name='get_yearlywise_expense'),
    path('daily_expense/income_date/<str:date>/',get_Datewise_income,name='get_Datewise_income'),
    path('daily_expense/total_yearly_count/',get_YearlyTotalCount,name='get_YearlyTotalCount'),
    
  

]