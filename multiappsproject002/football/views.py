from django.shortcuts import render

# Create your views here.
def Football_Info(request):
    return render(request, 'football/footballdir.html')