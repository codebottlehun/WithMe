# Generated by Django 4.0 on 2022-05-09 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletin', '0002_post_reply_delete_bulletinfeed'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
