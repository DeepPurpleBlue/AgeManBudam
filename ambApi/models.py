from django.db import models

# Create your models here.
class Post(models.Model):
    text=models.CharField(max_length=100)
    likes=models.IntegerField()
    def increment(self):
        #current_like=self.like
        #incremented_like=current_like+1
        nlikes=self.likes+1
        self.likes=nlikes
        self.save()
        #Post.objects.get(id=self.id)
    def __str__(self):
        return self.text
    def as_dict(self):
        return dict(
            post_id=self.id,
            post_text=self.text,
            post_likes=self.likes)