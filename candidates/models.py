from django.conf import settings
from django.db import models
from django.utils import timezone

class Candidate(models.Model):
    #El sisguiente atributo es una relacion en DB
    recruiter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    first_name = models.CharField(null = False, max_length=50)
    second_name = models.CharField(null=True, blank=True, max_length=50)
    last_name = models.CharField(null=False, max_length=50)
    second_last_name = models.CharField(null=True, blank=True, max_length=50)
    birthdate = models.DateField(null=False)
    email = models.EmailField(null = False)
    phone = models.CharField(max_length=10, null=False, default='1234567890')
    comments = models.TextField(null=True, blank=True)

    created_date = models.DateField(null=False, default=timezone.now)

    SOURCE_OPTIONS = (
        ('SELECIONAR', 'SELECIONAR'),
        ('Bolsa de trabajo UV', 'Bolsa de trabajo UV'),
        ('OCC Mundial', 'OCC Mundial'),
        ('Buscotrabajo', 'Buscotrabajo'),
        ('Quierotrabajo', 'Quierotrabajo')
    )

    source = models.CharField(choices=SOURCE_OPTIONS, max_length=200, default='SELECCIONAR')

    STATUS_OPCIONS = (
        ('AVAILABLE', 'AVAILABLE'),
        ('INTERVIEW', 'INTERVIEW'),
        ('NOT AVAILABLE', 'NOT AVAILABLE'),
        ('HIRED', 'HIRED'),
    )

    status = models.CharField(choices=STATUS_OPCIONS, max_length=200, default='AVAILABLE')

    
  

    def create(self):
        self.save()

    def __str__(self):
        return self.first_name + ' ' + self.last_name



class Comment(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete = models.CASCADE)
    recruiter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null=True)
    description = models.TextField(null = False)
    created_date = models.DateTimeField(null = False, default=timezone.now)
    status = models.CharField(max_length=200, default=False)
