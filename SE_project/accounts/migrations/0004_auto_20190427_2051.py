# Generated by Django 2.1.7 on 2019-04-27 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20190424_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='contact_of_reference',
            field=models.PositiveIntegerField(),
        ),
    ]
