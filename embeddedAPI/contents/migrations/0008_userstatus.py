# Generated by Django 2.0.2 on 2018-02-09 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0007_auto_20180208_2308'),
    ]

    operations = [
        migrations.CreateModel(
            name='userStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=20)),
                ('comments', models.CharField(max_length=500, null=True)),
            ],
        ),
    ]