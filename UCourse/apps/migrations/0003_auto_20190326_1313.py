# Generated by Django 2.1.7 on 2019-03-26 13:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('apps', '0002_auto_20190324_2140'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('avatar_upload', models.ImageField(upload_to='UserProfile/')),
                ('avatar_link', models.CharField(max_length=255)),
                ('headline', models.CharField(max_length=255)),
                ('biography', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]