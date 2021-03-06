# Generated by Django 3.0.3 on 2020-09-02 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("webstore", "0006_product_photo")]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="photo",
            field=models.ImageField(upload_to="products"),
        ),
        migrations.CreateModel(
            name="SubCategory",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, unique=True)),
                ("slug", models.SlugField(editable=False, max_length=40)),
                ("description", models.TextField()),
                ("photo", models.ImageField(upload_to="sub_categories")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="webstore.Category",
                    ),
                ),
            ],
            options={
                "verbose_name": "Підкатегорія",
                "verbose_name_plural": "Підкатегорії",
            },
        ),
    ]
