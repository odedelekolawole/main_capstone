# Generated by Django 4.2.4 on 2023-09-12 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news2', '0008_rename_title_breakingnews_content'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BreakingNews',
        ),
    ]