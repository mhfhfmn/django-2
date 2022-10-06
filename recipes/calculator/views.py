from django.http import HttpResponse
from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'salad': {
        'помидор, шт': 1,
        'огурец, шт': 1,
        'перец, шт': 1,
        'масло, л': 0.1,
        'соль, г': 0.06,

    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def home_view(request):
    return render(request, 'calculator/index.html')


def recipes(request, recipe):
    context = {}
    if recipe in DATA:
        servings = int(request.GET.get('servings', 1))
        tmp_dict = {}
        for key, val in DATA[recipe].items():
            tmp_dict.setdefault(key, round(val * servings, 2))
        context.setdefault('recipe', tmp_dict)
    return render(request, 'calculator/index.html', context)

