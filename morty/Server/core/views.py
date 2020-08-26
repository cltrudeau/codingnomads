from django.shortcuts import render
from core.models import ImageData


def all_images(request):
    data = {
        'title':'Rick &amp; Morty Images',
        'images':ImageData.objects.all(),
    }

    return render(request, 'image_list.html', data)


def single_image(request, image_id):
    data = {
        'title':'A Particular Rick &amp; Morty Image',
        'images':[ImageData.objects.get(id=image_id), ]
    }

    return render(request, 'image_list.html', data)
