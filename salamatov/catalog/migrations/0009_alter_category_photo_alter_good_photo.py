# Generated by Django 4.2.1 on 2023-06-04 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_category_photo_alter_good_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='photo',
            field=models.ImageField(upload_to='category-images/'),
        ),
        migrations.AlterField(
            model_name='good',
            name='photo',
            field=models.ImageField(upload_to='good-images/'),
        ),
    ]