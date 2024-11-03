# Generated by Django 5.1.2 on 2024-11-03 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_alter_person_age_alter_person_id_alter_person_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(help_text="The person's name. Must be unique.", max_length=255),
        ),
    ]