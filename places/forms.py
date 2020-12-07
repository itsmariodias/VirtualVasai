from django import forms
from places.models import Place, Image, Comment
from django.core.files.uploadedfile import InMemoryUploadedFile
from places.humanize import naturalsize
from django.forms import ClearableFileInput


# Create the form class.
class PlaceModelForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)

    # Call this 'picture' so it gets copied from the form to the in-memory model
    # It will not be the "bytes", it will be the "InMemoryUploadedFile"
    # because we need to pull out things like content_type

    # picture = forms.FileField(required=False, label='File to Upload <= '+max_upload_limit_text)
    # upload_field_name = 'picture'

    # Hint: this will need to be changed for use in the ads application :)
    class Meta:
        model = Place
        fields = ['title', 'address', 'category']  # Picture is manual

    # Validate the size of the picture
    def clean(self):
        cleaned_data = super().clean()
        pic = cleaned_data.get('picture')
        if pic is None:
            return
        if len(pic) > self.max_upload_limit:
            self.add_error('picture', "File must be < "+self.max_upload_limit_text+" bytes")

# https://docs.djangoproject.com/en/3.0/topics/http/file-uploads/
# https://stackoverflow.com/questions/2472422/django-file-upload-size-limit
# https://stackoverflow.com/questions/32007311/how-to-change-data-in-django-modelform
# https://docs.djangoproject.com/en/3.0/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other

class ImageModelForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['images']
        widgets = {
            'images': ClearableFileInput(attrs={'multiple': True}),
        }
        # widget is important to upload multiple files

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'comment', 'rate']