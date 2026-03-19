"""URL configuration for the JobApplicationTracker project."""
from django.contrib import admin
from django.urls import include, path 

urlpatterns = [
    path('applications/', include("applications.urls")),
    path('admin/', admin.site.urls),
]
