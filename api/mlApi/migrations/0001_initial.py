# Generated by Django 5.0.1 on 2024-01-05 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteTransparencyScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_name', models.CharField(max_length=255, unique=True)),
                ('transparency_score', models.FloatField()),
            ],
        ),
    ]
