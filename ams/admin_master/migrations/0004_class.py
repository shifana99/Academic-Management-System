# Generated by Django 5.0 on 2024-01-01 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_master', '0003_qualification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(max_length=20)),
                ('status', models.IntegerField(default=1)),
            ],
        ),
    ]
