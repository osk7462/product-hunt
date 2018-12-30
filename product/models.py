from django.db import models
from django.contrib.auth.models import User


class product(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    icom = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title


    def summary(Self):
        return self.body[:200]

    def publiction_date(self):
        return self.pub_date.strftime('%b %e %Y')
