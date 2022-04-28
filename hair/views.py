from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'hair/home.html')
def contact(request):
    return render(request,'hair/contact.html')
def about(request):
    return render(request,'hair/about.html')
def price(request):
    return render(request,'hair/price.html')
def services(request):
    return render(request,'hair/services.html')
