# Generated by Django 2.0.5 on 2018-05-13 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_auto_20180513_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reklama_in_efir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_efir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Efir')),
                ('id_reklama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Reklama')),
            ],
        ),
    ]
