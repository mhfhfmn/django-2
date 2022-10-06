from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings
from pagination.settings import BUS_STATION_CSV
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))




def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(BUS_STATION_CSV, encoding='utf-8') as file:
        data = list(csv.DictReader(file))
    paginator = Paginator(data, 15)
    current_page = request.GET.get('page', 1)
    page = paginator.get_page(current_page)
    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
