from django.shortcuts import render,redirect

from home.models import GalleryModel

from . forms import GalleryForm

# Create your views here.

def index(request):
    return render(request,'index.html')

def home (request):
    data = GalleryModel.objects.all()
    return render(request,'home.html',{'data':data})

def addtogallery (request):
    if request.method == "POST":
        form = GalleryForm(request.POST or None , request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(request,'home')
    else:
        form = GalleryForm()
    return render(request,'addtogallery.html',{'form':form})

def details(request,id):
    data = GalleryModel.objects.get(id=id)

    return render(request,'details.html',{'data':data})