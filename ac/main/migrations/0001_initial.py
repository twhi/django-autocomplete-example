# Generated by Django 2.2.7 on 2019-11-12 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(default='', max_length=100)),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
