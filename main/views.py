from sqlite3 import Date
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .filters import *
from django.core.mail import send_mail
from .forms import *
from django.contrib import messages
from .mpesa import ac_token
import requests
import json

# Create your views here.


def daraja_callback(request):
    #parse json data from the request body
    data = json.loads(request.body)
    # you can use the data as you want
    # for example storing in the database
    # you can also check the signature sent by daraja
    # to verify the authenticity of the webhook
    # and also check the transaction status
    return HttpResponse("Callback received")

def Home(request):
    return render(request, 'main/index.html', {})

def Homepage(request):
    pay = Payment.objects.all()
    if request.method == 'POST':
        Name = request.POST['name']
        Number = request.POST['number']
        Purpose = request.POST['purpose']
        Amount = request.POST['amount']
        pay = Payment.objects.create(Name=Name, Number=Number, Purpose=Purpose, Amount=Amount)
        pay.save()
        
        #Mpesa API
        token = ac_token()
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer %s' %token
        }
        payload = {
            "BusinessShortCode": 174379,
            "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMjMwMTA5MTI1NjU1",
            "Timestamp": "20230109125655",
            "TransactionType": "CustomerPayBillOnline",
            "Amount": Amount,
            "PartyA": Number,
            "PartyB": 174379,
            "PhoneNumber": Number,
            "CallBackURL": 'https://api.darajambili.com/express-payment',
            "AccountReference": Name + Purpose,
            "TransactionDesc": "Payment of X"
        }

        response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', headers = headers, json = payload)
        # print(response.text.encode('utf8'))
        code = response.json()
        try:
            if code['ResponseCode'] == '0':
                print("Successful!. Complete the pin prompt sent to your device")
                # payment = Payment.objects.update(Successful=True)
                # payment.save()
            else:
                print("Failed! Kindly try again.")
        except:
            'Message didnt work'
        # return code()

        messages.success(request, ("Your payment request has been sent successful!"))
        return redirect('/')
        
    context = {
        'Messages' : Week_Message.objects.filter(),
        'announcement' : Announcement.objects.all().order_by("-Date_posted")
    }


    return render(request=request,
                  template_name='main/home.html',
                  context= context)

def About(request):
    return render(request=request,
                  template_name='main/About.html')

def Activities(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save
            messages.success(request, ("You have book a slot successfully"))
            return redirect('/activities')

    activity = Activity.objects.all().order_by('-Date')
    activity_filter = ActivityFilter(request.GET, queryset=activity)

    form = BookingForm

    context = {
        'filter' : activity_filter,
        'form' : form
    }

    return render(request=request,
                  template_name='main/Activities.html',
                  context= context)
                  
def Families(request):
    join_family = Join_Family.objects.all()
    if request.method == 'POST':
        Name = request.POST['name']
        Number = request.POST['number']
        District = request.POST['district']
        join_family = Join_Family.objects.create(Name=Name, Number=Number, District=District)
        join_family.save()
        messages.success(request, ("Your application to this family has been received successfully"))
        return redirect('/')

    family = Family.objects.all()
    family_filter = FamilyFilter(request.GET, queryset=family)

    return render(request=request,
                  template_name='main/Families.html',
                  context={'filter':family_filter})
                  
def Sunday_Service(request):
    sermon = Sermon.objects.filter(Service="Sunday Service").order_by('-Date')
    sermon_filter = SermonFilter(request.GET, queryset=sermon)

    return render(request=request,
                  template_name='main/Sunday_Service.html',
                  context={'filter':sermon_filter})
                  
def Teams(request):
    join_team = Join_Team.objects.all()
    if request.method == 'POST':
        Name = request.POST['name']
        Number = request.POST['number']
        District = request.POST['district']
        join_team = Join_Team.objects.create(Name=Name, Number=Number, District=District)
        join_team.save()
        messages.success(request, ("Your application to the team has been received successfully"))
        return redirect('/')

    team = Team.objects.all()
    team_filter = TeamFilter(request.GET, queryset=team)

    return render(request=request,
                  template_name='main/Teams.html',
                  context={'filter':team_filter})
                  
def Tuesday_Service(request):
    sermon = Sermon.objects.filter(Service="Tuesday Service").order_by('-Date')
    sermon_filter = SermonFilter(request.GET, queryset=sermon)
    
    return render(request=request,
                  template_name='main/Tuesday_Service.html',
                  context={'filter': sermon_filter})

def Register(request):
    membership = Membership.objects.all()
    if request.method == 'POST':
        First_name = request.POST['first_name']
        Last_Name = request.POST['last_name']
        Gender = request.POST['gender']
        Number = request.POST['number']
        Area = request.POST['area']
        District = request.POST['district']
        membership = Membership.objects.create(First_name=First_name, Last_Name=Last_Name, Gender=Gender, Number=Number, Area=Area, District=District)
        Membership.objects.update(Confirmed=True)
        membership.save()
        messages.success(request, ("Your registration ha been received successfully"))
        return redirect('/')

    return render(request, "main/register.html")

def Schedules(request):
    schedules = Schedule.objects.all()
    if request.method == 'POST':
        Name = request.POST['name']
        Number = request.POST['number']
        District = request.POST['district']
        Person = request.POST['person']
        Date = request.POST['date']
        schedules = Schedule.objects.create(Name=Name, Number=Number, District=District, Person=Person, Date=Date)
        schedules.save()

        #sending an email
        send_mail(
            "Schedule appointment for " + Name, #subject
            "You have a new scheduled appointment with " + Name +" ( "+ "Phone number - " + Number +" )" + " from " + District + " on " +  Date +". Kindly confirm your availability. Thank you and have a blessed day.", #message
            "wahome4jeff@gmail.com", #from email
            ['jeffwahome2001@gmail.com'], #to email
        )

        return render(request, 'main/schedule.html', {'Name' : Name})

    return render(request, "main/schedule.html", )

  
                  