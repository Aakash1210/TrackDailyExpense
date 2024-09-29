from django.db import models

# Create your models here.

class Category(models.Model):
        category_name=models.CharField(max_length=20,unique=True)
        def __str__(self) -> str:
            return self.category_name
class DailyExpense(models.Model):
    id= models.AutoField(primary_key=True)
    purpose=models.CharField(max_length=50,blank=False)
    income=models.DecimalField(max_digits=10,decimal_places=2,blank=True,default=0.00)
    expense=models.DecimalField(max_digits=10,decimal_places=2,blank=True,default=0.00)
    category=models.ForeignKey(Category,null=False,blank=True,on_delete=models.CASCADE,related_name='category_expenses')
    daily_expense_date=models.DateField(blank=False,null=False)
    descriptions= models.TextField(max_length=50,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.purpose} - {self.category if self.category else 'No Category'} ({self.daily_expense_date})"
