# Generated by Django 3.1.1 on 2020-09-19 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_auto_20200917_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='image_preview',
            field=models.ImageField(blank=True, null=True, upload_to='staticfiles/'),
        ),
    ]