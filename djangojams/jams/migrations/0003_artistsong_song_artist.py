# Generated by Django 4.2 on 2023-04-06 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jams', '0002_playlistsong_playlist_songs'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistSong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jams.artist')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jams.song')),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ManyToManyField(through='jams.ArtistSong', to='jams.artist'),
        ),
    ]
