# Generated by Django 4.0.4 on 2022-06-04 02:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entidad', models.CharField(max_length=60)),
                ('donado', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('shares', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Themes',
            fields=[
                ('id', models.CharField(default=uuid.UUID('816c0e3b-384c-42c4-9261-d36c61e65eaa'), max_length=100, primary_key=True, serialize=False)),
                ('tema', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.CharField(default=uuid.UUID('080630cd-2cca-4a8a-8633-074095c85e9c'), max_length=100, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('especialidad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('id', models.CharField(default=uuid.UUID('633c52f6-4a2f-4da9-a0c4-208e2174b928'), max_length=100, primary_key=True, serialize=False)),
                ('subtema', models.CharField(max_length=40)),
                ('themes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='BlogLeyes.themes')),
            ],
        ),
    ]
