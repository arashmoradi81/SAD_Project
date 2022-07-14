from django.shortcuts import render, redirect
from . import models
from .forms import PollForm, OpenEndForm, CloseTestForm


def HomePage(request):
    context = models.Poll.objects.all()
    return render(request, 'poll/home.html', {'context': context})


def CreateVote(request):
    form = PollForm()
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            form.save()
            return AddQuestion(request, models.Poll.objects.get(title=form.data['title']).id)
    context = {'form': form}
    return render(request, 'poll/create-vote.html', context)


def AddQuestion(request, pk):
    return render(request, 'poll/add-questions.html', {'id': pk})


def AddOpenEnd(request, pk):
    form = OpenEndForm(initial={'p_id': pk})
    if request.method == 'POST':
        form = OpenEndForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add-question', pk)
    context = {'form': form}
    return render(request, 'poll/open-end.html', context)
