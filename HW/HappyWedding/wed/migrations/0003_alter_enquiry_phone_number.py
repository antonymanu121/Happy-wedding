# Generated by Django 5.0 on 2024-04-05 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wed', '0002_alter_enquiry_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='phone_number',
            field=models.PositiveIntegerField(),
        ),
    ]
