# Generated by Django 3.1.1 on 2020-09-05 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_category_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
