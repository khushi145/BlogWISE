# Generated by Django 4.1.5 on 2023-02-01 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
