from django.shortcuts import render
from django.http import HttpResponse

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
    # можете добавить свои рецепты ;)
}


def recipe(request,item):
    count = int(request.GET.get('servings', 1))

    context = {}
    context['recipe'] = {}

    if item in DATA:
        for product, number in DATA[item].items():
            context['recipe'][product] = float('{0:9.3f}'.format(number*count))

    return render(request, 'calculator/index.html', context)
    