from django.db import models


class Contacto(models.Model):
    nombre= models.CharField(max_length=50)
    asunto= models.CharField(max_length=50)
    mail= models.EmailField()
    mensaje = models.TextField()
    