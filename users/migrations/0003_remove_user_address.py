# Generated by Django 3.1.3 on 2020-12-09 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_date_of_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='address',
        ),
    ]
