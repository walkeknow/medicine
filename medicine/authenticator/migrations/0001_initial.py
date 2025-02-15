# Generated by Django 2.1.7 on 2019-04-02 06:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BatchNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_no', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer_name', models.TextField(default='Not Specified', max_length=80)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacturer', models.CharField(default='Not Specified', max_length=80)),
                ('product_name', models.CharField(max_length=80)),
                ('price', models.CharField(max_length=80)),
                ('expiry', models.CharField(max_length=80)),
                ('packing', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='batchnumber',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authenticator.Product'),
        ),
    ]
