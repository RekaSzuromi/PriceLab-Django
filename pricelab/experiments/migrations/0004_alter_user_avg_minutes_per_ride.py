# Generated by Django 5.0.1 on 2024-01-17 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0003_rename_users_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avg_minutes_per_ride',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]