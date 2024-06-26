# Generated by Django 5.0.6 on 2024-06-10 12:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0003_remove_product_manufactured_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                blank=True,
                help_text="Введите категорию продукта",
                max_length=100,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="products",
                to="product.category",
                verbose_name="Категория",
            ),
        ),
    ]
