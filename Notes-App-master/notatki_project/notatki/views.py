from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from .models import Notatka
from .forms import NotatkaForm
from django.db import models
# Create your views here.
def lista_notatek(request,tag_slug=None):
    notatki = Notatka.objects.all().order_by(
        models.Case(
            models.When(poziom_waznosci='bardzo', then=1),
            models.When(poziom_waznosci='srednio', then=2),
            models.When(poziom_waznosci='malo', then=3),
            output_field=models.IntegerField(),
        )
    )
    if tag_slug:
        notatki = Notatka.objects.filter( status='data_publikacji',tag__slug=tag_slug)

    paginator = Paginator(notatki, per_page=8)
    strona = request.GET.get('strona')

    try:
        notatki_strona = paginator.page(strona)
    except PageNotAnInteger:
        notatki_strona = paginator.page(1)
    except EmptyPage:
        notatki_strona = paginator.page(paginator.num_pages)


    return render(request,'notatki/lista_notatek.html',{'strona':notatki_strona,})

def dodaj_notatke(request):
    if request.method == 'POST':
        form = NotatkaForm(request.POST)
        if form.is_valid():
            notatka = form.save(commit=False)
            notatka.autor = request.user
            notatka.save()
            form.save()
            return redirect('lista_notatek')
    else:
        form = NotatkaForm()
    return render(request, 'notatki/dodaj_notatke.html', {'form': form})

def edytuj_notatke(request, pk):
    notatka = get_object_or_404(Notatka, pk=pk)
    if request.method == 'POST':
        form = NotatkaForm(request.POST, instance=notatka)
        if form.is_valid():
            form.save()
            return redirect('lista_notatek')
    else:
        form = NotatkaForm(instance=notatka)
    return render(request, 'notatki/edytuj_notatke.html', {'form': form})

def szczegoly_notatki(request, notatka_id):
    notatka = get_object_or_404(Notatka, pk=notatka_id)
    return render(request, 'notatki/szczegoly_notatki.html', {'notatka': notatka})
