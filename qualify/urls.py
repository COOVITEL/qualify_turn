from django.urls import path
from . import views


urlpatterns = [
    path("<int:cedula>", views.quality, name="quality"),
    path("gracias!", views.thanks, name="thanks")
]