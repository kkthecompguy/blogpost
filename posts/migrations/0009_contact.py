# Generated by Django 3.0.4 on 2020-04-03 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_anonymousview'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
