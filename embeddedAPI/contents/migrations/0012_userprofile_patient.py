# Generated by Django 2.0.2 on 2018-02-18 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0011_auto_20180218_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='patient',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]