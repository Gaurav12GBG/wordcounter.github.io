# Generated by Django 3.2.8 on 2021-12-16 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textutils', '0003_auto_20211216_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfeedback',
            name='feedback',
            field=models.TextField(max_length=250, null=True),
        ),
    ]