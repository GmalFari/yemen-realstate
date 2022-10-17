from tkinter import Image
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from .forms import ImageRealstateForm, RealstateForm
from .models import Realstate, RealstateImage
from .filter import Rsfilter

# Create your views here.


@login_required
def list_view(request):
    list_rs = Realstate.objects.filter(company=request.user)
    context={
        "list_rs":list_rs,
    }
    return render(request,"realstate/list.html",context=context)

@login_required
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
@login_required
def rs_update_view(request,id=None):
    try:
        obj = Realstate.objects.get(id=id)
    except:
        obj = None
    if obj is None:
        return HttpResponse("not found")
    
    form = RealstateForm(request.POST or None, instance=obj)
    RealstateImageFormset = modelformset_factory(RealstateImage,form=ImageRealstateForm,extra=0)
    rs_imgs_qs = obj.realstateimage_set.all() #[]
    formset = RealstateImageFormset(request.POST or None , queryset=rs_imgs_qs)
    context = {
        "form":form,
        "formset":formset,
        "obj":obj,
    }
    if all([form.is_valid(),formset.is_valid()]):
        parent = form.save(commit=False)
        parent.save()
        for f in formset:
            child = f.save(commit=False)
            if child.realstate is None:
                child.realstate = parent
            child.save()
            print("updated data.")
            context['message'] = "updated data."
    if request.htmx:
        return render(request,"realstate/partials/forms.html")     
    return render(request,"realstate/rs-update.html",context=context)


# global scope
def homepage_view(request):
    objects = Realstate.objects.all()
    myfilter = Rsfilter(request.GET,queryset=objects)
    all_rs  = myfilter.qs
    context = {
        "objects":all_rs,
        "myfilter":myfilter,
        "rental_rs":Realstate.objects.filter(offer_type="for_rent")
    }
    return render(request,"realstate/homepage.html",context=context)
def realstate_detail_view(request,id=None):
    hx_url = reverse("realstate:hx-rs-detail",kwargs={"id":id})
    context = {
        "hx_url":hx_url,
    }
    return render(request,"realstate/rs-detail.html",context=context)

def realstate_hx_detail_view(request,id=None):
    try:
        obj = Realstate.objects.get(id=id)
    except:
        obj = None
    if obj is  None:
        return HttpResponse("Not found")
    context = {
        "object":obj,
    }
    return render(request,"realstate/partials/rs-detail.html",context=context)