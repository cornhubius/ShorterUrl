from django.http.response import HttpResponseNotFound
from django.shortcuts import redirect, render
import shortuuid
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from shorturl.forms import New_link
from shorturl.models import Links
from django.contrib.auth.models import User


def redirect_long(request, short):
    long = Links.objects.get(short_link=short).link
    return redirect(long)


def create_short(request):
    if request.method == 'POST':
        form = New_link(request.POST)
        host = request.build_absolute_uri('/')
        if form.is_valid():
            try:
                print(form.cleaned_data['link'])
                check=Links.objects.get(link=form.cleaned_data['link'])
                return render(request, 'create_short.html', {'short': check.short_link, 'host': host})
            except Exception:
                short = shortuuid.uuid()[:8]
                user = User.objects.get(id=request.user.id)
                Links.objects.create(**form.cleaned_data,
                                 short_link=short, id_admin=user)
                return render(request, 'create_short.html', {'short': short, 'host': host})    
    else:
        form = New_link()
    return render(request, 'create_short.html', {'form': form})


def link_list(request):
    links = Links.objects.filter(id_admin=request.user.id)
    short_link = [x.short_link for x in links]
    long_link = [x.link for x in links]
    host = request.get_host()
    return render(request, 'link_list.html', {'short': short_link, 'long': long_link, 'host': host})


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/login/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
