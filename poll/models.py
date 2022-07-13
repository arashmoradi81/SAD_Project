from django.db import models
import uuid


class Poll(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(blank=False, null=False, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    expired_datetime = models.DateTimeField()

    def __str__(self):
        return self.title


class OpenEnd(models.Model):
    p_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    question = models.CharField(blank=False, null=False, max_length=200)

    def __str__(self):
        return self.question


class OpenEnd_Answer(models.Model):
    q_id = models.ForeignKey(OpenEnd, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.answer


class CloseTest(models.Model):
    p_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    question = models.CharField(blank=False, null=False, max_length=200)
    radio1 = models.CharField(blank=True, null=True, max_length=200)
    radio2 = models.CharField(blank=True, null=True, max_length=200)
    radio3 = models.CharField(blank=True, null=True, max_length=200)
    radio4 = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.question


radios = (
    ('radio1', ),
    ('radio2', ),
    ('radio3', ),
    ('radio4', ),
)
class CloseTest_Answer(models.Model):
    q_id = models.ForeignKey(CloseTest, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    answer = models.CharField(max_length=200, choices=radios)

    def __str__(self):
        return self.answer

