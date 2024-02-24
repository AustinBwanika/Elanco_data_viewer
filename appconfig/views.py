from django.shortcuts import render
from .api_data import ApiData
# Create your views here.

def show_home(request):
    return render(request, 'home.html')

def show_visuals(request):
    api_data = ApiData()
    data = api_data.get_data()
    consumption = api_data.consumption_per_day()

    labels = [date for date, k in consumption]
    usage= [quantity for k, quantity in consumption]

    graph_data = {
        'labels': labels,
        'usage': usage
    }
    return render(request, 'visuals.html', context={'data': data, 'consumption': consumption, 'graph_data': graph_data})

def show_data(request):
    api_data = ApiData()
    data = api_data.get_data()
    search = request.GET.get('search', None)

    if search:
        data = [item for item in data if search.lower() in item['ResourceGroup'].lower()]
        return render(request, 'data_search.html', context={'data': data, 'search': search})
    return render(request, 'data.html', context={'data': data})
