# Generated by Django 2.1.12 on 2022-10-03 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressmodel',
            name='state',
            field=models.CharField(default='VIC', max_length=3),
        ),
    ]