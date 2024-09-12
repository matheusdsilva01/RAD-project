from django.shortcuts import render
from django.views.generic import ListView, CreateView, View
from django.urls import reverse_lazy
from .models import Client
from datetime import datetime
from django.shortcuts import redirect

def home(request):
    # return render(request, 'home.html')
    return render(request, 'garage/home.html')

class ClientListView(ListView):
    model = Client

class CreateClientView(CreateView):
    model = Client
    fields = ['name', 'email', 'phone', 'address', 'vehicle']
    success_url = reverse_lazy('clients')

class ClientExitView(View):
    def get(self, request, pk):
        client = Client.objects.get(pk=pk)
        client.departureDate = datetime.now()
        client.save()
        return redirect('clients')