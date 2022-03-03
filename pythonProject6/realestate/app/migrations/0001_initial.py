# Generated by Django 3.2.3 on 2021-05-17 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=15)),
                ('lastname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=30)),
                ('confirmpassword', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=20)),
            ],
            options={
                'db_table': 'user_table',
            },
        ),
    ]
