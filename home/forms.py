from . models import GalleryModel
from django import forms

class GalleryForm(forms.ModelForm):
    class Meta():
        model = GalleryModel
        fields = '__all__'