from django.db import models

# Create your models here.
class Tarefa(models.Model):
    nome = models.CharField(max_length=100)
    data_inicial = models.DateField()
    data_encerramento = models.DateField()
    status = models.BooleanField(default=False)