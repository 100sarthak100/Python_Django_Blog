from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from tinymce.models import HTMLField


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = HTMLField('content')
    #content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

# class Comment(models.Model):
#     post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     content = models.TextField(max_length=200)
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return '{}-{}'.format(self.post.title, str(self.user.username))

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text