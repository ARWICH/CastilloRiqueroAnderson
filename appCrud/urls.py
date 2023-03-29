from django.urls import path
from .views import index,personadetalle,personanuevo,ajax_campo,personaeditar,personaactua

app_name = "appCrud"
urlpatterns = [
    #Vista del index
    path('',personadetalle, name='Index'),
    path('personas/',personadetalle, name="personas"),
    path('persona/nuevo/',personanuevo,name='persona/nuevo/'),
    path('persona/editar/<int:id>',personaeditar),
    path('persona/actualizar/<int:id>',personaactua),
    path('ajax_campo/',ajax_campo,name='ajax_campo')
]