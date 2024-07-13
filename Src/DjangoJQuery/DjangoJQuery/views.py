from django.shortcuts import render

def Home(request):
    template = 'index.html'
    context = {
        'Text': 'Hello world!'
    }
    return render(request, template, context)