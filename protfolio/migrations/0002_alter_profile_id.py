# Generated by Django 3.2.13 on 2023-03-11 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('protfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]