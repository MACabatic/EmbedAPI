# Generated by Django 2.0.2 on 2018-02-08 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0004_userprofile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_pic', models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='pic_folder/')),
            ],
        ),
    ]
