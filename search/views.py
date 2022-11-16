from django.shortcuts import render
from realstate.models import Realstate,RealstateImage
# Create your views here.

def search_view(request):
    print('from search')
    query = Realstate.objects.filter(realstate_type='house')
    context = {
        "queryset":query
    }
    template = 'search/result-view.html'
    if request.htmx:
        template = 'search/partials/results.html'
    return render(request,template,context=context)