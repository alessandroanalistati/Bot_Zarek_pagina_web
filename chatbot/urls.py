from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('home.urls')),
	path('capturas/', include('capturas.urls')),
	path('home/', include('home.urls')),
	path('perguntas/', include('perguntas.urls')),
	path('usuarios/', include('usuarios.urls')),
    path('admin/', admin.site.urls),
]
