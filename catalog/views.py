from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def hom(request):
    return render(request, 'contacts.html')
