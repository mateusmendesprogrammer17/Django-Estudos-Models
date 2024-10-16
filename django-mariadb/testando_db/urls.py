from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),           # URL para o admin
    path('', include('users.urls')),           # Direciona a raiz para o aplicativo users
]
