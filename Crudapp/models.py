from django.db import models


class Streamplatform(models.Model):
    name = models.CharField(max_length=50)
    about = models.CharField(max_length=50)
    website = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=50)
    stroyline=models.TextField()
    platform=models.ForeignKey(Streamplatform,on_delete=models.CASCADE)
    active=models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
