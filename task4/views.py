# from django.shortcuts import render
#
# def home(request):
#     return render(request, 'fourth_task/platform.html')
#
# def games(request):
#     games_list = ["Игра 1", "Игра 2", "Игра 3"]  # Список игр
#     context = {'games': games_list}
#     return render(request, 'fourth_task/games.html', context)
#
# def cart(request):
#     return render(request, 'fourth_task/cart.html')

from django.shortcuts import render


def home(request):
    return render(request, 'fourth_task/platform.html')


def games(request):
    games = ["Игра 1", "Игра 2", "Игра 3"]
    return render(request, 'fourth_task/games.html', {'games': games})


def cart(request):
    return render(request, 'fourth_task/cart.html')