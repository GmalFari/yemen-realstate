from tkinter import Image
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponse,Http404
from django.shortcuts import HttpResponseRedirect, render
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
        obj = Realstate.objects.get(id=id,company=request.user)
    except:
        obj = None
    if obj is None:
        return HttpResponse("not found")
    form = RealstateForm(request.POST or None,request.FILES or None, instance=obj)
    new_image_url = reverse("realstate:hx-images-new",kwargs={"parent_id":obj.id})
    context = {
        "form":form,
        "object":obj,
        "new_image_url":new_image_url,
    }
    if form.is_valid():
        form.save()
        context['message'] = "updated data."
    if request.htmx:
        return render(request,"realstate/partials/forms.html",context=context)     
    return render(request,"realstate/rs-update.html",context=context)
@login_required
def realstate_imgs_hx_detail_view(request,parent_id=None,id=None):
    if not request.htmx:
        return HttpResponse("Not found")
    try:
        parent_obj = Realstate.objects.get(id=parent_id)
    except:
        parent_obj = None
    if parent_obj is  None:
        return HttpResponse(" parent Not found")
    instance = None
    if id is not None:
        try:
            instance = RealstateImage.objects.get(realstate=parent_obj,id=id)
        except:
            instance = None
    form = ImageRealstateForm(request.POST or None, request.FILES or None , instance=instance)
    url = instance.get_hx_edit_url() if instance else reverse("realstate:hx-images-new",kwargs={"parent_id":parent_obj.id})
    context = {
        "url":url,
        "form":form,
        "object":instance,
    }
    files = request.FILES.getlist('image')
    if form.is_valid():
        for file in files:
            new_obj = RealstateImage.objects.create(realstate=parent_obj,image=file)
        context['object'] = new_obj  
        messages.success(request,"New realstate added")    
        return render(request,"realstate/partials/images-inline.html",context=context)
    return render(request,"realstate/partials/images-form.html",context=context)
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
    if not request.htmx:
        return HttpResponse("Not found")
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