# Generated by Django 4.2.4 on 2023-09-08 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news1', '0007_alter_news1_photographer_alter_news1_reporter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news1',
            name='reporter',
            field=models.ForeignKey(default=40, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]