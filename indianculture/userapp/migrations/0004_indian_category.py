# Generated by Django 4.2 on 2024-03-13 02:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0003_rename_image_indian_image1_indian_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='indian',
            name='category',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
