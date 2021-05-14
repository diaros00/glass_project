from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Defect(models.Model):
    defect_name = models.CharField(max_length=200)

class UserProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    department = models.CharField(max_length=200)
    shift = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username

class modelGlass(models.Model):
    model_code = models.CharField(max_length=200)
    model_name = models.CharField(max_length=200)
    model_desc = models.CharField(max_length=200,null=True)
    model_image = models.ImageField(upload_to='image/', null=True, verbose_name="")

    def __str__(self):
        return self.model_name + ": " + str(self.model_image)
 





    
