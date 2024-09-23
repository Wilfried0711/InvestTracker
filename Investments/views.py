from django.shortcuts import render, redirect
from .models import Investment
from Portfolios.models import Portfolio

def add_investment(request, portfolio_id):
    portfolio = Portfolio.objects.get(id=portfolio_id)
    if request.method == 'POST':
        investment_type = request.POST.get('investment_type')
        quantity = request.POST.get('quantity')
        current_value = request.POST.get('current_value')
        Investment.objects.create(
            portfolio=portfolio,
            investment_type=investment_type,
            quantity=quantity,
            current_value=current_value
        )
        return redirect('portfolio_list')
    return render(request, 'add_investment.html', {'portfolio': portfolio})
