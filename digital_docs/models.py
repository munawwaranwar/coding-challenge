from django.db import models


class Topic(models.Model):
    topic_name = models.CharField(max_length=50)
    decription = models.TextField()


class Folder(models.Model):
    folder_name = models.CharField(max_length=50)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)


class Document(models.Model):
    document_name = models.CharField(max_length=50)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
