from PIL import Image
from io import BytesIO

from django.core.files.base import ContentFile
from django.shortcuts import render
from .forms import AddPhoto
from .models import Photo


def resize(request, *args, **kwargs):
    if request.method == 'POST':
        form = AddPhoto(request.POST, request.FILES)
        if form.is_valid():
            photo = request.FILES['photo']
            data = form.cleaned_data
            image = Image.open(photo)
            width, height = image.size
            if width > height:
                new_width = 150
                new_height = new_width * height // width
            else:
                new_height = 150
                new_width = new_height * width // height
            image = image.resize((new_width, new_height))
            buffer = BytesIO()
            image.save(fp=buffer, format='webp')
            name = ''.join((data['title'], '_', str(new_width), 'x', str(new_height), '.', data['format']))
            object = Photo.objects.create(title=name,
                                          format=data['format'],
                                          photo=photo,
                                          width=data['width'],
                                          height=data['height'])
            object.photo_mod.save(name=name, content=ContentFile(buffer.getvalue()), save=False)
            object.save()
            return render(request, 'app/resize.html', {'object': object})
    else:
        form = AddPhoto()
    return render(request, 'app/resize.html', {'form': form})