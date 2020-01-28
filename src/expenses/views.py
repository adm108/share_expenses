from django.shortcuts import render
from account.models import Account


def home_screen_view(request):
    context = {}
    users = Account.objects.all()
    context['users'] = users
    return render(request, 'base.html', context)
