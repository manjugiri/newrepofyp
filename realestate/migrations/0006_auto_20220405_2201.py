# Generated by Django 3.1.4 on 2022-04-05 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0005_auto_20220405_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='Rate',
            field=models.CharField(max_length=50),
        ),
    ]