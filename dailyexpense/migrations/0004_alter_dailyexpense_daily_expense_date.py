# Generated by Django 5.1 on 2024-09-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyexpense', '0003_alter_dailyexpense_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyexpense',
            name='daily_expense_date',
            field=models.DateField(),
        ),
    ]
