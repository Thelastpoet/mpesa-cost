# Generated by Django 4.2.7 on 2023-11-14 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpesacal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('send_money_to_registered_users', 'Send Money to Another M-pesa'), ('withdraw', 'Withdraw')], max_length=255, null=True),
        ),
    ]