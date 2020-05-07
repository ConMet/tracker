from django.shortcuts import render


def scrape(request):
    return render(request, 'scrape.html', {})
