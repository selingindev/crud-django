from django.shortcuts import render

def adicionarEquipamento(request):
    return render(request, 'adicionar_equipamento.html')
