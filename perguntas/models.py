from django.db import models

# Create your models here.
class Pergunta(models.Model):
	code = models.CharField(max_length=15)
	code_user = models.CharField(max_length=15)
	active = models.IntegerField()
	code_relation = models.CharField(max_length=15)
	question = models.CharField(max_length=5000)
	answer = models.CharField(max_length=5000)

	def __str__(self):
		return self.question