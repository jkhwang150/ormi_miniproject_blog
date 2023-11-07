from django.db import models
class Board(models.Model):
    author = models.CharField(max_length=10, null=True)
    title = models.CharField(max_length=100, null=True)
    content = models.TextField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    comment = models.TextField()
    
    post = models.ForeignKey('Board', null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)