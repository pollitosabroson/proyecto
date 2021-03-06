from contend.models import Paciente, Consulta
from contend.forms import DatosPaciente, Observaciones
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, loader
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
	return render_to_response('inicio.html', context_instance=RequestContext(request))

def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/inicio')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/inicio')
                else:
                    return render_to_response('noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('nousuario.html', context_instance=RequestContext(request))
    else:
        formulario = AuthenticationForm()
    return render_to_response('ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))	

@login_required(login_url='/ingresar')
def new_pacient(request):
    if  request.method =='POST':
        formulario = DatosPaciente(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/consulta')
    else:
        formulario = DatosPaciente()
    return render_to_response ('citas.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def consulta(request):
    if request.method == 'POST':
        formulario = Observaciones(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = Observaciones()
    return render_to_response('consulta.html',{'formulario':formulario}, context_instance=RequestContext(request))


@login_required(login_url='/ingresar')
def datos(request):
    usuario = request.user
    return render_to_response('datos.html',{'usuario':usuario},context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')

