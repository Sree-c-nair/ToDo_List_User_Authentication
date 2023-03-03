from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django .contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.views import LoginView
from .forms import RegisterForm

from .models import Tasks
# Create your views here.


def Home(request):
    return render(request,'home.html')


class TaskList(ListView):
    model = Tasks
    context_object_name = 'task1'
    template_name = 'tasklist.html'


class TaskCreate(CreateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('task1')
    template_name = 'taskcreate.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request,'The task was created successfully..')
        return super(TaskCreate,self).form_valid(form)


class TaskUpdate(UpdateView):
    model = Tasks
    fields = '__all__'
    success_url = reverse_lazy('task1')
    template_name = 'taskcreate.html'


class TaskDelete(DeleteView):
    model= Tasks
    fields = '__all__'
    success_url = reverse_lazy('task1')
    template_name = 'taskdelete.html'


class TaskDetailView(DetailView):
    model = Tasks
    # context_object_name = 'task1'
    # success_url = reverse_lazy('task1')
    template_name = 'taskdetail.html'


def login_user (request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:# if user exist
			login(request, user)
			messages.success(request,('Youre logged in'))
			return redirect('home')
		else:
			messages.success(request,('Error logging in'))
			return redirect('login')
	else:
		return render(request, 'login.html', {})


def logout_user(request):
	logout(request)
	messages.success(request,('Youre now logged out'))
	return redirect('home')


def register_user(request):

	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ( 'Youre now registered' ))
			return redirect('home')
	else:
		form = RegisterForm()

	context = {'form': form}
	return render(request, 'register1.html', context)


def change_password(request):

	if request.method =='POST':
		form = PasswordChangeForm(data=request.POST, user= request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('You have edited your password'))
			return redirect('home')
	else:
		form = PasswordChangeForm(user= request.user)

	context = {'form': form}
	return render(request, 'change_password.html', context)
	context = {'form': form}
	return render(request, 'change_password.html', context)