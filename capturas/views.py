from django.shortcuts import render
from .models import Captura

# Create your views here.
def capturas(request, code_user):
	titulo = 'CAPTURA DE DADOS DO USUÁRIOS'
	captura = Captura.objects.filter(code_user=code_user)
	return render(request, 'capturas.html', 
				 {'titulo': titulo, 'capturas': captura, 'code_user': code_user})
