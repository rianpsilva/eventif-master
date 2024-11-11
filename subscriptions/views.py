from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from subscriptions.forms import SubscriptionForm
from subscriptions.models import Subscription
from django.core import mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.conf import settings


def subscribe(request):
    if request.method == 'POST':
       return create(request)
    else:
        return new(request)

def create(request):
    form = SubscriptionForm(request.POST)

    if not form.is_valid():
        return render(request, 'subscriptions/subscription_form.html', {'form': form})

    _send_mail(
        'subscriptions/subscription_email.txt',
        form.cleaned_data,
        'Confirmação de inscrição!',
        settings.DEFAULT_FROM_EMAIL,
        form.cleaned_data['email'])

    Subscription.objects.create(**form.cleaned_data)


    messages.success(request, 'Inscrição realizada com sucesso!')
    return HttpResponseRedirect('/inscricao/')


def new(request):
    return render(request, 'subscriptions/subscription_form.html', {'form': SubscriptionForm()})


def _send_mail(template_name, context, subject, from_, to):
    body = render_to_string(template_name, context)
    email = mail.send_mail(subject, body, from_, [from_, to])