from PIL import Image
from io import BytesIO

from django.core.files.base import ContentFile
from django.shortcuts import render
from .forms import AddPhoto
from .models import Photo
from .utils import counter

def resize(request, *args, **kwargs):
    '''
    Calculates the image size and creates an object
    '''
    if request.method == 'POST':
        form = AddPhoto(request.POST, request.FILES)
        if form.is_valid():
            photo = request.FILES['photo']
            data = form.cleaned_data
            image = Image.open(photo)
            width, height = image.size
            new_width, new_height = counter(request=request,
                                            width=width,
                                            height=height
                                            )
            image = image.resize((new_width, new_height))
            buffer = BytesIO()
            image.save(fp=buffer, format='webp')
            name = ''.join((data['title'], '_', str(new_width), 'x',
                            str(new_height), '.', data['format'])
                           )
            object = Photo.objects.create(title=name,
                                          format=data['format'],
                                          photo=photo,
                                          width=data['width'],
                                          height=data['height'])
            object.photo_mod.save(name=name,
                                  content=ContentFile(buffer.getvalue()),
                                  save=False
                                  )
            object.save()
            return render(request, 'app/resize.html', {'object': object})
    else:
        form = AddPhoto()
    return render(request, 'app/resize.html', {'form': form})