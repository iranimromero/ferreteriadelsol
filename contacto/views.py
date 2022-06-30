from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic import View
from .models import Contacto
from .form import ContactoCreateForm

class ContactoView(View):
    def get(self, request, *args, **kwargs):
        form=ContactoCreateForm()
        context={
            'form':form
        }
        return render(request, 'contactanos.html', context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form=ContactoCreateForm(request.POST)
            if form.is_valid():
                 nombre = form.cleaned_data.get('nombre')
                 asunto = form.cleaned_data.get('asunto')
                 mail = form.cleaned_data.get('mail')
                 mensaje = form.cleaned_data.get('mensaje')

            p, created = Contacto.objects.get_or_create(nombre=nombre, asunto =asunto, mail =mail ,mensaje=mensaje)

            p.save()
            return redirect('contacto:home')
        else:
            form = ContactoCreateForm()
            return render(request, 'index.html', {'form':form})