# Generated by Django 4.0.6 on 2022-07-28 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiares',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('relationship', models.CharField(max_length=40)),
                ('sys_creation_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]