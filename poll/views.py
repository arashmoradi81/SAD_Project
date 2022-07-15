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
            return AddQuestion(request, models.Poll.objects.last().id)
    context = {'form': form}
    return render(request, 'poll/create-vote.html', context)


def AddQuestion(request, pk):
    return render(request, 'poll/add-questions.html', {'id': pk})


def AddOpenEnd(request, pk):
    form = OpenEndForm()
    if request.method == 'POST':
        form = OpenEndForm(request.POST)
        models.OpenEnd.objects.create(p_id=models.Poll.objects.get(id=pk), question=form.data['question'])
        return redirect('add-question', pk)
    context = {'form': form['question']}
    return render(request, 'poll/open-end.html', context)


def AddCloseTest(request, pk):
    form = CloseTestForm()
    if request.method == 'POST':
        form = CloseTestForm(request.POST)
        models.CloseTest.objects.create(p_id=models.Poll.objects.get(id=pk), question=form.data['question'], radio1=form.data['radio1'], radio2=form.data['radio2'], radio3=form.data['radio3'], radio4=form.data['radio4'])
        return redirect('add-question', pk)
    context = {'form': (form['question'], form['radio1'], form['radio2'], form['radio3'], form['radio4'])}
    return render(request, 'poll/close-test.html', context)
