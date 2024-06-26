# Generated by Django 5.0.4 on 2024-05-16 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0007_fiche_liste_fiche_item_list_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='content_id',
        ),
        migrations.RemoveField(
            model_name='document',
            name='date',
        ),
        migrations.RemoveField(
            model_name='document',
            name='group_id',
        ),
        migrations.AddField(
            model_name='document',
            name='content',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
