# Generated by Django 4.0 on 2022-01-11 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textutils', '0024_rename_sno_texthistory_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texthistory',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='texthistory',
            name='text',
            field=models.TextField(max_length=250),
        ),
    ]