import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder
import json


from django.shortcuts import render
from .api_data import ApiData
from datetime import datetime, timedelta

# Create your views here.

def show_home(request):
    return render(request, 'home.html')

def show_visuals(request):
    api_data = ApiData()
    data = api_data.get_data()
    consumption = api_data.consumption_per_day()

    # labels = [date for date, k in consumption]
    # usage= [quantity for k, quantity in consumption]
    test_consumption = [
        (datetime.now() - timedelta(days=i), i * 10) for i in range(9)
    ]

    labels = [date.strftime("%Y-%m-%d") for date, quantity in test_consumption]
    usage = [quantity for date, quantity in test_consumption]

    graph_data = {
        'labels': labels,
        'usage': usage
    }
    return render(request, 'visuals.html', context={'data': data, 'consumption': consumption, 'graph_data': json.dumps(graph_data)})

def show_data(request):
    api_data = ApiData()
    data = api_data.get_data()
    search = request.GET.get('search', None)

    if search:
        data = [item for item in data if search.lower() in item['ResourceGroup'].lower()]
        return render(request, 'data_search.html', context={'data': data, 'search': search})
    return render(request, 'data.html', context={'data': data})
