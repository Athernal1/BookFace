# Generated by Django 4.0.3 on 2022-04-09 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_message_userfriend_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserFriend',
        ),
    ]
