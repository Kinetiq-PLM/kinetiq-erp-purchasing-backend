from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Kinetiq Backend!")

urlpatterns = [
    path("admin/", admin.site.urls),  
    path("api/", include("api.urls")),  # ✅ Only include `api.urls`
    path("", home),  # Default homepage
    
   
]
