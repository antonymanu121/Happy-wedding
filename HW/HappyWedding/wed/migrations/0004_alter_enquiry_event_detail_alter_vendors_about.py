# Generated by Django 5.0 on 2024-04-15 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wed', '0003_alter_enquiry_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='Event_detail',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='vendors',
            name='About',
            field=models.CharField(max_length=1000),
        ),
    ]
