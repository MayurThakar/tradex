# Generated by Django 3.2.4 on 2021-06-17 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appUser', '0002_alter_post_updated_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'Posts'},
        ),
    ]