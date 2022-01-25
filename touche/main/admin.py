from django.contrib import admin
from .models import CategoryDish, Contact,Dish


# Register your models here.

class CategoryDishAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }


class DishAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat', 'price')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')


admin.site.register(CategoryDish)
admin.site.register(Dish)
admin.site.register(Contact)
