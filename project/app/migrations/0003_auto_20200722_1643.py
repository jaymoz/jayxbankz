# Generated by Django 2.2.14 on 2020-07-22 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200720_1224'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donation',
            name='full_name',
        ),
        migrations.AddField(
            model_name='donation',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='donation',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='donation',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
