# Generated by Django 2.1.4 on 2018-12-17 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='body')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='post time')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.WXUser', verbose_name='author')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie', verbose_name='commented post')),
            ],
        ),
    ]
