from django.views.generic import TemplateView
from dos.form import *
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from dos.form import DosForm

# Create your views here.

def index (request):
    return HttpResponse("<h2> Formulaire Dos Enregistrer </h2>")

def ajout_dos(request):
    template_name = 'dos/dos_form.html'

    if request.method == 'POST':
        form = DosForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print("hello form is submitted")
            #form.save(commit=True)
        # form = DosForm()
            return HttpResponseRedirect(reversed('dos:index'))
    else:
        form=DosForm()
    return render(request, template_name, {'form': form})


class EnregistrementView(TemplateView):
        template_name='dos/dos_form.html'

        def get(self, request, *args, **kwargs):
            form=DosForm()
            return render(request, self.template_name, {'form': form})


        def post(self,request):

            if request.method == 'POST':
                form = DosForm(request.POST)
                # check whether it's valid:
                if form.is_valid():
                    print("hello form is submitted")
                   # form.save(commit=True)
                   # form = DosForm()
                    #return HttpResponse("<h2> Formulaire Dos Enregistrer </h2>")

                #return render(request, self.template_name, {'form': form})