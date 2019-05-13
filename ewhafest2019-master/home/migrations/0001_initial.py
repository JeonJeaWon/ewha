# Generated by Django 2.2.1 on 2019-05-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.IntegerField()),
                ('place', models.CharField(max_length=20)),
                ('booth_num', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('sold_out', models.IntegerField()),
                ('password', models.IntegerField()),
                ('detail', models.TextField()),
            ],
        ),
    ]