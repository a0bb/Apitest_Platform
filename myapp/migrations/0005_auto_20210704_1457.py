# Generated by Django 2.2 on 2021-07-04 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_dbapis'),
    ]

    operations = [
        migrations.AddField(
            model_name='dbapis',
            name='last_api_body',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='dbapis',
            name='last_body_method',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
