from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)

class Article(models.Model):
    id = models.IntegerField()
    board_key = models.IntegerField()
    board_type = models.CharField(max_length=45)
    num = models.IntegerField()
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    date = models.DateTimeField()
    reading = models.IntegerField()
    contents = models.TextField()

    class Meta:
    	db_table = "articles"

class Comment(models.Model):
    id = models.IntegerField()
    article_id = models.IntegerField()
    board_key = models.IntegerField()
    board_type = models.CharField(max_length=45)
    author = models.CharField(max_length=255)
    contents = models.TextField()
    datetime = models.DateTimeField()
    ip = models.CharField(max_length=45)

    class Meta:
    	db_table = "comments"

