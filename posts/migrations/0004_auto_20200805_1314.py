# Generated by Django 3.1 on 2020-08-05 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_comment_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='message',
            new_name='comment',
        ),
    ]
