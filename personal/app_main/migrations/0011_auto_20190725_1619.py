# Generated by Django 2.2.3 on 2019-07-25 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0010_auto_20190725_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pythoncourse',
            name='Name',
        ),
        migrations.AddField(
            model_name='pythoncourse',
            name='Session',
            field=models.IntegerField(default='0'),
        ),
        migrations.AlterField(
            model_name='post',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='pythoncourse',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]