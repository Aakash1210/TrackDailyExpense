from django.contrib import admin
from .models import DailyExpense,Category
# Register your models here.
admin.site.register(DailyExpense)
admin.site.register(Category)
