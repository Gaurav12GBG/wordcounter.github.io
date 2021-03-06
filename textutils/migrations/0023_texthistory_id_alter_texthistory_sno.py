# Generated by Django 4.0 on 2022-01-10 16:48

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('textutils', '0022_alter_texthistory_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='texthistory',
            name='id',
            field=models.BigAutoField(auto_created=True, default=datetime.datetime(2022, 1, 10, 16, 48, 3, 176433, tzinfo=utc), primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='texthistory',
            name='sno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
