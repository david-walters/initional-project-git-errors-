# Generated by Django 5.1.3 on 2024-12-01 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfume',
            name='size',
            field=models.CharField(choices=[('25 ml', '25 ml'), ('50 ml', '50 ml'), ('100 ml', '100 ml')], default='25 ml', max_length=10),
        ),
    ]
