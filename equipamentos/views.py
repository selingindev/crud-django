from django.shortcuts import render
from .models import Equipamento  

def visualizarEquipamentos(request):
    if request.method == "GET":
        equipamentos = Equipamento.objects.all() 
        print(equipamentos)
        return render(request, 'visualizarEquipamentos.html', {'equipamentos': equipamentos})
