# Generated by Django 4.2.1 on 2023-05-08 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('photo', models.ImageField(upload_to='category-images/')),
                ('description', models.TextField(verbose_name=200)),
            ],
        ),
        migrations.CreateModel(
            name='Wood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(verbose_name=350)),
                ('date_of_manufacture', models.DateTimeField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('photo', models.ImageField(upload_to='', verbose_name='wood-images/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
            ],
        ),
    ]
