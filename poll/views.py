from django.shortcuts import render, redirect
from . import models
from .forms import PollForm, OpenEndForm, CloseTestForm, OpenEndAnswerForm, CloseTestAnswerForm


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
        models.CloseTest.objects.create(p_id=models.Poll.objects.get(id=pk), question=form.data['question'],
                                        radio1=form.data['radio1'], radio2=form.data['radio2'],
                                        radio3=form.data['radio3'], radio4=form.data['radio4'])
        return redirect('add-question', pk)
    context = {'form': (form['question'], form['radio1'], form['radio2'], form['radio3'], form['radio4'])}
    return render(request, 'poll/close-test.html', context)


def FillPoll(request, pk):
    q = models.Poll.objects.get(id=pk).poll_openend.all()
    l = [OpenEndAnswerForm() for i in q]
    c = models.Poll.objects.get(id=pk).poll_closetest.all()
    f = [CloseTestAnswerForm() for i in c]
    if request.method == 'POST':
        if 'home' in request.POST:
            return redirect('home-page')
        for i in range(len(q)):
            if q[i].question in request.POST:
                l[i] = OpenEndAnswerForm(request.POST)
                models.OpenEnd_Answer.objects.create(q_id=q[i], answer=l[i].data['answer'])
            if c[i].question in request.POST:
                f[i] = CloseTestAnswerForm(request.POST)
                models.CloseTest_Answer.objects.create(q_id=c[i], answer=f[i].data['answer'])

    context = {'form1': ({'answer': l[i]['answer'], 'question': q[i].question} for i in range(len(l))), 'form2': (
        {'answer': f[i]['answer'], 'question': c[i].question, 'radio1': c[i].radio1, 'radio2': c[i].radio2,
         'radio3': c[i].radio3, 'radio4': c[i].radio4} for i in range(len(f)))}
    return render(request, 'poll/form-poll.html', context)


def ViewResult(request, pk):
    openends = models.Poll.objects.get(id=pk).poll_openend.all()
    questions = []
    answers = []
    for openend in openends:
        questions.append(openend.question)
        answers.append([])
        ans = openend.openToAnswer.all()
        for a in ans:
            answers[-1].append(a.answer)
    closetests = models.Poll.objects.get(id=pk).poll_closetest.all()
    for closetest in closetests:
        questions.append(closetest.question)
        answers.append([])
        ans = closetest.closeToAnswer.all()
        for a in ans:
            answers[-1].append(a.answer)

    context ={'form': ({'question': questions[i], 'answer': answers[i]} for i in range(len(questions)))}
    return render(request, 'poll/view-poll.html', context)
