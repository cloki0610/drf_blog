# Generated by Django 4.2.2 on 2023-06-11 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_body',
            new_name='content',
        ),
    ]