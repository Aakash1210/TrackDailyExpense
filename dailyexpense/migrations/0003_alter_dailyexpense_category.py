# Generated by Django 5.1 on 2024-08-29 15:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyexpense', '0002_alter_dailyexpense_purpose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyexpense',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='category_expenses', to='dailyexpense.category'),
        ),
    ]
