# Generated by Django 2.1.7 on 2019-03-30 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_remove_userprofileinfo_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_pic'),
        ),
    ]