# Generated by Django 5.1.3 on 2024-12-04 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_perfume_gender_alter_perfume_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfume',
            name='size',
            field=models.CharField(choices=[('25 ml', '25 ml'), ('50 ml', '50 ml'), ('75 ml', '75 ml')], default='25 ml', max_length=10),
        ),
    ]
