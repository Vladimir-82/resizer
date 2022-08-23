from .models import Photo
from django import forms


class AddPhoto(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'format', 'photo', 'width', 'height']
        help_texts = {'format': "PNG/JPEG/GIF/RAW/TIFF/BMP/PSD",
                      'width': "You can choose one of the options or two",
                      'height': "You can choose one of the options or two"
                      }