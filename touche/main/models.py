from django.db import models


# Create your models here.
class CategoryDish(models.Model):
    name = models.CharField(" Категория", max_length=20, unique=True)
    slug = models.SlugField("URL", unique=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Dish(models.Model):
    title = models.CharField("Название", max_length=20)
    description = models.TextField("Описание")
    cat = models.ForeignKey("CategoryDish", on_delete=models.PROTECT)
    price = models.FloatField("Цена")
    image = models.ImageField("Картинка",upload_to='static/portfolio')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
        ordering = ('title', 'price')


class Contact(models.Model):
    name = models.CharField("Имя", max_length=20)
    email = models.EmailField("Почта")
    message = models.TextField(verbose_name='Сообщение', unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
        ordering = ("name",)
