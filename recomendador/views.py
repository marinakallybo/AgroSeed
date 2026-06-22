from django.shortcuts import render

from .models import Cultura


def listar_culturas(request):
    culturas = Cultura.objects.all().order_by("nome")

    return render(request, "recomendador/listar_culturas.html", {
        "culturas": culturas
    })
