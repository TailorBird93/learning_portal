from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import TutorialForm, Tutorial
import stripe
from django.conf import settings

#TEMPORARY KEY
stripe.api_key = settings.STRIPE_SECRET_KEY
#CHANGE LATER


def home(request):
    tutorials = Tutorial.objects.all()
    return render(request, 'main/home.html', {'tutorials': tutorials})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

@login_required
def add_tutorial(request):
    if request.method == 'POST':
        form = TutorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TutorialForm()
    return render(request, 'main/add_tutorial.html', {'form': form})

def tutorial_detail(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)
    return render(request, 'main/tutorial_detail.html', {'tutorial': tutorial})

def checkout(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)

    if tutorial.purchased:
        return redirect('tutorial_detail', pk=pk)

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': tutorial.title,
                },
                'unit_amount': int(tutorial.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=request.build_absolute_uri(f'/success/{pk}/'),
        cancel_url=request.build_absolute_uri('/cancel/'),
    )
    return redirect(session.url, code=303)

def success(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)
    tutorial.purchased = True
    tutorial.save()
    return render(request, 'main/success.html', {'tutorial': tutorial})


def cancel(request):
    return render(request, 'main/cancel.html')