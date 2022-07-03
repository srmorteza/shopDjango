from django.shortcuts import render, redirect


def home_page(request):
    context = {
        'data': 'new_data'
    }
    return render(request, 'home_page.html', context)
