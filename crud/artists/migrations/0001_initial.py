# Generated by Django 3.1.7 on 2021-02-25 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('duration', models.DecimalField(decimal_places=2, max_digits=100000)),
                ('spotify_published', models.BooleanField(null=True)),
                ('youtube_published', models.BooleanField(null=True)),
                ('foreign_key', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='artists.artist')),
            ],
        ),
    ]
