from django.shortcuts import render

# Create your views here.
def Basket_Info(request):
    return render(request, 'basketball/basketdir.html')

