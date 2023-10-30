from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'calificacion', views.ApiQuality, 'apiencuesta')

urlpatterns = [
    path("<int:cedula>/<int:id_turn>", views.quality, name="quality"),
    path("gracias!", views.thanks, name="thanks"),
    path("encuesta_digiturno/api/", include(router.urls))
]