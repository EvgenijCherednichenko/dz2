# Generated by Django 5.0.6 on 2024-05-29 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="manufactured_at",
            field=models.DateField(
                auto_now=True, verbose_name="Дата производства продукта"
            ),
        ),
    ]