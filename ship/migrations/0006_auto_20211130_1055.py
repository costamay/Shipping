# Generated by Django 3.2.9 on 2021-11-30 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ship', '0005_boat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boat',
            name='price',
        ),
        migrations.RemoveField(
            model_name='boat',
            name='side',
        ),
        migrations.RemoveField(
            model_name='boat',
            name='size',
        ),
        migrations.AddField(
            model_name='boat',
            name='company_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='boat',
            name='name',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='boat',
            name='tone',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
