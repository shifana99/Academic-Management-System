# Generated by Django 5.0 on 2024-01-01 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_master', '0002_designation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualname', models.CharField(max_length=200)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
    ]
