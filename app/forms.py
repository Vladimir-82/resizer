from .models import Photo
from django import forms


class AddPhoto(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'format', 'photo', 'width', 'height']
        help_texts ='sss'