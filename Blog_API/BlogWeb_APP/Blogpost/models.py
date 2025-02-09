from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# create models for blogpost..
class blogpost(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    is_published=models.BooleanField(default=False)
    total_likes=models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
# create models for Comments for blogpost..
class Comment(models.Model):
    comment_user=models.ForeignKey(User,on_delete=models.CASCADE)
    likes=models.PositiveIntegerField(default=0,validators=[MinValueValidator(0),MaxValueValidator(1)])
    comments=models.TextField()
    blogpost=models.ForeignKey(blogpost,on_delete=models.CASCADE,related_name="comments")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.likes)+"|"+self.blogpost.title
