from django.shortcuts import render,redirect
from .models import Hiretuber
from django.contrib import messages
  # first_name = models.CharField(max_length=100)
  # last_name = models.CharField(max_length=100)
  # email = models.CharField(max_length=150)
  # tuber_id = models.IntegerField()
  # tuber_name = models.CharField(max_length=100)
  # city = models.CharField(max_length=100)
  # state = models.CharField(max_length=100)
  # phone = models.CharField(max_length=100)
  # message = models.TextField(blank=True)
  # user_id = models.IntegerField(blank=True)

def hiretuber(request):
  if request.method == 'POST':
    first_name = request.POST['first_name']
    last_name = request.POST['last_name'] 
    email = request.POST['email'] 
    tuber_id = request.POST['tuber_id']
    tuber_name = request.POST['tuber_name']
    city = request.POST['city']
    state = request.POST['state']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']

    # TODO: DO all sanitization
    hiretuber = Hiretuber(first_name=first_name, last_name=last_name, email=email, tuber_id=tuber_id, tuber_name=tuber_name, city=city, state=state, phone=phone, message=message, user_id=user_id)
    hiretuber.save()
    messages.success(request, "Thanks for reching out!")
    return redirect('youtubers')
