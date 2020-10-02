from django.shortcuts import render, redirect, resolve_url
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.views.generic.edit import FormMixin, CreateView
from django.urls import reverse_lazy

# Create your views here.
class Signup(CreateView):
    template_name="todo/signupuser.html"
    form_class=UserCreationForm
    success_url=reverse_lazy('currenttodos')

    def form_valid(self, form):
        result=super().form_valid(form)

        login(self.request, self.object)

        return result

def currenttodos(request):
    return render(request, 'todo/currenttodos.html')
