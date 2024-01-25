from django.urls import path
from .views import capturas


urlpatterns = [    
    path('<int:code_user>/', capturas)
    
]
