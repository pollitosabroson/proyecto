#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Paciente(models.Model):
	Sexo = (
    (u'men', 'Hombre'),
    (u'women', 'Mujer'),
	)
    
	Estado_Civil = (
	(u'sol','Soltero'),
	(u'cas','Casado'),
	(u'viu','Viudo'),
	(u'div','Divorsiado'),
	(u'uni','Union libre'),
	)
	nombre = models.CharField(max_length=100, verbose_name='Nombre')
	ap_paterno = models.CharField(max_length=50,verbose_name='Apellido Paterno')
	ap_materno = models.CharField(max_length=50,verbose_name='Apellido Materno',blank= True)
	edad = models.IntegerField(verbose_name='Edad',help_text='Edad en numeros porfavor')
	sexo = models.CharField (max_length=150,verbose_name='Sexo del paciente',choices = Sexo)
	es_civil = models.CharField (max_length= 50, verbose_name ='Estado civil', choices= Estado_Civil)
	fecha_registro = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return self.nombre

class Consulta(models.Model):
	Dias = (
		(u'1','1'),
		(u'2','2'),
		(u'3','3'),
		(u'4','4'),
		(u'5','5'),
		(u'6','6'),
		(u'7','7'),
		(u'8','8'),
		(u'9','9'),
		(u'10','10'),
		(u'11','11'),
		(u'12','12'),
		(u'13','13'),
		(u'14','14'),
		(u'15','15'),
		(u'16','16'),
		(u'17','17'),
		(u'18','18'),
		(u'19','19'),
		(u'20','20'),
		(u'21','21'),
		(u'22','22'),
		(u'23','23'),
		(u'24','24'),
		(u'25','25'),
		(u'26','26'),
		(u'27','27'),
		(u'28','28'),
		(u'29','29'),
		(u'30','30'),
		(u'31','31'),
		)
	Mes = (
		(u'enero','Enero'),
		(u'febrero','Febrero'),
		(u'marzo','Marzo'),
		(u'abril','Abril'),
		(u'mayo','Mayo'),
		(u'junio','Junio'),
		(u'julio','Julio'),
		(u'agosto','Agosto'),
		(u'septiembre','Seprtiembre'),
		(u'octubre','Octubre'),
		(u'noviembre','Noviembre'),
		(u'diciembre','Diciembre'),
		)
	paciente = models.ForeignKey(Paciente)
	enfermedades = models.CharField(max_length= 200,verbose_name='Descripción de la enfermedad', help_text='Separe las enfermades con una coma')
	descripcionenfer = models.TextField(max_length = 300, verbose_name = 'Descripcionde la enfermedar')
	medicamento = models.CharField(max_length= 200)
	descripcion = models.TextField(max_length=300, help_text='Cada cuando tomar el medicamento')
	dia = models.CharField(max_length=130, verbose_name='Proxima cita', help_text='Dia',choices=Dias,blank= True)
	mes= models.CharField(max_length=10,verbose_name='Mes',choices=Mes,blank= True)
	tiempo_registro = models.DateTimeField(auto_now=True)
	usuario = models.ForeignKey(User)
	def __unicode__(self):
		return self.enfermades