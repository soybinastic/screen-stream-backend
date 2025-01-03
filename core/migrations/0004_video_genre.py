# Generated by Django 4.2.16 on 2024-11-25 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_video_video_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='genre',
            field=models.CharField(choices=[('ACTION', 'Action'), ('COMEDY', 'Comedy'), ('DRAMA', 'Drama'), ('HORROR', 'Horror'), ('SCIFI', 'Science Fiction'), ('DOCUMENTARY', 'Documentary')], default='ACTION', max_length=50),
            preserve_default=False,
        ),
    ]
