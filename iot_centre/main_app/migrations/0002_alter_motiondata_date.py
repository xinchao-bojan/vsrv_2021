# Generated by Django 3.2.9 on 2021-11-06 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='motiondata',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]