# Generated by Django 4.2.3 on 2023-07-27 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum', models.IntegerField()),
                ('status', models.CharField(max_length=120)),
                ('order_id', models.CharField(max_length=120)),
            ],
        ),
    ]