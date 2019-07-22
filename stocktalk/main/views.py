from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import myusers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import pandas
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
from .forms import NewUserForm
from itertools import islice

x=[]
y=[]
# Create your views here.
def homepage(request):
    return render(request = request,
                  template_name='main/home.html',
                  context = {"myusers":myusers.objects.all})

def register(request):
    global x
    x *= 0
    global y
    y = 0

    if request.method == "POST":
        #print("if post")
        form =UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"new account created: {username}")
            login(request, user)
            return redirect("main:nextpage")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg} : {form.error_messages[msg]}")

            return render(request = request,
                          template_name = "main/register.html",
                          context={"form":form})
    #print("outside if")
    form = UserCreationForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return redirect("main:homepage")

def login_request(request):
    #print("inside login")
    if request.method == "POST":
        form=AuthenticationForm(request , data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as {username}")
                return redirect("main:nextpage")
            else:
                messages.error(request, f"Invalid username or password")
        else:
            messages.error(request, f"Invalid username or password")

    form=AuthenticationForm()
    return render(request,
                  "main/login.html",
                  {"form":form})

def next_page(request):
    if request.method == "POST":
        form=myusers(stock=request.POST["symbol"], uid=request.user)
        if form.stock == "A" or form.stock == "AAPL" or form.stock == "BRK.A" or form.stock == "C" or form.stock == "GOOG" or form.stock == "HOG" or form.stock == "HPQ" or form.stock == "INTC" or form.stock == "A" or form.stock == "KO" or form.stock == "LUV" or form.stock == "MMM" or form.stock == "MSFT" or form.stock == "T" or form.stock == "TGT" or form.stock == "TXN" or form.stock == "WMT":
            form.save()
            messages.info(request, f"done")
            ts = TimeSeries(key='2OZMWFTFF2DLF0TP', output_format='pandas')
            data, meta_data = ts.get_intraday(symbol=form.stock, interval='1min', outputsize='full')
            x.append(data.head(2).to_html())
            y.append(form.stock)
            l = len(y)
            return render( request, "main/nextpage.html",{"x":x, "n":y})
        else:
            messages.info(request, f"Invalid symbol")
            l=len(y)
            return render( request, "main/nextpage.html",{"x":x, "n":y})
    else:
        l = len(y)
        #global y
        return render( request, "main/nextpage.html",{"x":x, "n":y})

def userpage(request):
    aans={""}
    sa=myusers.objects.all()
    for x in sa:
        if x.uid == request.user :
            aans.add(x.stock)
    return render(request,"main/userpage.html", {"ans":aans})