# Generated by Django 4.1.1 on 2022-09-18 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='feb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fakultas', models.CharField(max_length=50)),
                ('prodi', models.CharField(max_length=100)),
            ],
        ),
    ]
