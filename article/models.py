from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name
class Article(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='articles')