# Generated by Django 2.0.2 on 2018-02-18 07:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0010_file'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExampleModel',
        ),
        migrations.DeleteModel(
            name='File',
        ),
        migrations.DeleteModel(
            name='userStatus',
        ),
    ]