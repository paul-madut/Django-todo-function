# Generated by Django 4.2.7 on 2023-12-02 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_remove_todo_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ['title']},
        ),
    ]