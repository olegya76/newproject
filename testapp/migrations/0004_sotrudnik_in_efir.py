# Generated by Django 2.0.5 on 2018-05-13 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20180513_1446'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sotrudnik_in_efir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('efir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Efir')),
                ('sotrudnik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.Sotrudnik')),
            ],
        ),
    ]
