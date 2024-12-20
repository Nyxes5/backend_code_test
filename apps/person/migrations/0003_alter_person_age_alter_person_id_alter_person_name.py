# Generated by Django 5.1.2 on 2024-11-01 14:40

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_alter_person_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.PositiveIntegerField(help_text="The person's age in years, as a positive integer. Must be 18+."),
        ),
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='A unique identifier for each Person instance, generated automatically.', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(help_text="The person's name. Must be unique.", max_length=255, unique=True),
        ),
    ]
