# Generated by Django 3.1.4 on 2021-01-03 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0002_auto_20210103_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]