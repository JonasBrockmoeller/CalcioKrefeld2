# Generated by Django 4.2.14 on 2024-07-30 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0002_remove_result_away_ranking_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='club_1',
        ),
        migrations.RemoveField(
            model_name='result',
            name='club_10',
        ),
        migrations.RemoveField(
            model_name='result',
            name='club_11',
        ),
        migrations.RemoveField(
            model_name='result',
            name='club_12',
        ),
        migrations.RemoveField(
            model_name='result',
            name='club_13',
        ),
        migrations.RemoveField(
            model_name='result',
            name='club_14',
        ),
        migrations.RemoveField(
            model_name='result',
            name='club_15',
        ),
        migrations.RemoveField(
            model_name='result',
            name='club_16',
        ),
        migrations.RemoveField(
            model_name='result',
            name='club_17',
        ),
        migrations.RemoveField(
            model_name='result',
            name='club_18',
        ),
        migrations.RemoveField(
            model_name='result',
            name='club_2',
        ),
        migrations.RemoveField(
            model_name='result',
            name='club_3',
        ),
        migrations.RemoveField(
            model_name='result',
            name='club_4',
        ),
        migrations.RemoveField(
            model_name='result',
            name='club_5',
        ),
        migrations.RemoveField(
            model_name='result',
            name='club_6',
        ),
        migrations.RemoveField(
            model_name='result',
            name='club_7',
        ),
        migrations.RemoveField(
            model_name='result',
            name='club_8',
        ),
        migrations.RemoveField(
            model_name='result',
            name='club_9',
        ),
        migrations.RemoveField(
            model_name='result',
            name='type',
        ),
        migrations.AddField(
            model_name='result',
            name='awayranking',
            field=models.JSONField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='homeranking',
            field=models.JSONField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='result',
            name='logoranking',
            field=models.JSONField(default='test'),
            preserve_default=False,
        ),
    ]