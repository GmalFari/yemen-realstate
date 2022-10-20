from django.contrib import admin

from .models import Realstate, RealstateImage

class RsImageInline(admin.StackedInline):
    model = RealstateImage
    extra: 0

class RealstateAdmin(admin.ModelAdmin):
    inlines = [RsImageInline]

# Register your models here.
admin.site.register(Realstate,RealstateAdmin)
admin.site.register(RealstateImage)

