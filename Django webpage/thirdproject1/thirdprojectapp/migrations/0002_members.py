# Generated by Django 4.1.3 on 2022-11-16 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thirdprojectapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
    ]
