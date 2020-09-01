from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BlogManager(models.Manager):
    def latest_all_blog(self):
        return self.all().order_by('created_at')
    def getone(self,id:int):
        return self.get(id=id)
    def createBlog(self,**kwargs):
        return self.create(title=kwargs['title'],body=kwargs['body'],user=kwargs['user'])
    def delete(self,id:int):
        return self.getone(id).delete()
class blog(models.Model):
    bid=models.BigAutoField().primary_key=True
    title=models.CharField(max_length=225)
    body=models.TextField()
    created_at=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,models.CASCADE,related_name='edit_post')
    objects=BlogManager()
    
    def __str__(self):
        return self.title
