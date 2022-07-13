from django.shortcuts import render


def HomePage(request):
    return render(request, 'poll/home.html')

def CreateVote(request):
    pass
