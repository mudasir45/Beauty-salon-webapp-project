# Generated by Django 4.1.3 on 2023-06-08 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_order_discount_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]