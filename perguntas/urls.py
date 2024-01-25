from django.urls import path
from .views import perguntas, pergunta, novo, salvarNovo, edicao, salvarEdicao, delecao, salvarDelecao, chatbot, questao, api


urlpatterns = [    
    path('<int:code_user>/', perguntas),
    path('pergunta/<int:id>/', pergunta),
	path('novo/<int:code_user>/', novo),
	path('salvarNovo/', salvarNovo),
	path('edicao/<int:id>/', edicao),
	path('salvarEdicao/', salvarEdicao),
	path('delecao/<int:id>/', delecao),
	path('salvarDelecao/', salvarDelecao),
	path('chatbot/<int:code_user>/', chatbot),
	path('questao/<int:code_user>/<int:code_before>/<str:question>/', questao),
	path('api/<int:code_user>/', api)
    
]