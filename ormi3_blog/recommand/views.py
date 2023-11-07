from django.shortcuts import render

def recommand(request):
    return render(request, 'recommand/recommand.html')