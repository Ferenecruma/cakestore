# Generated by Django 3.0.3 on 2020-08-31 12:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [("webstore", "0001_initial")]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Категорії", "verbose_name_plural": "Категорія"},
        ),
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(
                default=django.utils.timezone.now,
                editable=False,
                max_length=40,
                unique=True,
            ),
            preserve_default=False,
        ),
    ]
