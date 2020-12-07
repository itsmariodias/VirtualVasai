from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator
from django.conf import settings

from django.db.models import Avg, Count


class Place(models.Model) :
    title = models.CharField(
            max_length=100,
            validators=[MinLengthValidator(5, "Title must be greater than 5 characters")]
    )

    slug = models.SlugField(unique= True, blank=True)

    region = models.ForeignKey('Region', on_delete=models.CASCADE)

    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    address = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(10, "Address must be greater than 10 characters")]
    )

    #for the map
    latitude = models.DecimalField(max_digits=10, decimal_places=8,
    			validators=[MinValueValidator(-90, message="Latitude should be between -90 and 90"), MaxValueValidator(90, message="Latitude should be between -90 and 90")]
    	)
    longitude = models.DecimalField(max_digits=11, decimal_places=8,
    		 	validators=[MinValueValidator(-180, message="Longitude should be between -180 and 180"), MaxValueValidator(180, message="Longitude should be between -180 and 180")]
    	)

    map_place_id = models.CharField(
            null = True,
            max_length=200,
            help_text='(optional) Enter the maps place id for the site, e.g. ChIJpWiC6ZCu5zsRv1_fkb9WBeg'
    )

    streetview = models.CharField("Enable streetview?", max_length=10,choices=(('True', 'Yes'), ('False', 'No')), default='True',
    			help_text='Enable streetview or not.')

    description = models.TextField(null=True)
    # comments = models.ManyToManyField(settings.AUTH_USER_MODEL, 
    #     bthrough='Comment', related_name='comments_owned')

    featured_image = models.ImageField(upload_to="uploads/%Y/%m/%d", null=True)

    # Picture
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.title

    def averagereview(self):
        reviews = Comment.objects.filter(place=self, status='True').aggregate(average=Avg('rate'))
        avg=0
        if reviews["average"] is not None:
            avg=float(reviews["average"])
        return avg

    def countreview(self):
        reviews = Comment.objects.filter(place=self, status='True').aggregate(count=Count('id'))
        cnt=0
        if reviews["count"] is not None:
            cnt = int(reviews["count"])
        return cnt

class Image(models.Model):
    images = models.ImageField(upload_to="uploads/%Y/%m/%d")
    place = models.ForeignKey(Place, on_delete=models.CASCADE)


class Category(models.Model):
    name = models.CharField(
            max_length=200,
            help_text='Enter a category (e.g. Church)',
            validators=[MinLengthValidator(2, "Category must be greater than 1 character")]
    )

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Region(models.Model):
    name = models.CharField(
            max_length=100,
            validators=[MinLengthValidator(2, "Region must be greater than 2 characters")]
    )

    image = models.ImageField(upload_to="uploads/%Y/%m/%d")

    def __str__(self):
        """String for representing the Model object."""
        return self.name

#Adding review system
class Comment(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=50, blank=True)
    comment = models.CharField(max_length=250,blank=True)
    rate = models.IntegerField(default=1)
    ip = models.CharField(max_length=20, blank=True)
    status=models.CharField(max_length=10,choices=STATUS, default='True')
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['place', 'user'], name='single_review')]

    def __str__(self):
        return self.subject

