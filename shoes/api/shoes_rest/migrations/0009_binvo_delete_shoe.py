# Generated by Django 4.0.3 on 2023-07-22 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes_rest', '0008_remove_shoe_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='BinVO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('closet_name', models.CharField(max_length=100)),
                ('bin_number', models.PositiveSmallIntegerField()),
                ('bin_size', models.PositiveSmallIntegerField()),
                ('bin_href', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Shoe',
        ),
    ]
