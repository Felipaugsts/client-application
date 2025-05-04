from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AuthApi.urls')), 
    path('', include('UserProducts.urls')),
    path('jobs/', include('UserJobs.urls')),
]
