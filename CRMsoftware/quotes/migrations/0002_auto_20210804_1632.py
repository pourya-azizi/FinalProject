# Generated by Django 3.2.5 on 2021-08-04 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quoteitem',
            name='tax',
            field=models.FloatField(default=5),
        ),
        migrations.AlterField(
            model_name='quoteitem',
            name='qty',
            field=models.PositiveIntegerField(default=1),
        ),
    ]