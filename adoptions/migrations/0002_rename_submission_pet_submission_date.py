# Generated by Django 4.0.2 on 2022-02-11 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='submission',
            new_name='submission_date',
        ),
    ]
