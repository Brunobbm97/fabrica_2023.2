from django.shortcuts import render, redirect
from .models import Piloto
import datetime
from .forms import PilotoForm


def home(request):
    data = {}
    data['pilotos'] = ['t1','t2','t3']

    data['now'] = datetime.datetime.now()
    now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now

    return render(request, 'pilotos/home.html',data)

def listagem(request):
    data = {}
    data['pilotos']  = Piloto.objects.all()
    return render(request, 'pilotos/listagem.html',data)

def novo_piloto(request):
    data = {}
    form = PilotoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    return render(request, 'pilotos/form.html', data)

def update(request, pk):
    data= {}
    piloto = Piloto.objects.get(pk=pk)
    form = PilotoForm(request.POST or None, instance=piloto)

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    data['form'] = form
    data['piloto'] = piloto
    return render(request, 'pilotos/form.html', data)

def delete(request, pk):
    piloto = Piloto.objects.get(pk=pk)
    piloto.delete()
    return redirect('url_listagem')

# Create your views here.
