from django.db import models


class Mess(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    status = models.PositiveSmallIntegerField(choices=[(1, 'Send'), (2, 'Wait')], default=2)

    def __str__(self):
        return f'{self.title} ({self.status})'


class SendTo(models.Model):
    mail = models.EmailField()

    def __str__(self):
        return self.mail