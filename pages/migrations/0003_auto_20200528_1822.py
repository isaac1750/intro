# Generated by Django 2.2.12 on 2020-05-29 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(),
        ),
    ]