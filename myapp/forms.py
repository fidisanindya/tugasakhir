from django import forms
from .models import Book, Detection

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'cover_image']
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

class DetectionForm(forms.ModelForm):
    class Meta:
        model = Detection
        fields = ['name', 'phone', 'email', 'address', 'image']
