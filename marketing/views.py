from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import EmailSignupForm
from .models import SignUp
import requests
import json



MAILCHIMP_API_KEY = settings.MAILCHIMP_API_KEY
MAILCHIMP_DATA_CENTER = settings.MAILCHIMP_DATA_CENTER
MAILCHIMP_EMAIL_LIST_ID = settings.MAILCHIMP_EMAIL_LIST_ID

api_url = f"https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0"
members_endpoint = f"{api_url}/lists/{MAILCHIMP_EMAIL_LIST_ID}/members"

def subscribe(email):
  data = {
    "email_address": email,
    "status": 'subscribed'
  }
  r = requests.post(members_endpoint, data=json.dumps(data), auth=("",MAILCHIMP_API_KEY))
  return r.status_code, r.json()


def email_lists_signup(request):
  form = EmailSignupForm(request.POST or None)
  if request.method == 'POST':
    if form.is_valid():
      email_signup_qs = SignUp.objects.filter(email=form.instance.email)
      if email_signup_qs.exists():
        messages.info(request, 'You are already subscribed')
      else:
        subscribe(form.instance.email)
        form.save()
  return HttpResponseRedirect(request.META.get("HTTP_REFERER"))