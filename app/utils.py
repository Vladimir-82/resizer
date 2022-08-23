def counter(request, width, height):
    '''
    Сounts image size
    '''
    if request.POST['width'] and request.POST['height']:
        new_width, new_height = int(request.POST['width']), int(request.POST['height'])
    elif request.POST['width']:
        new_width = int(request.POST['width'])
        new_height = int((new_width / int(width)) * int(height))
    else:
        new_height = int(request.POST['height'])
        new_width = int((new_height / int(height)) * int(width))
    return new_width, new_height