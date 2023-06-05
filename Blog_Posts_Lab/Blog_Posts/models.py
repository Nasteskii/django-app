from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class EditUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to="files/")
    date_created = models.DateTimeField()
    last_modified = models.DateTimeField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    date_posted = models.DateField()
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    commented_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_author.username + " commented on " + self.commented_post.title
