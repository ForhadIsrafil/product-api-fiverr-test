# Generated by Django 4.0.4 on 2022-04-27 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Available', 'available'), ('Unavailable', 'unavailable')], default='available', max_length=50),
        ),
    ]
