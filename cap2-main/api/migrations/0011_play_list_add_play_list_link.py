# Generated by Django 4.1.3 on 2023-04-07 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_play_list_add_name_play_list_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='play_list_add',
            name='Play_list_Link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Play_list_Link', to='api.play_list'),
        ),
    ]
