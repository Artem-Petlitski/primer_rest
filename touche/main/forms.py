from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'id': "name", 'class': "form-control", 'placeholder': "Имя", 'required': "required"}),
            'email':forms.TextInput(attrs={'id': "email", 'class': "form-control", 'placeholder': "Почта", 'required': "required"}),
            'message':forms.Textarea(attrs={'id': "message", 'class': "form-control", 'placeholder': "Сообщение", 'required': "required",'rows':"4"})
        }
