# Generated by Django 5.1.5 on 2025-01-31 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_about_button_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('position', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='team')),
            ],
        ),
    ]
