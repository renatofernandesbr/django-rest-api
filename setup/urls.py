from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('escola/', include('escola.urls')),
    path('cliente/', include('cliente.urls')),
]
