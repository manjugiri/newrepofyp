# Generated by Django 3.2.9 on 2022-04-04 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realestate', '0003_auto_20220404_1356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bidders',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='bidders',
            name='start_date',
        ),
        migrations.AddField(
            model_name='properti',
            name='bidding_end_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='properti',
            name='bidding_start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bidders',
            name='properti',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidders_prop', to='realestate.properti'),
        ),
    ]
