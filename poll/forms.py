from django.forms import ModelForm
from .models import Poll, OpenEnd, CloseTest


class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['title', 'expired_datetime']

    def __init__(self, *args, **kwargs):
        super(PollForm, self).__init__(*args, **kwargs)


class OpenEndForm(ModelForm):
    class Meta:
        model = OpenEnd
        fields = ['question', 'p_id']

    def __init__(self, *args, **kwargs):
        super(OpenEndForm, self).__init__(*args, **kwargs)


class CloseTestForm(ModelForm):
    class Meta:
        model = CloseTest
        fields = ['question', 'radio1', 'radio2', 'radio3', 'radio4']

    def __init__(self, *args, **kwargs):
        super(CloseTestForm, self).__init__(*args, **kwargs)