# Generated by Django 4.1.3 on 2022-11-06 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]