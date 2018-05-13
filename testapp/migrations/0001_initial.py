# Generated by Django 2.0.5 on 2018-05-13 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dolznost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dolznost_name', models.CharField(max_length=255, unique=True)),
                ('oklad', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Efir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_efir', models.DateTimeField(unique=True)),
                ('stop_efir', models.DateTimeField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Peredacha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peredacha_name', models.CharField(max_length=255, unique=True)),
                ('rek_stoim_for_min', models.FloatField(max_length=10)),
                ('rating', models.FloatField(max_length=10)),
                ('studiya', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reklama',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reklama_name', models.CharField(max_length=255, unique=True)),
                ('rekvesit', models.CharField(max_length=255)),
                ('mail', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Reklama_in_efir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_efir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Efir')),
                ('id_reklama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Reklama')),
            ],
        ),
        migrations.CreateModel(
            name='Sotrudnik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fam', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('otchestvo', models.CharField(max_length=255)),
                ('kard_number', models.CharField(max_length=255)),
                ('otdel', models.IntegerField()),
                ('passport_number', models.CharField(max_length=255)),
                ('data_priom', models.DateField()),
                ('id_dolznost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Dolznost')),
            ],
        ),
        migrations.CreateModel(
            name='Sotrudnik_in_efir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_efir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Efir')),
                ('id_sotrudnik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Sotrudnik')),
            ],
        ),
        migrations.AddField(
            model_name='efir',
            name='id_peredacha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Peredacha'),
        ),
    ]
