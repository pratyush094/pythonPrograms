# Generated by Django 2.1.5 on 2019-02-14 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bloodbank', '0002_statecity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statecity',
            name='id',
        ),
        migrations.AlterField(
            model_name='statecity',
            name='city',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
