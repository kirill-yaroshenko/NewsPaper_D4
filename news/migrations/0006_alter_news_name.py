# Generated by Django 4.1.7 on 2023-03-30 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_news_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]