from django import forms
from appCrud.models import Persona,Pais
from datetime import date

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
       # fields = "__all__"
        fields = ['id','nombre','nacimiento','nacionalidad']
      #  nacionalidad = forms.ModelChoiceField(queryset=Pais.objects.all(),empty_label="Seleccionar",
      #                                         to_field_name='nacionalidad',
      #                                      required=True,widget=forms.Select
      #                                      (attrs={'class':'form-control'})
      #                                      )
    def clean_validarid(self):
            id_unico = self.cleaned_data.get('id')
            if Persona.objects.filter(id=id_unico).exists():
                raise forms.ValidationError('El Id único ya está en uso')
            return id_unico
        
    def clean_validarmayoredad(self):
            fecha_nacimiento = self.cleaned_data['nacimiento']
            edad = date.today().year - fecha_nacimiento.year - ((date.today().month, date.today().day) < (fecha_nacimiento.month, fecha_nacimiento.day))
            if edad < 18:
                raise forms.ValidationError('Debe ser mayor de edad.')
            return fecha_nacimiento
        
#class PaisForm(forms.ModelForm):
#    class Meta:
#        model = Pais
#        fields = "__all__"