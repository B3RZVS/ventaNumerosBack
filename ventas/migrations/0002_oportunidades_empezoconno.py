# Generated by Django 4.2 on 2024-10-16 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='oportunidades',
            name='empezoConNo',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
