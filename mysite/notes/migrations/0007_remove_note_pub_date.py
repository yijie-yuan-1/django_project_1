# Generated by Django 2.2.6 on 2019-10-15 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0006_note_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='pub_date',
        ),
    ]