from django.shortcuts import render
from django.http import HttpResponse
from .models import Company
from .forms import CompanyForm



def index(request):
    return render(request, 'templates/adminlte/index.html')


def create(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('company_index')
            except:
                pass
    else:
        form = CompanyForm()

    return render(request, "company_create.html", {'form': form})
