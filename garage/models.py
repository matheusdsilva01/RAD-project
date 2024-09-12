from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Nome')
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False, verbose_name='Criado em')
    phone = models.CharField(max_length=20, null=False, blank=False, verbose_name='Telefone')
    address = models.CharField(max_length=200, null=False, blank=False, verbose_name='Endereço')

    vehicle = models.CharField(max_length=150, null=False, blank=False, verbose_name='Veículo')
    entryDate = models.DateTimeField(auto_now_add=True, null=False, blank=False, verbose_name='Data de entrada')
    departureDate = models.DateTimeField(null=True, blank=True, verbose_name='Data de saída')

    class Meta:
        ordering = ['-entryDate']
    def __str__(self):
        return self.name