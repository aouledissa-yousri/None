# Generated by Django 4.0.1 on 2022-01-31 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starTeractAPI', '0008_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='id',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]