import pathlib
import uuid
from django.urls import reverse
from django.db.models import Q
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from .utils import path_file_name , img_file_name
# Create your models here.
"""
-global
    realstate 

    pictures
-user

    realstate 
    pictures

company 
alternatives

additional info if was dept or building or land 

"""
class RealstateQuerySet(models.QuerySet):
    def search(self,query=None):
        if query is None or query=="":
            return self.none()
        lookups =( Q(realstate_title__icontains=query) 
        )
        return self.filter(lookups)

class RealstateManager(models.Manager):
    def get_queryset(self):
        return RealstateQuerySet(self.model,using=self._db)
    def search(self,query=None):
        return self.get_queryset().search(query=query)

class Realstate(models.Model):
    offer_choices = [
        ('for_rent','for rent'),
        ('for_sale','for sale')
    ]
    ownership_choices = [
        ('free','free'),
        ('waqf','waqf')
    ]
    type_choices = [
        ('dept','department'),
        ('house','house'),
        ('land','land'),
        ('basement','basement'),

    ]
    town_choices = [
        ('sanaa',"sana'a"),
        ('Dhamar','Dhamar'),
        ("Taiz","Taiz")
    ]
    company = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True)
    realstate_title = models.CharField(max_length=50)
    main_img = models.ImageField(upload_to=path_file_name,null=True,blank=True)
    offer_type = models.CharField(max_length=20,choices=offer_choices,null=True,blank=True) # للبيع للإيجار
    realstate_type= models.CharField(max_length=50,choices=type_choices,null=True,blank=True)# شقق عمارة أرضية 
    ownership_type = models.CharField(max_length=20,choices=ownership_choices,null=True,blank=True) #وقف أو حر 
    realstate_description = models.TextField(null=True,blank=True)
    realstate_town = models.CharField(max_length=50,choices=town_choices,null=True,blank=True)# المدينة
    realstate_area = models.CharField(max_length=50,null=True,blank=True) # المنطقة
    realstate_price = models.IntegerField(null=True,blank=True)
    is_negotiable = models.BooleanField(null=True,blank=True)# قابلية التفاوض
    phone = models.CharField(max_length=50,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    objects = RealstateManager() # for search 
    
    @property
    def name(self):
        return self.realstate_title
    def get_absolute_url(self):
        return reverse("realstate:rs-detail",kwargs={"id":self.id})
    def get_delete_url(self):
        return reverse("realstate:delete",kwargs={"id":self.id})
    def get_update_url(self):
        return reverse("realstate:rs-update",kwargs={"id":self.id})
    def get_hx_url(self):
        return reverse("realstate:hx-rs-detail",kwargs={"id":self.id})
    def get_child_images(self):
        return self.realstateimage_set.all()
    def __str__(self):
        return self.realstate_title
    @property
    def imageURL(self):
        try:
            url = self.main_img.url
        except:
            url='/media/image2.jpeg'
        return url
    class Meta:
        verbose_name = _("Realstate")
        verbose_name_plural = _("Realstates")



class RealstateImage(models.Model):
    realstate= models.ForeignKey(Realstate,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=img_file_name)
    
    def get_absolute_url(self):
        return self.realstate.name
    
    def get_delete_url(self):
        kwargs = {
            "parent_id":self.realstate.id,
            "id":self.id
            }
        return reverse("realstate:images-delete",kwargs=kwargs)
        
    def get_hx_edit_url(self):
        kwargs = {
            "parent_id":self.realstate.id,
            "id":self.id
            }
        return reverse("realstate:hx-images-update",kwargs=kwargs)

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")
    

