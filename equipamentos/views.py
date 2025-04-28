from django.shortcuts import render
from equipamentos import Equipamentos

def visualizarEquipamentos(request):
    if request.method == "GET":
        equipamentos = equipamentos.objects.all;
        print(equipamentos)