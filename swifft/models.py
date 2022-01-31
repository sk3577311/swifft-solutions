from django.db import models
from ckeditor.fields import RichTextField



class contactus(models.Model):
    Username = models.CharField(max_length=50,null=True)
    Email = models.EmailField(max_length=100,null=True)
    Subject = models.CharField(max_length=50,null=True)
    Details = RichTextField(max_length=50,null=True)
    Phone_no = models.CharField(max_length = 100 ,null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.Username

# Create your models here.
