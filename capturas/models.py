from django.db import models

# Create your models here.
class Captura(models.Model):
	code = models.CharField(max_length=15)
	code_user = models.CharField(max_length=15)
	active = models.IntegerField()
	name = models.CharField(max_length=100) # nome
	age = models.IntegerField() # idade
	sex = models.CharField(max_length=10) # sexo
	email = models.CharField(max_length=100) # email
	cellphone = models.CharField(max_length=15) # telefone celular
	phone = models.CharField(max_length=10) # telefone fixo
	cep = models.CharField(max_length=10) # cep - exemplo: 04538-133
	state = models.CharField(max_length=50) # estado
	city = models.CharField(max_length=100) # cidade
	neighborhood = models.CharField(max_length=100) # bairro
	address = models.CharField(max_length=200) # endereço
	number = models.CharField(max_length=5) # número
	cpf = models.CharField(max_length=15) # cpf - exemplo: 542.458.414-43
	cnpj = models.CharField(max_length=15) # cnpj - exemplo: 76.255.668/0001-41

	def __str__(self):
		return self.code
