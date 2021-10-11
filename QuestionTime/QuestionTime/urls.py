"""QuestionTime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from django_registration.backends.one_step.views import RegistrationView

from core.views import IndexTemplateView
from users.forms import CustomUserForm

urlpatterns = [
    path('admin/', admin.site.urls),

    # url to registration page for new users
    # https://django-registration.readthedocs.io/en/3.2/one-step-workflow.html
    # The one-step workflow uses two templates:
    #   django_registration/registration_form.html.
    #   django_registration/registration_closed.html
    path('accounts/register/', RegistrationView.as_view(form_class=CustomUserForm, success_url='/'),
         name='django_registration_register'),

    path('accounts/', include('django_registration.backends.one_step.urls')),

    # https://docs.djangoproject.com/en/3.1/topics/auth/default/#module-django.contrib.auth.views
    path('accounts/', include('django.contrib.auth.urls')),

    # login via API
    path('api/', include('users.api.urls')),

    #
    path('api/', include('questions.api.urls')),

    # login via API
    path('api-auth/', include('rest_framework.urls')),

    # login via rest
    path('api/rest-auth/', include('rest_auth.urls')),

    # registration via rest, the same as accounts/register/ form
    path('api/rest-auth/registration/', include('rest_auth.registration.urls')),

    re_path(r"^.*$", IndexTemplateView.as_view(), name='entry-point')

]
