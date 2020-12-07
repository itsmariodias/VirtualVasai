from django.shortcuts import render
from django.views import View
from django.conf import settings
from places.models import Region, Place, Comment
from django.db.models import Avg, Case, When
# Create your views here.

# This is a little complex because we need to detect when we are
# running in various configurations


class HomeView(View):
    def get(self, request):
        print(request.get_host())
        host = request.get_host()
        top_places = Comment.objects.filter(status='True').values('place_id').annotate(average=Avg('rate')).order_by('-average').values('place_id')
        preserved = Case(*[When(id=place['place_id'], then=pos) for pos, place in enumerate(top_places)])
        place_list = Place.objects.filter(id__in=top_places).order_by(preserved)[:3]
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed': settings.INSTALLED_APPS,
            'islocal': islocal,
            'place_list' : place_list
        }

        return render(request, 'home/main.html', context)

class AboutView(View):
    def get(self, request):
        return render(request, 'home/about.html')

class RegionView(View):
    def get(self, request):
        region_list = Region.objects.all()
        ctx = {'region_list' : region_list}
        return render(request, 'home/region.html', ctx)
