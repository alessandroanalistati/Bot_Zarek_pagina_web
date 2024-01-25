from django.urls import path
from .views import login, entrar, usuarios, usuario, novo, salvarNovo, edicao, salvarEdicao, delecao, salvarDelecao

urlpatterns = [
	path('login/', login),
	path('entrar/', entrar),
	path('', usuarios),
	path('usuario/<int:code>/', usuario),
	path('novo/', novo),
	path('salvarNovo/', salvarNovo),
	path('edicao/<int:id>/', edicao),
	path('salvarEdicao/', salvarEdicao),
	path('delecao/<int:id>/', delecao),
	path('salvarDelecao/', salvarDelecao)
]
