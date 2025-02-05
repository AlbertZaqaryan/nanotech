# Generated by Django 5.1.5 on 2025-01-31 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_slider_delete_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Contact name')),
                ('email', models.EmailField(max_length=254, verbose_name='Contact email')),
                ('text', models.TextField(verbose_name='Contact text')),
            ],
        ),
    ]
