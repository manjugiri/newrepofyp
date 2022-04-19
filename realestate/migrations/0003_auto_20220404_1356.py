# Generated by Django 3.2.9 on 2022-04-04 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('realestate', '0002_auto_20220402_1512'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='properti',
            name='bidding_end_time',
        ),
        migrations.CreateModel(
            name='Bidders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_amount', models.FloatField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('properti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidders', to='realestate.properti')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='bidder_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]