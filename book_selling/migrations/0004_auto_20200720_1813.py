# Generated by Django 3.0.8 on 2020-07-20 18:13

import BookSelling.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_selling', '0003_auto_20200719_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaserequest',
            name='tel_number',
            field=models.CharField(max_length=12, validators=[BookSelling.validators.validate_phone_number]),
        ),
    ]
