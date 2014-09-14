from django.shortcuts import render
from subscription.models import Subscriber
from subscription.forms import SubscribeForm


def index(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'subscription/index.html', {'success': True})
        return render(request, 'subscription/index.html', {'success': False})
    else:
        form = SubscribeForm()
    return render(request, 'subscription/index.html', {'form': form})