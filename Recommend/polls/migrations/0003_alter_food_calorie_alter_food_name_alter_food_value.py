# Generated by Django 4.2.7 on 2023-12-17 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20231217_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='calorie',
            field=models.IntegerField(verbose_name='calorie'),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=100, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='food',
            name='value',
            field=models.IntegerField(verbose_name='value'),
        ),
    ]
