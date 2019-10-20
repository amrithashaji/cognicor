# Generated by Django 2.2 on 2019-10-20 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image_as_a_blob',
            field=models.ImageField(default='pic_folder/None/no-img.jpg', upload_to='static/image'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
