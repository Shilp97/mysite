from django.conf import settings
from django.db import models
from django.utils import timezone
#from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
#from django.contrib.auth.models import User


STATUS_CHOICES = [
  ('d', 'Draft'),
   ('p', 'Published'), 
]

class Post(models.Model):

    
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField(blank = True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    image_post = models.ImageField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default = 'd')
 #   comm_count = models.IntegerField(blank=True, default = 0)

    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


#def save_post(sender, instance, **kwargs):
 #   print("save")


#pre_save.connect(save_post, sender=Post)      

#post_save.connect(save_post, sender=Post)      



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
 

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


#def comment_count(sender, **kwargs):
#    post = kwargs['instance'].post
#    post.comm_count = post.comm_count + 1
 #   post.save()
  #  print(post.comm_count)

#post_save.connect(comment_count, sender=Comment)  

class Image(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')


#class Profile(models.Model):
 #   user = models.OneToOneField(User, on_delete=models.CASCADE)
  #  bio = models.TextField(max_length=500, blank=True)
   # location = models.CharField(max_length=30, blank=True)
    #birth_date = models.DateField(null=True, blank=True)



    def __str__(self):
        return self.title




        