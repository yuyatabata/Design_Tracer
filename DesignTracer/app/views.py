from django.shortcuts import get_object_or_404,redirect,render
from .models import Image
from django.contrib import messages
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
def index(request):
    if request.method == "POST":
        updata = request.FILES['image']
        if updata != None:
            fs = FileSystemStorage()
            filename = fs.save(updata.name, updata)
            uploaded_file_url = fs.url(filename)
            img = Image()
            img.image_f = uploaded_file_url
            img.save()
            images = Image.objects.all().order_by("-created_at")
        return render(request, 'index.html', {'images':images})
    else:
        images = Image.objects.all().order_by("-created_at")
        return render(request, 'index.html', {'images':images})