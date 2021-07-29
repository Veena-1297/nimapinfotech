# Generated by Django 2.2 on 2021-07-28 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_remove_client_projects'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='decription',
            new_name='description',
        ),
        migrations.AddField(
            model_name='project',
            name='client_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
