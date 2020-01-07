from django.shortcuts import get_object_or_404,redirect,render
from .models import Image
from django.contrib import messages
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import ImageForm

# Create your views here.
def index(request):
    if request.method == "POST":
        updata = request.FILES['image']
        form = ImageForm(request.POST, request.FILES)
        if updata != None:
            fs = FileSystemStorage()
            filename = fs.save(updata.name, updata)
            uploaded_file_url = fs.url(filename)
            img = form.save(commit = False)
            # img = Image()
            img.image_f = uploaded_file_url
            print("uploaded_file_url:",uploaded_file_url)
            print("image_f:",img.image_f)
            print("title:",img.title)
            img.save()
            images = Image.objects.all().order_by("-created_at")
        return render(request, 'app/index.html', {'images':images,'form':form})
    else:
        images = Image.objects.all().order_by("-created_at")
        form = ImageForm()
        return render(request, 'app/index.html', {'images':images,'form':form})

def images_detail(request,pk):
    image = get_object_or_404(Image,pk=pk)
    return render(request,'app/images_detail.html', {'image':image})

def images_delete(request,pk):
    form = ImageForm()
    images = Image.objects.all().order_by("-created_at")
    image = get_object_or_404(Image,pk=pk)
    image.delete()
    return render(request, 'app/index.html', {'images':images,'form':form})
    # return redirect('app:users_detail',request.user.id)
