# Generated by Django 4.2.2 on 2023-07-18 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.TextField(max_length=30)),
                ('posted', models.DateField()),
                ('content', models.TextField()),
                ('user_name', models.TextField()),
            ],
        ),
    ]
