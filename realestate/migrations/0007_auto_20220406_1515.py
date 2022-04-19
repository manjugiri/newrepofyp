# Generated by Django 3.2.9 on 2022-04-06 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0006_auto_20220405_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplyAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Agency_name', models.CharField(max_length=50)),
                ('Agency_Location', models.CharField(max_length=50)),
                ('Agency_Contact', models.CharField(max_length=50)),
                ('Agency_Email', models.EmailField(max_length=254)),
                ('Agency_Description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='properti',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bank',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bidders',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='properti',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]