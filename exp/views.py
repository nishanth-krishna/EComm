from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse_lazy

# Create your views here.
class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'exp/index.html')
    def post(self, request):
        return render()

class FirstView(View):
    def get(self, request):
        return render(request, 'exp/first.html')
    def post(self, request):
        return render()

class SignUp(View):
    def get(self, request):
        return render(request, 'exp/signup.html')
    def post(self, request):
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        #messages.success(request, 'your acc has been successfully created.')
        #myuser.is_active=False
        return redirect(reverse_lazy('exp:first'))