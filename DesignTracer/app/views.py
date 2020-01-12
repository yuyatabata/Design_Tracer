from django.shortcuts import get_object_or_404,redirect,render
from .models import Image
from django.contrib import messages
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import ImageForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

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
            img.user = request.user
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

def users_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    images = Image.objects.all().order_by("-created_at")
    return render(request, 'app/mypage.html', {'user':user, 'images':images})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            input_username = form.cleaned_data['username']
            input_password = form.cleaned_data['password1']
            new_user = authenticate(username=input_username, password=input_password)
            if new_user is not None:
                login(request, new_user)
                return redirect('app:users_detail', pk=new_user.pk)
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', {'form':form})
