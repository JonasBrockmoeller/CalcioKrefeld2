# Generated by Django 5.0.7 on 2024-07-27 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_remove_member_id_alter_member_appleid'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.CharField(default='example', max_length=255),
            preserve_default=False,
        ),
    ]