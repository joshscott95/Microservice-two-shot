# Generated by Django 4.0.3 on 2023-07-24 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes_rest', '0011_rename_bin_href_binvo_import_href'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoe',
            old_name='color',
            new_name='shoeColor',
        ),
    ]