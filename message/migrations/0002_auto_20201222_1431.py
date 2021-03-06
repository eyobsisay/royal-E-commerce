# Generated by Django 3.1.2 on 2020-12-22 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscrib',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
            options={
                'verbose_name': 'subscrib',
                'verbose_name_plural': 'SUBSCRIB',
            },
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='email',
            field=models.EmailField(blank=True, max_length=50),
        ),
    ]
