from django.db import models
from django.conf import settings
from django.db.models.signals import post_save, pre_save
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

# Create your models here.
User = settings.AUTH_USER_MODEL
class Profile(models.Model):
    user = models.OneToOneField(User,verbose_name=_("user"),on_delete=models.CASCADE)
    slug = models.SlugField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True)
    address= models.CharField(max_length=50)
    join_date = models.DateTimeField(auto_now=True)

    def save(self,*args,**kwargs):
        if  self.slug is None:
            self.slug = slugify(self.user.username)
        super().save(*args,**kwargs)
    class Meta:
        verbose_name=_("profile")
        verbose_name_plural = _("Profiles")
    def __str__(self):
        return self.user.username
    def get_absolute_url(self):
         return reverse('accounts:profile',kwargs={'slug':self.slug})


def get_profile(instance ,new_profile,save=False):
    pass
def create_profile(sender,instance,created,*args,**kwargs):
    
    if created:
        user_profile = Profile.objects.create(user=instance)


   
post_save.connect(create_profile,sender=User)