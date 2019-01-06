# Generated by Django 2.1.4 on 2018-12-31 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ATM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atm_id', models.CharField(max_length=7, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SKPD',
            fields=[
                ('no_skpd', models.CharField(max_length=17, primary_key=True, serialize=False)),
                ('nama_pemilik', models.CharField(max_length=255)),
                ('alamat_pemilik', models.CharField(max_length=255)),
                ('area_koordinasi_pemilik', models.CharField(max_length=255)),
                ('isi_teks', models.CharField(max_length=255)),
                ('tempat_pemasangan', models.CharField(max_length=255)),
                ('lokasi_pemasangan', models.CharField(max_length=255)),
                ('kota_lokasi_pemasangan', models.CharField(max_length=255)),
                ('kecamatan_lokasi_pemasangan', models.CharField(max_length=255)),
                ('kelurahan_lokasi_pemasangan', models.CharField(max_length=255)),
                ('masa_berlaku_awal', models.DateField()),
                ('masa_berlaku_akhir', models.DateField()),
                ('nilai_sewa', models.IntegerField()),
                ('comment', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ukuran',
            fields=[
                ('skpd', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.SKPD')),
                ('panjang_1', models.DecimalField(decimal_places=2, max_digits=3)),
                ('lebar_1', models.DecimalField(decimal_places=2, max_digits=3)),
                ('panjang_2', models.DecimalField(decimal_places=2, max_digits=3)),
                ('lebar_2', models.DecimalField(decimal_places=2, max_digits=3)),
                ('panjang_3', models.DecimalField(decimal_places=2, max_digits=3)),
                ('lebar_3', models.DecimalField(decimal_places=2, max_digits=3)),
                ('panjang_4', models.DecimalField(decimal_places=2, max_digits=3)),
                ('lebar_4', models.DecimalField(decimal_places=2, max_digits=3)),
                ('total', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.AddField(
            model_name='skpd',
            name='atm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ATM', to_field='atm_id'),
        ),
    ]
