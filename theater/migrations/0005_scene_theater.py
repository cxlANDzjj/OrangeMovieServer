# Generated by Django 2.1.4 on 2018-12-19 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0004_remove_scene_theater'),
    ]

    operations = [
        migrations.AddField(
            model_name='scene',
            name='theater',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='theater.Theater', verbose_name='theater'),
            preserve_default=False,
        ),
    ]
