# Generated by Django 2.0 on 2018-09-27 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0046_require_sponsor_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='population',
            field=models.IntegerField(default=0, help_text='Population'),
        ),
    ]
