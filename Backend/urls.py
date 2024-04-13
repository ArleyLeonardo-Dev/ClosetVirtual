from django.urls import path, include
from .views import *
from rest_framework import routers

routes = routers.DefaultRouter()
routes.register(r'Zapatos', ZapatosView, "ApiZapatos")
routes.register(r'pantalonesFaldas', PantalonesFaldasView, "ApiPantalonesFaldas")
routes.register(r'Camisas', CamisasView, "ApiCamisas")
routes.register(r'Vestidos', VestidosView, "ApiVestidos")



urlpatterns = [
    path("",include(routes.urls)),
    path("Combinaciones/", CombinacionesView.as_view(), name = "Combinaciones"),
    path("Combinaciones/<int:pk>/", DetalleCombinacionesView.as_view(), name = "CombinacionesDetalles"),
    
]