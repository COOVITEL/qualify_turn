from django.shortcuts import render, redirect
from .models import Quality
import datetime


def quality(request, cedula):
    """"""
    date = datetime.date.today()
    turn = Quality.objects.filter(cedula=cedula, date=date)
    if turn:
        return render(request, "test.html")
    else:
        if request.method == "POST":
            score_time = request.POST["score_time"]
            score_service = request.POST["score_service"]
            score_attention = request.POST["score_attention"]
            score_recomment = request.POST["score_recomment"]
            time = datetime.datetime.now()
            created = Quality(cedula=cedula,
                            score_time=score_time,
                            score_service=score_service,
                            score_attention=score_attention,
                            score_recomment=score_recomment,
                            time=time,
                            date=date
            )
            created.save()
            return redirect("thanks")
        return render(request, "quality.html")

def thanks(request):
    """"""
    return render(request, "thanks.html")