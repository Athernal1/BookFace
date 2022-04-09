# Generated by Django 4.0.3 on 2022-04-08 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_rename_post_blogpost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='user',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
