# Generated by Django 4.0.4 on 2022-12-29 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0003_lavozm_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Murojaj',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('gmail', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('vaqt', models.DateField()),
            ],
        ),
    ]
