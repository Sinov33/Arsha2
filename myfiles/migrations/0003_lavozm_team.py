# Generated by Django 4.0.4 on 2022-12-29 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0002_malumot_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lavozm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=20)),
                ('familiya', models.CharField(max_length=20)),
                ('yosh', models.IntegerField()),
                ('rasm1', models.ImageField(upload_to='media')),
                ('malumot', models.CharField(max_length=200)),
                ('lavozm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.lavozm')),
            ],
        ),
    ]
