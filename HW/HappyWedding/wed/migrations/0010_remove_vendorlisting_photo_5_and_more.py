# Generated by Django 5.0 on 2024-04-17 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wed', '0009_vendorlisting_district'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorlisting',
            name='photo_5',
        ),
        migrations.AlterField(
            model_name='vendorlisting',
            name='photo_1',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='vendorlisting',
            name='photo_2',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='vendorlisting',
            name='photo_3',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.AlterField(
            model_name='vendorlisting',
            name='photo_4',
            field=models.ImageField(upload_to='images'),
        ),
    ]
