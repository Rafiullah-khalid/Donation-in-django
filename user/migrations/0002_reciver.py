# Generated by Django 4.1.2 on 2022-10-11 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reciver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('f_name', models.CharField(max_length=30)),
                ('taskera', models.CharField(max_length=40)),
                ('cantact', models.CharField(max_length=30, null=True)),
                ('address', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
