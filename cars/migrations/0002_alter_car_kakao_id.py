# Generated by Django 4.0.5 on 2022-07-12 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='kakao_id',
            field=models.BigIntegerField(null=True, unique=True),
        ),
    ]
