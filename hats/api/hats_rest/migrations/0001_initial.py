# Generated by Django 4.0.3 on 2023-07-19 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabric', models.CharField(max_length=255)),
                ('style_name', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('picture_url', models.URLField()),
            ],
            options={
                'ordering': ('style_name',),
            },
        ),
    ]