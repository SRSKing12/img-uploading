from django.contrib import admin
from django.urls import path
from usr import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.regst, name='register'),
    path('sin', views.sgin, name='sin'),
    path('sout', views.sout, name="sout"),
    path('sginpg', views.sginpg, name="sginpg"),
    path('change_pass', views.change_pass, name="change_pass"),
    path('update_data', views.update_data, name="update_data"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)