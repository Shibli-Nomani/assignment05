from django.shortcuts import render

# Create your views here.
def Cric_Info(request):
    return render(request, 'cricket/cricdir.html')
