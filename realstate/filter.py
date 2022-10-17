import django_filters

from .models import Realstate

class Rsfilter(django_filters.FilterSet):
    class Meta:
        model = Realstate
        fileds = '__all__'
        exclude = ['main_img','phone']