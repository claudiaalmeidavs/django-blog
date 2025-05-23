from django.db import models # Defines our model as an object
from django.conf import settings
from django.utils import timezone

class Post(models.Model): # models.Models means that the Post is a Django model, so Django knows that it should be saved in the database
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    abstract = models.TextField(max_length=500, default="")
    text = models.TextField() # This is for long text without a limit
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
