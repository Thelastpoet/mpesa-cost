from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('nas-man/', admin.site.urls),
    path('', include('mpesacal.urls')),
    path('accounts/', include('allauth.urls')),
]
