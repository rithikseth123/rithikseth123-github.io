# Generated by Django 4.2.5 on 2023-10-28 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=True, max_length=100),
        ),
    ]
