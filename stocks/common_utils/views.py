from django.shortcuts import render


# Create your views here.
def health_check(request):
    return render(request, 'health_check.html')