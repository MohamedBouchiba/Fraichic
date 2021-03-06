# Generated by Django 3.1.1 on 2020-09-17 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=1)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('birthday_date', models.DateField()),
                ('mail_address', models.EmailField(max_length=150)),
                ('address', models.CharField(max_length=150)),
                ('post_code', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
