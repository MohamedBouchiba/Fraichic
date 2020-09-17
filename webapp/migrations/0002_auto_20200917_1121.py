# Generated by Django 3.1.1 on 2020-09-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Fruits', 'Fruits'), ('Légumes', 'Légumes')], max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('unit_of_measure', models.CharField(choices=[('Fruits', 'Fruits'), ('Légumes', 'Légumes')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Masculin', 'M'), ('Féminin', 'F')], max_length=20),
        ),
    ]