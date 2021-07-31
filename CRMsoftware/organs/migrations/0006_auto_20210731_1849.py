# Generated by Django 3.2.5 on 2021-07-31 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organs', '0005_auto_20210731_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='organization',
            name='organization_product',
            field=models.ManyToManyField(to='organs.OrganizationProduct'),
        ),
    ]
