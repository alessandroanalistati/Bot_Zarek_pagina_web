from django.shortcuts import render
from .models import Usuario
from django.views.decorators.csrf import csrf_protect
from perguntas.models import Pergunta
from capturas.models import Captura

ok = 0

# Create your views here.
def login(request):
	global ok
	ok = 0
	titulo = 'LOGIN'
	return render(request, 'login.html', {'titulo': titulo, 'login': 0})

@csrf_protect
def entrar(request):
	user = request.POST.get("user")
	password = request.POST.get("password")
	user = user.strip()
	password = password.strip()

	# super usuário (administrador do sistema)
	if user == 'alessandro' and password == 'ass123456':
		global ok
		ok = 1
		titulo = 'Cadastro de Usuários'
		usuarios = Usuario.objects.all()
		return render(request, 'usuarios.html', {'titulo': titulo, 'usuarios': usuarios, 'ok': ok})
	else:
		usuario = Usuario.objects.filter(user=user, password=password, active=1)
		code_user = 0
		if len(usuario) > 0:
			for x in usuario:
				code_user = x.code
			return render(request, 'entrando.html', {'code_user': code_user})
		else:
			titulo = 'LOGIN'
			return render(request, 'login.html', {'titulo': titulo, 'login': 1})

def usuarios(request):
	titulo = 'Cadastro de Usuários'
	usuarios = Usuario.objects.all()
	global ok
	return render(request, 'usuarios.html', {'titulo': titulo, 'usuarios': usuarios, 'ok': ok})

def usuario(request, code):
	titulo = 'Cadastro de Usuários'
	usuario = Usuario.objects.get(code=code)
	global ok
	return render(request, 'usuarios.html', {'titulo': titulo, 'usuarios': [usuario], 'ok': ok})

def novo(request):
	titulo = 'Iserção de Usuários'
	global ok
	return render(request, 'novoUsuarios.html', {'titulo': titulo, 'ok': ok})

def getCODE():
	from datetime import datetime
	dataHora = datetime.now()
	code =  str(dataHora.year)
	code += str(dataHora.month)
	code += str(dataHora.day)
	code += str(dataHora.hour)
	code += str(dataHora.minute)
	code += str(dataHora.second)
	code =  str(int(round(int(code)/2, 0)))
	return code

@csrf_protect
def salvarNovo(request):
	code = getCODE()
	active = int(request.POST.get("active"))
	name = request.POST.get("name")
	email = request.POST.get("email")
	user = request.POST.get("user")
	password = request.POST.get("password")

	u = Usuario(
		code=code,
		active=active,
		name=name,
		email=email,
		user=user,
		password=password
	)
	u.save()

	titulo = 'Cadastro de Usuários'
	usuarios = Usuario.objects.all()
	global ok
	return render(request, 'usuarios.html', {'titulo': titulo, 'usuarios': usuarios, 'ok': ok})

def edicao(request, id):
	titulo = 'Edição de Usuários'
	usuario = Usuario.objects.get(id=id)
	global ok
	return render(request, 'edicaoUsuarios.html', {'titulo': titulo, 'usuarios': usuario, 'ok': ok})

@csrf_protect
def salvarEdicao(request):
	id = int(request.POST.get("id"))
	code = request.POST.get("code")
	active = int(request.POST.get("active"))
	name = request.POST.get("name")
	email = request.POST.get("email")
	user = request.POST.get("user")
	password = request.POST.get("password")

	Usuario.objects.filter(id=id).update(
		active=active,
		name=name,
		email=email,
		user=user,
		password=password
	)

	if active <= 0:
		Pergunta.objects.filter(code_user=code).update(active=0)
	else:
		Pergunta.objects.filter(code_user=code).update(active=1)

	titulo = 'Cadastro de Usuários'
	usuarios = Usuario.objects.all()
	global ok
	return render(request, 'usuarios.html', {'titulo': titulo, 'usuarios': usuarios, 'ok': ok})

def delecao(request, id):
	titulo = 'Deleção de Usuários'
	usuario = Usuario.objects.get(id=id)
	return render(request, 'delecaoUsuarios.html', {'titulo': titulo, 'usuarios': usuario, 'ok': ok})

@csrf_protect
def salvarDelecao(request):
	id = int(request.POST.get("id"))
	code = request.POST.get("code")
	Usuario.objects.filter(id=id).delete()
	Pergunta.objects.filter(code_user=code).delete()
	Captura.objects.filter(code_user=code).delete()

	titulo = 'Cadastro de Usuários'
	usuarios = Usuario.objects.all()
	global ok
	return render(request, 'usuarios.html', {'titulo': titulo, 'usuarios': usuarios, 'ok': ok})	
