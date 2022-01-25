from django.shortcuts import render
from .models import CategoryDish,Dish,Contact
from  .forms import ContactForm


# Create your views here.

def index(request):
    error = ''
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Неверные данные'
    content = {
        'dishes':Dish.objects.all(),
        'form':ContactForm(),
        'error':error,
        'category': CategoryDish.objects.all(),
        'ads':Contact.objects.all(),


    }
    print(content)
    return render(request, 'main/index.html',content)
