# Generated by Django 5.0.1 on 2024-01-22 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0009_alter_experiment_treatment_group_ratio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experiment',
            old_name='experiment_ready',
            new_name='ready',
        ),
    ]