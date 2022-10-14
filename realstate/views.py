from django.urls import reverse
from django.contrib import messages
from django.shortcuts import HttpResponse, HttpResponseRedirect, render

from .forms import ImageRealstateForm, RealstateForm
from .models import Realstate, RealstateImage


# Create your views here.
def homepage_view(request):
    objects = Realstate.objects.all()
    context = {
        "objects":objects,
    }
    return render(request,"realstate/homepage.html",context=context)
def realstate_detail_view(request,id=None):
    try:
        obj = Realstate.objects.get(id=id)
    except:
        obj = None
    if obj is  None:
        return HttpResponse("Not found")
    context = {
        "object":obj,
        "obj_imgs":obj.realstateimage_set.all()
    }
    return render(request,"realstate/rs-detail.html",context=context)

def realstate_create_view(request):
    form = RealstateForm(request.POST or None,request.FILES or None)
    files = request.FILES.getlist('image')
    if form.is_valid()  :
        com_obj = form.save(commit=False)
        com_obj.company = request.user
        com_obj.save()
        for file in files:
            RealstateImage.objects.create(realstate=com_obj,image=file)
        messages.success(request,"New realstate added")    
        return HttpResponseRedirect(reverse("realstate:rs-detail",kwargs={"id":com_obj.id}))
    else:
        print(form.errors)
    images= RealstateImage.objects.all()
    context={
        "form":RealstateForm(),
        "imgsform":ImageRealstateForm(),
        'images': images
    }
    
    return render(request,"realstate/create-rs.html",context=context)
