from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    purpose = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=30, verbose_name="Наименование", help_text="Наименование товара"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Описание товара"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания", help_text="Записи в БД"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения", help_text="Записи в БД")
    photo = models.ImageField(
        upload_to="photo",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите фото товара",
    )
    price_product = models.PositiveIntegerField(
        help_text="Цена товара"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория товара",
        null=True,
        blank=True,
        related_name="products",)



class Meta:
    verbose_name = "Товар"
    verbose_name_plural = "Товары"


def __str__(self):
    return self.name
