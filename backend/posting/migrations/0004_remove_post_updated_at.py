# Generated by Django 4.1.1 on 2022-09-07 06:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("posting", "0003_rename_passworrd_post_password"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="updated_at",
        ),
    ]
