from django.shortcuts import render

# Create your views here.

def index_view(request):
    context={
        'app':"App is ready",
    }
    return render(request,'index.html', context)