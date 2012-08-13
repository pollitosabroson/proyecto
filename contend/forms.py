#encoding:utf-8 
from django.forms import ModelForm
from django import forms
from contend.models import Paciente, Consulta

class DatosPaciente(ModelForm):
	class Meta:
		model = Paciente

class Observaciones(ModelForm):
	class Meta:
		model = Consulta
		exclude = ('paciente')