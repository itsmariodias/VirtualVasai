from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from places.models import Place, Category, Image, Comment, Region
from places.forms import PlaceModelForm, ImageModelForm, CommentForm
from places.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from places.utils import dump_queries
from django.db.models import Q
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db.utils import IntegrityError

from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
class PlaceListView(OwnerListView):
    model = Place
    # By convention:
    template_name = "places/place_list.html"

    def get(self, request) :
        place_list = Place.objects.all()
        region_list = Region.objects.all()
        category_list = Category.objects.all()

        strval =  request.GET.get("search", False)
        strrate =  request.GET.get("searchByRating", False)
        strcat = request.GET.getlist("searchByCategory", False)
        strreg = request.GET.getlist("searchByRegion", False)
        if strrate :
            #Rating filter
            ids = [place.id for place in place_list if place.averagereview() >= float(strrate)]
            place_list = place_list.filter(id__in=ids)

        if strcat :
            # Category checkbox filter

            #First get the corresponding id's from table and convert to list
            category_id_list = Category.objects.filter(name__in=strcat).values_list('pk', flat=True)

            #then check the respective ids in the place table
            place_list = place_list.filter(category_id__in=category_id_list)
        if strreg :
            # Region checkbox filter

            #First get the corresponding id's from table and convert to list
            region_id_list = Region.objects.filter(name__in=strreg).values_list('pk', flat=True)

            #then check the respective ids in the place table
            place_list = place_list.filter(region_id__in=region_id_list)
        if strval :
            # Simple title-only search
            # objects = Post.objects.filter(title__contains=strval).select_related().order_by('-updated_at')[:10]

            # Multi-field search
            query = Q(title__icontains=strval)
            query.add(Q(description__icontains=strval), Q.OR)
            query.add(Q(address__icontains=strval), Q.OR)
            place_list = place_list.filter(query).select_related()

        objects = place_list.order_by('-updated_at')

        # Augment the post_list
        for obj in objects:
            obj.natural_updated = naturaltime(obj.updated_at)

        paginator = Paginator(objects, 5)
        page = self.request.GET.get('page')

        try:
            objects = paginator.page(page)
        except PageNotAnInteger:
            objects = paginator.page(1)
        except EmptyPage:
            objects = paginator.page(paginator.num_pages)

        get_copy = request.GET.copy()
        parameters = get_copy.pop('page', True) and get_copy.urlencode()

        ctx = {'place_list' : objects, 'region_list' : region_list, 'category_list' : category_list, 'search' : strval, 
        'searchByCategory' : strcat, 'searchByRegion' : strreg, 'searchByRating' : float(strrate), 'parameters' : parameters}
        dump_queries()
        return render(request, self.template_name, ctx)

class PlaceDetailView(OwnerDetailView):
    template_name = "places/place_detail.html"
    def get(self, request, slug) :
        place = get_object_or_404(Place, slug=slug)
        images = Image.objects.all().filter(place_id=place.id)
        
        comments = Comment.objects.filter(place_id=place.id,status='True').order_by('-update_at')

        review = None
        if request.user.is_authenticated:
            review = Comment.objects.filter(place_id=place.id,user_id=request.user.id)
        context = { 'place' : place, 'images' : images, 'comments': comments, 'review' : review }
        return render(request, self.template_name, context)

def addcomment(request,slug):
    url = request.META.get('HTTP_REFERER')  # get last url
    if url==None:   #if directly tried to use link redirect to original page
        url = '/explore/'+slug
    if request.user.is_authenticated:   #only allow logged in user to rate
        place = get_object_or_404(Place, slug=slug)
        if request.method == 'POST':  # check post
            form = CommentForm(request.POST)
            if form.is_valid():
                data = Comment()  # create relation with model
                data.subject = form.cleaned_data['subject']
                data.comment = form.cleaned_data['comment']
                data.rate = form.cleaned_data['rate']
                data.ip = request.META.get('REMOTE_ADDR')
                data.place_id=place.id
                current_user= request.user
                data.user_id=current_user.id
                try:
                    data.save()  # save data to table
                except IntegrityError:
                    messages.warning(request, "Something went wrong. Please try again later.")
                    return HttpResponseRedirect(url)
                messages.success(request, "Review sent successfully. Thank you for your interest.")
            return HttpResponseRedirect(url)
    else:
        return HttpResponseRedirect('/explore/'+slug)

    return HttpResponseRedirect(url)

def editcomment(request,slug):
    url = '/explore/'+slug
    if request.user.is_authenticated:   #only allow logged in user to rate
        place = get_object_or_404(Place, slug=slug)
        review = Comment.objects.filter(place_id=place.id, user_id=request.user.id)[0]
        if request.method == 'POST':  # check post
            form = CommentForm(request.POST)
            if form.is_valid():
                data = Comment.objects.filter(place_id=place.id).get(user_id=request.user.id)  # create relation with model
                data.subject = form.cleaned_data['subject']
                data.comment = form.cleaned_data['comment']
                data.rate = form.cleaned_data['rate']
                data.ip = request.META.get('REMOTE_ADDR')
                try:
                    data.save()  # save data to table
                except IntegrityError:
                    messages.warning(request, "Something went wrong. Please try again later.")
                    return HttpResponseRedirect(url)
                messages.success(request, "Review edited successfully.")
            return HttpResponseRedirect(url)
        else:
            return render(request, "places/edit_review.html", {'place' : place, 'review' : review})
    else:
        return HttpResponseRedirect('/explore/'+slug)

    return HttpResponseRedirect(url)