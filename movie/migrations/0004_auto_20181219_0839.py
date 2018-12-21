# Generated by Django 2.1.4 on 2018-12-19 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20181219_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActorTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100, verbose_name='role')),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actor', related_query_name='actor', to='movie.Actor', verbose_name='actor')),
            ],
        ),
        migrations.RemoveField(
            model_name='actormovietable',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='actormovietable',
            name='movie',
        ),
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='actors', related_query_name='actors', through='movie.ActorTable', to='movie.Actor', verbose_name='actors'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tags',
            field=models.ManyToManyField(related_name='tags', related_query_name='tags', to='movie.Tag', verbose_name='tags'),
        ),
        migrations.DeleteModel(
            name='ActorMovieTable',
        ),
        migrations.AddField(
            model_name='actortable',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie', related_query_name='movie', to='movie.Movie', verbose_name='movie'),
        ),
    ]