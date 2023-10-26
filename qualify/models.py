""" This modole contein the models"""
from django.db import models


class Quality(models.Model):
    """
        This model create a quilify to specific asesor with his C.C
        Paramas or attributs:
        c_c: Number of the C.C asesor
        score_time: Quality wait time
        score_service: Quality the service given for asesor
        score_attention Quality the service given for coovitel
        score_recoomment: Recomment coovitel
        time: Qualification time
    """
    cedula = models.IntegerField()
    score_time = models.CharField(max_length=100)
    score_service = models.CharField(max_length=100)
    score_attention = models.CharField(max_length=100)
    score_recomment = models.CharField(max_length=100)
    time = models.DateTimeField()
    date = models.DateField()

    def __str__(self):
        """"""
        return f"Qualify asesor with number C.C {self.c_c} {self.time}"
