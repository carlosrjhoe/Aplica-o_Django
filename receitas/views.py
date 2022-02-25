from django.shortcuts import render

# Create your views here.
def index(request):
    receitas = {
        1:'Bolo_vucão',
        2:'Bolo_tipico',
        3:'Broa',
        4:'Bolo de chocolate'
    }
    dados = {
        'nome_das_receitas' : receitas
    }
    return render(request, 'index.html', dados)

def receita(request):
    return render(request, 'receita.html')