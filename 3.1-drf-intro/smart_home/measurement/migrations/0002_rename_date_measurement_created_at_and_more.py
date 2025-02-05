# Generated by Django 5.0.4 on 2024-05-02 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='date',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
