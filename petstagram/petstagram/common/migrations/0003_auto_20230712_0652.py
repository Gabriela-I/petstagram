# Generated by Django 3.2.19 on 2023-07-12 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_alter_photo_photo'),
        ('common', '0002_create_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photocomment',
            name='photo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='photos.photo'),
        ),
        migrations.AlterField(
            model_name='photolike',
            name='photo',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='photos.photo'),
        ),
    ]
