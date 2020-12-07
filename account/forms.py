from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
	email = forms.EmailField(required=True, label="Email address")

	class Meta:
		model = User
		fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class EditProfileForm(UserChangeForm):
	password = None
	current_password = forms.CharField(required=True, widget=forms.PasswordInput, label="Current password")

	class Meta:
		model = User
		fields = [ "email", "first_name", "last_name", "current_password"]

	def clean_current_password(self):
         valid = self.instance.check_password(self.cleaned_data['current_password'])
         if not valid:
             raise forms.ValidationError("Password is incorrect.")
         return valid