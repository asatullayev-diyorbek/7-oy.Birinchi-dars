from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import RegisterForm, LoginForm
from .models import Confirmation


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context = {
            'form': form,
            'title': 'Ro\'yxatdan o\'tish'
        }
        return render(request,'register/register.html', context)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                is_active=False,
            )

            confirmation_code = Confirmation.generate_confirmation_code()
            confirmation = Confirmation.objects.create(
                email=user.email,
                confirmation_code=confirmation_code
            )

            send_mail(
                f"Xush kelibsiz {user.get_full_name()}",
                f'Sizning ro\'yxatdan o\'tishni yakunlash uchun linkingiz: http://127.0.0.1:8000/auth/confirmation/?email={user.email}&confirmation_code={confirmation.confirmation_code}',
                'noreply@localhost',
                [user.email]
            )
            messages.success(request, f"Ro'yxatdan o'tishni yakunlash uchun {form.cleaned_data['email']} elektron pochtasiga yuborilgan link ustiga bosing")
            return redirect('register:register')
        else:
            context = {
                'form': form,
                'title': 'Ro\'yxatdan o\'tish'
            }
            return render(request, 'register/register.html', context)


class ConfirmationView(View):
    def get(self, request):
        email = request.GET.get('email')
        confirmation_code = request.GET.get('confirmation_code')

        if email and confirmation_code:
            confirmation = Confirmation.objects.filter(email=email, confirmation_code=confirmation_code).first()
            if confirmation:
                user = User.objects.get(email=email)
                user.is_active = True
                user.save()
                confirmation.delete()
                login(request, user)
                send_mail(
                    f'Sizning ro\'yxatdan o\'tishingiz muvaffaqiyatli tugatildi!',
                    f"Sizni saytimizdan to'liq ro'yxatdan o'tganingiz bilan tabriklaymiz",
                    'noreply@localhost',
                    [user.email]
                )
                messages.success(request, f"Sizning ro'yxatdan o'tishningiz muvaffaqiyatli tugatildi!")
            else:
                messages.error(request, "Nimadur xato ketdi!")
        return redirect('news:index')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            'form': form,
            'title': 'Kirish'
        }
        return render(request, 'register/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            login(request, form.cleaned_data['user'])
            messages.success(request, "Siz tizimga kirdingiz!")
            return redirect('news:index')
        context = {
            'form': form,
            'title': "Kirish"
        }
        return render(request, 'register/login.html', context)


def logout_user(request):
    logout(request)
    messages.warning(request, "Siz tizimdan chiqdingiz!")
    return redirect('register:login')

