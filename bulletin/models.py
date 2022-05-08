from django.db import models
from accounts.models import User
# Create your models here.

# 게시판 피드 객체
class Post(models.Model):
    title       = models.CharField(max_length=255,  null=True)
    write_date  = models.DateTimeField(null=True)
    modify_date = models.DateTimeField(null=True, blank=True)
    content     = models.TextField(max_length=255,  null=True)
    user        = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    view_count  = models.PositiveIntegerField(default=0)
    
    def update_counter(self):
        self.view_count = self.view_count + 1
        self.save()


class Reply(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content    = models.TextField()
    user       = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)
    post       = models.ForeignKey(Post, on_delete=models.CASCADE, null = True)