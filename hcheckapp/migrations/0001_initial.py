# Generated by Django 4.2.5 on 2024-08-08 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='healthdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('containerd', models.CharField(max_length=10)),
                ('apache2', models.CharField(max_length=10)),
                ('mysql', models.CharField(max_length=10)),
                ('mongod', models.CharField(max_length=10)),
                ('gpumanager', models.CharField(max_length=10)),
                ('firewalld', models.CharField(max_length=10)),
                ('docker', models.CharField(max_length=10)),
            ],
        ),
    ]
