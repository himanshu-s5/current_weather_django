from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import ImageModel, UserModel
from .forms import ImageForm, BmiForm, ContactForm, UserForm

import math
import json
import urllib.request


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        try:
            source = urllib.request.urlopen(
                'http://api.openweathermap.org/data/2.5/weather?q='
                + city + '&appid=b704b13900e2d6c5820c6d56d31a9ded&unit=metric').read()

            list_of_data = json.loads(source)
            temp = (list_of_data['main']['temp']) - 273.15
            temp = math.trunc(temp)
            feel_like = (list_of_data['main']['feels_like']) - 273.15
            feel_like = math.trunc(feel_like)

            cloud_image = str(list_of_data['weather'][0]['description'])
            print(cloud_image)
            visible = str(list_of_data['visibility'] // 1000)
            print(visible)
            data = {
                "name": str(list_of_data['name']),
                "country_code": str(list_of_data['sys']['country']),
                "temp": temp,
                "cloud_image": cloud_image,
                "feel_like": feel_like,
                "wind": str(list_of_data['wind']['speed']),
                "visibility": visible,
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
            }

        except Exception as e:

            error = {'error': e}
            return render(request, "index.html", error)

    else:
        data = {}

    return render(request, "index.html", data)


def home(request):
    return render(request, 'home/home.html')


def gallery(request):
    try:
        image_db = ImageModel.objects.all()
        if request.method == 'POST':
            form = ImageForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                messages.success(request, 'Your gallery is  successfully created !!')
                return redirect('gallery')
        else:

            form = ImageForm()
        return render(request, 'gallery/gallery.html', {'form': form, 'imagedb': image_db})
    except Exception as e:
        messages.warning(request, e)
        return render(request, 'galler.html')


def contactus(request):
    try:
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                messages.info(request, 'Your response has been sent')
                return redirect('home')
            else:
                messages.error(request, 'Not a valid credentials Try Again !!')

        else:
            form = ContactForm()
        return render(request, 'contact/contactus.html', {'form': form})
    except Exception as e:
        messages.warning(request, e)
        return render(request, 'contactus.html')


def aboutus(request):
    return render(request, 'about/aboutus.html')


def register(request):
    try:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                first_name = form.cleaned_data['First_name']
                last_name = form.cleaned_data['Last_name']
                user_name = form.cleaned_data['username']
                password = form.cleaned_data['password']
                email = form.cleaned_data['Email']
                user_db = User.objects.create_user(username=user_name, first_name=first_name,
                                                   last_name=last_name, email=email, password=password)
                user_db.save()

                messages.success(request, f'Your account has been created !')
                return redirect('login_page')
            else:
                messages.warning(request, 'Not a valid credential try again')
        else:
            form = UserForm()
        return render(request, 'register.html', {'form': form})
    except Exception as e:
        messages.warning(request, e)
        return render(request, 'register.html')


def login_page(request):
    try:
        redirect_to = request.GET.get('next')
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['pass1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Successfully logged in !!')
                return redirect(redirect_to)

            else:
                messages.warning(request, 'Username password are not match')
                return redirect('login_page')
        return render(request, 'login.html')
    except Exception as e:
        messages.warning(request, e)
        return render(request, 'login.html')


def log_out(request):
    try:
        redirect_to = request.GET.get('next')
        logout(request)
        messages.success(request, 'successfully log out')
        return redirect(redirect_to)
    except Exception as e:
        messages.warning(request, e)
        return render(request, 'login.html')


def bmi(request):
    if request.method == 'POST':
        form = BmiForm(request.POST)

        if form.is_valid():
            h = form.cleaned_data['height']
            w = form.cleaned_data['weight']
            height = h / 100
            bmi_cal = (w / (height * height))
            bmi_cal = '{:.2f}'.format(bmi_cal)
            param = {'form': form, 'bmi': bmi_cal}
            return render(request, 'bmi.html', param)
    else:
        form = BmiForm()
    return render(request, 'bmi.html', {'form': form})


def weather(request):
    return render(request, 'home/weather.html')


def global_w(request):
    return render(request, 'home/global.html')


def pop_n(request):
    return render(request, 'home/pop_n.html')


def forecast(request):
    return render(request, 'home/forecast.html')
