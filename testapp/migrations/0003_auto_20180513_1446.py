# Generated by Django 2.0.5 on 2018-05-13 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_auto_20180513_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reklama_in_efir',
            name='id_efir',
        ),
        migrations.RemoveField(
            model_name='reklama_in_efir',
            name='id_reklama',
        ),
        migrations.RemoveField(
            model_name='sotrudnik_in_efir',
            name='id_efir',
        ),
        migrations.RemoveField(
            model_name='sotrudnik_in_efir',
            name='id_sotrudnik',
        ),
        migrations.DeleteModel(
            name='Reklama_in_efir',
        ),
        migrations.DeleteModel(
            name='Sotrudnik_in_efir',
        ),
    ]
