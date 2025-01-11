from django.shortcuts import render

def home(request):
    return render(request, 'third_task/platform.html')

def games(request):
    items = {
        'item1': 'Игра 1',
        'item2': 'Игра 2',
        'item3': 'Игра 3',
    }
    return render(request, 'third_task/games.html', {'items': items})

def cart(request):
    return render(request, 'third_task/cart.html')