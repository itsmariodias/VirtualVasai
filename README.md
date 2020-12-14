# VirtualVasai
Django-based website to showcase tourist places in Vasai

### First setup:
Configure the settings in `settings.py` for the database backend. We have used MySQL as the database for our project.
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Requirements:
```
django
django-crispy-forms
social-auth-app-django
social-auth-core
django-extensions
Pillow
```

### About:
This is a simple website designed and implemented using Django 3 along with Bootstrap in MySQL. It is a tourist based site where users can see and review places based in and around Vasai. Admin users can add and manage the users and add new places using Django's default admin page. Users can register and login as they wish to review sites and rate them. Based on the rating the top 3 places are displayed on the Homepage as well. There is a filter and search feature to quickly find relevant places.

###### Disclaimer: All api keys and media files have been removed for privacy reasons. 
