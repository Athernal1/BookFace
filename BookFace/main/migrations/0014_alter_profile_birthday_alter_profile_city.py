# Generated by Django 4.0.3 on 2022-04-09 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_delete_userfriend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
    ]