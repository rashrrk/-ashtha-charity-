# Generated by Django 4.2 on 2023-07-10 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_volunteertbl_amount_volunteertbl_dtype_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messagetbl',
            name='username',
        ),
        migrations.AlterField(
            model_name='messagetbl',
            name='message',
            field=models.TextField(max_length=100),
        ),
    ]
