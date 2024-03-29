# Generated by Django 4.1.3 on 2023-06-06 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_services_discount_services_price_services_tag_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='serviceImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='service')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_image', to='main.services')),
            ],
        ),
    ]
