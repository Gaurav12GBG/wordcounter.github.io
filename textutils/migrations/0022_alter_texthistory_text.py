# Generated by Django 4.0 on 2022-01-10 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textutils', '0021_rename_textcontent_texthistory_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texthistory',
            name='text',
            field=models.CharField(max_length=250),
        ),
    ]
