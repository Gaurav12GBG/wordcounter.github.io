# Generated by Django 3.2.8 on 2021-12-13 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textutils', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'wordadmincontact',
            },
        ),
        migrations.DeleteModel(
            name='UserReg',
        ),
    ]