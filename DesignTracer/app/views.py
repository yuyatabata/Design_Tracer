from django.shortcuts import get_object_or_404,redirect,render
from .models import Image
from django.contrib import messages
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.dispatch import receiver

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
            print("uploaded_file_url:",uploaded_file_url)
            print("image_f:",img.image_f)
            img.save()
            images = Image.objects.all().order_by("-created_at")
        return render(request, 'app/index.html', {'images':images})
    else:
        images = Image.objects.all().order_by("-created_at")
        return render(request, 'app/index.html', {'images':images})

def images_detail(request,pk):
    image = get_object_or_404(Image,pk=pk)
    return render(request,'app/images_detail.html', {'image':image})

def images_delete(request,pk):
    image = get_object_or_404(Image,pk=pk)
    image.delete()
    return render(request, 'app/index.html', {'images':images})
    # return redirect('app:users_detail',request.user.id)

# @receiver(images_delete, sender)
# def delete_file(sender, instance, **kwargs):
#     instance.file_field.delete(False)
