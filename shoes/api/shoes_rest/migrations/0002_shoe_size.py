# Generated by Django 4.0.3 on 2023-07-20 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes_rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoe',
            name='size',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
