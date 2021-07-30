# Generated by Django 3.1.2 on 2021-01-04 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20201221_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_image', models.ImageField(blank=True, upload_to='slider_image/', verbose_name='Slider Image')),
                ('caption1', models.CharField(max_length=500, verbose_name='Caption')),
                ('caption2', models.CharField(max_length=500, verbose_name='Caption')),
                ('description', models.CharField(max_length=500, verbose_name='Description')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Slider Image',
                'verbose_name_plural': 'Slider Images',
            },
        ),
    ]