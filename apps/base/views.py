from django.shortcuts import render, redirect
from .models import *
from apps.telegram_bot.views import send_message
from django.core.mail import send_mail

# Create your views here.
def index(request):
    title = "Geeks"
    settings = Settings.objects.latest('id')
    data = Data.objects.latest("id")
    return render(request, 'base/index.html', locals())

def contact(request):
    settings = Settings.objects.latest('id')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        cause = request.POST.get('cause')
        message = request.POST.get('message')
        Contact.objects.create(name=name, phone=phone, email=email, cause=cause, message=message,)

        send_message(
            f"""
имя пользователя - {name}
почта (email) - {email}
номер телефона - {phone}
причина - {cause}
сообщение - {message}"""
        )

        send_mail("Новый отзыв", f"Сообщение - {message}", "abdykadyrovsyimyk0708@gmail.com", [email])

        return redirect('index')
    return render(request, 'base/contact.html', locals())
