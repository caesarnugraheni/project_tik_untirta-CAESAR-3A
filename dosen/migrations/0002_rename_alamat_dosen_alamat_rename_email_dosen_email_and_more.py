# Generated by Django 4.1.1 on 2022-10-05 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dosen', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dosen',
            old_name='Alamat',
            new_name='alamat',
        ),
        migrations.RenameField(
            model_name='dosen',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='dosen',
            old_name='Fakultas',
            new_name='fakultas',
        ),
        migrations.RenameField(
            model_name='dosen',
            old_name='Nama',
            new_name='foto',
        ),
        migrations.RenameField(
            model_name='dosen',
            old_name='Photo',
            new_name='nama',
        ),
        migrations.RenameField(
            model_name='dosen',
            old_name='NIP',
            new_name='nip',
        ),
        migrations.RenameField(
            model_name='dosen',
            old_name='Prodi',
            new_name='prodi',
        ),
        migrations.RenameField(
            model_name='dosen',
            old_name='Tanggal_Lahir',
            new_name='ttl',
        ),
    ]
