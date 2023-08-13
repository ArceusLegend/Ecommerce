from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

#from orders.views import user_orders

from .forms import RegistrationForm
from .models import UserBase
from .tokens import account_activation_token

def account_register(request):
    
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.is_active=False
            user.save()
            #E-mail setup
            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('users/registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject=subject, message=message)
            return HttpResponse('registered succesfully and activation sent')
        
    else:
        registerForm = RegistrationForm()
    return render(request, 'users/registration/register.html', {'form': registerForm})

def account_activate(request, token, uidb64):
    try:
        print(urlsafe_base64_decode(uidb64).decode())
        uid = urlsafe_base64_decode(uidb64).decode()
        print('uid:', uid)
        user = UserBase.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, UserBase.DoesNotExist):
        user = None
    print(user)
    print(token)
    print(account_activation_token.check_token(user, token))
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('users:dashboard')
    else:
        return render(request, 'users/registration/activation_invalid.html')

@login_required
def dashboard(request):
    orders = user_orders(request)
    return render(
        request,
        'users/user/dashboard.html',
        {'section': 'profile', 'orders': orders}
    )

