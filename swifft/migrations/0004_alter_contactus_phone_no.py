# Generated by Django 3.2.9 on 2022-01-26 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swifft', '0003_auto_20220126_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='Phone_no',
            field=models.IntegerField(max_length=50, null=True),
        ),
    ]
