from django.contrib import admin
from places.models import Place, Category, Image, Region, Comment

# Register your models here.
class ImageInline(admin.TabularInline):
    model = Image

class PlaceAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	inlines = [
        ImageInline,
    ]
	readonly_fields = ('averagereview', 'countreview')

class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject','comment', 'user', 'place', 'rate', 'status','create_at']
    list_filter = ['status']
    readonly_fields = ('subject','comment','ip','user','place','rate','id')

admin.site.register(Place, PlaceAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
admin.site.register(Region)