# Generated by Django 3.1 on 2020-08-31 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afringa', '0003_audio_audiofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Audio',
        ),
        migrations.AddField(
            model_name='video',
            name='audio',
            field=models.FileField(null=True, upload_to='audio/', verbose_name=''),
        ),
    ]
