# Generated by Django 2.2 on 2020-02-22 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exam_app', '0004_auto_20200221_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='end',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start',
            field=models.DateField(),
        ),
    ]
