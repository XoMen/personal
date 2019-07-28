# Generated by Django 2.2.3 on 2019-07-22 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0006_auto_20190718_1541'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='Unknown', max_length=40)),
                ('Title', models.CharField(default='No Title was added right', max_length=80)),
                ('Message', models.TextField(blank=True, default='This Post have not any desription !!!')),
                ('Image', models.FileField(blank=True, null=True, upload_to='static/Posts/Img/')),
                ('DateCreate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]