from django.shortcuts import render, redirect
from .forms import RegisterForm, EditProfileForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def register(response):
	if response.user.is_authenticated:
		return redirect("/")
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			new_user = form.save()
			messages.info(response, "Thanks for registering. You are now logged in.")
			new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
			login(response, new_user)
			return redirect("/")
	else:
		form = RegisterForm()
	return render(response, "account/register.html", {"form":form})

@login_required(login_url='/account/login/')
def view_profile(request):
    return render(request, "account/profile.html", {'user': request.user})

@login_required(login_url='/account/login/')
def edit_profile(request):
	if request.user.has_usable_password():
		if request.method == 'POST':
			form = EditProfileForm(request.POST, instance=request.user)

			if form.is_valid():
				form.save()
				messages.success(request, "Changes are saved.")
				return redirect('/account/profile')
		else:
			form = EditProfileForm(instance=request.user)
	else:
		messages.info(request, "You cannot edit your profile on this account.")
		return redirect("/account/profile")
	return render(request, "account/edit_profile.html", {'form': form})