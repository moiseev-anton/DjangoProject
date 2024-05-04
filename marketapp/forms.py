from django import forms
from .models import Product


# задание 6
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'date_added']


# задание 7
class ImageUploadForm(forms.Form):
    image = forms.ImageField()
