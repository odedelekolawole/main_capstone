# Generated by Django 4.2.4 on 2023-08-26 20:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=500)),
                ('tagline', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Category1',
            },
        ),
        migrations.CreateModel(
            name='Continent1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Continent1',
            },
        ),
        migrations.CreateModel(
            name='News1',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('headline', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='images')),
                ('region', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news1.category1')),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news1.continent1')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'News1',
            },
        ),
    ]
