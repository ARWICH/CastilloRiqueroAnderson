from django.shortcuts import render,redirect
#from appCrud.forms import 
from appCrud.models import Persona,Pais
# Create your views here.
from appCrud.forms import PersonaForm
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def personadetalle(request):
   # personas = Persona.objects.all()
    personas = Persona.objects.select_related('nacionalidad').all().values('id','nombre','nacimiento','nacionalidad__nombre')
    return render(request,'maindetalle.html',{'personas':personas})

def personanuevo(request):
    paises = Pais.objects.all()
    if request.method == 'POST':
        personaform = PersonaForm(request.POST)
        if personaform.is_valid():
            try:
                personaform.save()
                return redirect('/personas/')
            except: 
                pass
    else:
        personaform = PersonaForm()
      #  paisform = PaisForm()
    return render(request,'mainnuevo.html',{'personaform':personaform,'paises':paises})

def personaeditar(request, id):
    persona = Persona.objects.get(id=id)
    paises = Pais.objects.all()
    #persona =  Persona.objects.select_related('nacionalidad').all().values('id','nombre','nacimiento','nacionalidad__nombre','nacionalidad__id','nacionalidad__nacionalidad') 
    pais = Persona.objects.prefetch_related('nacionalidad').filter(id=persona.id).values('id','nombre','nacionalidad__id','nacionalidad__nombre','nacionalidad__nacionalidad')
    return render(request, 'maineditar.html', {'persona': persona,'pais':pais,'paises':paises})

def personaactua(request, id):
    persona = Persona.objects.get(id=id)
    if request.method == 'POST':
            personaform = PersonaForm(request.POST, instance=persona)
            if personaform.is_valid():
                try:
                    personaform.save()
                    return redirect('/personas/')
                except:
                    pass
    else:
            personaform = PersonaForm(instance=persona)
    return render(request, 'maineditar.html', {'persona': persona,'personaform':personaform})

def ajax_campo(request):
        pais = request.GET.get('nacionalidad')
        if pais:
            nacionalidad = Pais.objects.get(id=pais).nacionalidad
            
        return JsonResponse({'nacionalidad':nacionalidad})