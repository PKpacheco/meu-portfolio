from django.shortcuts import render


def portfolio_exibir(request):
    return render(request, 'portfolios/portfolio_exibir.html', {})
