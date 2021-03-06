# Generated by Django 3.1.1 on 2020-09-17 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20200917_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='number_in_lot',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='products',
            name='unit_of_measure',
            field=models.CharField(choices=[('Kilo', 'Kg'), ('Gramme', 'Gr'), ('Pièces', 'Pièce')], max_length=20),
        ),
    ]
