# Generated by Django 4.2.2 on 2023-07-28 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
                ('short_description', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='message',
            name='full_name',
            field=models.CharField(max_length=50),
        ),
    ]
