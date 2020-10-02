from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError
from django.views import View

# Create your views here.
class Signup(View):
    template_name="todo/signupuser.html"
    form_class=UserCreationForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        form=self.form_class(data=request.POST)

        if not form.is_valid():
            return render(request, self.template_name, locals())

        user = form.save()
        login(request, user)
        return redirect('currenttodos')

def currenttodos(request):
    return render(request, 'todo/currenttodos.html')
