from django.shortcuts import render, redirect
from .models import Reg
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.urls import reverse_lazy


def index(request):
    reg = Reg()
    if request.method == 'POST':
        print(request.POST.get("name"))
        reg.name = request.POST.get("name")
        reg.email = request.POST.get("email")
        reg.save()
        return redirect('index')
    return render(request, 'index.html')

# def register(request):
#     regs = Reg.objects.all()
#     reg = Reg()
#     try:
#         if request.method == 'POST':
#             print(request.POST.get("name"))
#             reg.name = request.POST.get("name")
#             reg.email = request.POST.get("email")
#             reg.save()
#     except:
#         return render(request, 'register.html', {"regs": regs})
#     return render(request, 'register.html', {"regs": regs})

# class register(CreateView):
#     model = Reg
#     fields = ['name', 'email']
#     template_name = 'register.html'
#     success_url = reverse_lazy('register')

class Register(View):
    def get(self, request):
        regs = Reg.objects.all()
        return render(request, 'register.html', {"regs": regs})
   
# def register(request):
#     regs = Reg.objects.all()
#     reg = Reg()
#     try:
#         if request.method == 'POST':
#             print(request.POST.get("name"))
#             reg.name = request.POST.get("name")
#             reg.email = request.POST.get("email")
#             reg.save()
#     except:
#         return render(request, 'register.html', {"regs": regs})
#     return render(request, 'register.html', {"regs": regs})