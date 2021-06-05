from django.db import models
from django.contrib.auth.models import User
from datetime import datetime




# Create your models here.
class Defect(models.Model):
    defect_name = models.CharField(max_length=200,null=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    department = models.CharField(max_length=200,null=True)
    shift = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.user.username

class modelGlass(models.Model):
    model_code = models.CharField(max_length=200,null=True)
    model_name = models.CharField(max_length=200,null=True)
    model_desc = models.CharField(max_length=200,null=True)
    model_image = models.ImageField(upload_to='image/', null=True, verbose_name="")

    def __str__(self):
        return self.model_name + ": " + str(self.model_image)

class modelGlassWithDefect(models.Model):
    
    date_create = models.DateTimeField(default=datetime.now, blank=True)

    model_code = models.CharField(max_length=200,null=True)
    model_name = models.CharField(max_length=200,null=True)
    model_desc = models.CharField(max_length=200,null=True)
    defect_name1 = models.CharField(max_length=200,null=True)
    defect_name2 = models.CharField(max_length=200,null=True)
    defect_name3 = models.CharField(max_length=200,null=True)
    defect_name4 = models.CharField(max_length=200,null=True)
    defect_name5 = models.CharField(max_length=200,null=True)
    department = models.CharField(max_length=200,null=True)
    point_defect = models.CharField(max_length=200,null=True)
    date_select = models.DateField()
    shift = models.CharField(max_length=200,null=True)
    number_glass = models.CharField(max_length=200,null=True)
    status_glass = models.CharField(max_length=200,null=True)
    
    
# class modelGlassWithDefect_for_export(models.Model):
    
#     date_create = models.DateTimeField(default=datetime.now, blank=True)
#     model_code = models.TextField(null=True)
#     model_name = models.TextField(null=True)
#     model_desc = models.TextField(null=True)
#     shift = models.TextField(null=True)
#     number_glass = models.TextField(null=True)
#     status_glass = models.TextField(null=True)
#     date_select = models.DateField()
#     department = models.TextField(null=True)

#     point_1_defect_name_1 = models.TextField(null=True)
#     point_1_defect_name_2 = models.TextField(null=True)
#     point_1_defect_name_3 = models.TextField(null=True)
#     point_1_defect_name_4 = models.TextField(null=True)
#     point_1_defect_name_5 = models.TextField(null=True)

#     point_2_defect_name_1 = models.TextField(null=True)
#     point_2_defect_name_2 = models.TextField(null=True)
#     point_2_defect_name_3 = models.TextField(null=True)
#     point_2_defect_name_4 = models.TextField(null=True)
#     point_2_defect_name_5 = models.TextField(null=True)

#     point_3_defect_name_1 = models.TextField(null=True)
#     point_3_defect_name_2 = models.TextField(null=True)
#     point_3_defect_name_3 = models.TextField(null=True)
#     point_3_defect_name_4 = models.TextField(null=True)
#     point_3_defect_name_5 = models.TextField(null=True)

#     point_4_defect_name_1 = models.TextField(null=True)
#     point_4_defect_name_2 = models.TextField(null=True)
#     point_4_defect_name_3 = models.TextField(null=True)
#     point_4_defect_name_4 = models.TextField(null=True)
#     point_4_defect_name_5 = models.TextField(null=True)

#     point_5_defect_name_1 = models.TextField(null=True)
#     point_5_defect_name_2 = models.TextField(null=True)
#     point_5_defect_name_3 = models.TextField(null=True)
#     point_5_defect_name_4 = models.TextField(null=True)
#     point_5_defect_name_5 = models.TextField(null=True)

#     point_6_defect_name_1 = models.TextField(null=True)
#     point_6_defect_name_2 = models.TextField(null=True)
#     point_6_defect_name_3 = models.TextField(null=True)
#     point_6_defect_name_4 = models.TextField(null=True)
#     point_6_defect_name_5 = models.TextField(null=True)

#     point_7_defect_name_1 = models.TextField(null=True)
#     point_7_defect_name_2 = models.TextField(null=True)
#     point_7_defect_name_3 = models.TextField(null=True)
#     point_7_defect_name_4 = models.TextField(null=True)
#     point_7_defect_name_5 = models.TextField(null=True)

#     point_8_defect_name_1 = models.TextField(null=True)
#     point_8_defect_name_2 = models.TextField(null=True)
#     point_8_defect_name_3 = models.TextField(null=True)
#     point_8_defect_name_4 = models.TextField(null=True)
#     point_8_defect_name_5 = models.TextField(null=True)

#     point_9_defect_name_1 = models.TextField(null=True)
#     point_9_defect_name_2 = models.TextField(null=True)
#     point_9_defect_name_3 = models.TextField(null=True)
#     point_9_defect_name_4 = models.TextField(null=True)
#     point_9_defect_name_5 = models.TextField(null=True)

#     point_10_defect_name_1 = models.TextField(null=True)
#     point_10_defect_name_2 = models.TextField(null=True)
#     point_10_defect_name_3 = models.TextField(null=True)
#     point_10_defect_name_4 = models.TextField(null=True)
#     point_10_defect_name_5 = models.TextField(null=True)

#     point_11_defect_name_1 = models.TextField(null=True)
#     point_11_defect_name_2 = models.TextField(null=True)
#     point_11_defect_name_3 = models.TextField(null=True)
#     point_11_defect_name_4 = models.TextField(null=True)
#     point_11_defect_name_5 = models.TextField(null=True)

#     point_12_defect_name_1 = models.TextField(null=True)
#     point_12_defect_name_2 = models.TextField(null=True)
#     point_12_defect_name_3 = models.TextField(null=True)
#     point_12_defect_name_4 = models.TextField(null=True)
#     point_12_defect_name_5 = models.TextField(null=True)

#     point_13_defect_name_1 = models.TextField(null=True)
#     point_13_defect_name_2 = models.TextField(null=True)
#     point_13_defect_name_3 = models.TextField(null=True)
#     point_13_defect_name_4 = models.TextField(null=True)
#     point_13_defect_name_5 = models.TextField(null=True)

#     point_14_defect_name_1 = models.TextField(null=True)
#     point_14_defect_name_2 = models.TextField(null=True)
#     point_14_defect_name_3 = models.TextField(null=True)
#     point_14_defect_name_4 = models.TextField(null=True)
#     point_14_defect_name_5 = models.TextField(null=True)

#     point_15_defect_name_1 = models.TextField(null=True)
#     point_15_defect_name_2 = models.TextField(null=True)
#     point_15_defect_name_3 = models.TextField(null=True)
#     point_15_defect_name_4 = models.TextField(null=True)
#     point_15_defect_name_5 = models.TextField(null=True)

#     point_16_defect_name_1 = models.TextField(null=True)
#     point_16_defect_name_2 = models.TextField(null=True)
#     point_16_defect_name_3 = models.TextField(null=True)
#     point_16_defect_name_4 = models.TextField(null=True)
#     point_16_defect_name_5 = models.TextField(null=True)

#     point_17_defect_name_1 = models.TextField(null=True)
#     point_17_defect_name_2 = models.TextField(null=True)
#     point_17_defect_name_3 = models.TextField(null=True)
#     point_17_defect_name_4 = models.TextField(null=True)
#     point_17_defect_name_5 = models.TextField(null=True)

#     point_18_defect_name_1 = models.TextField(null=True)
#     point_18_defect_name_2 = models.TextField(null=True)
#     point_18_defect_name_3 = models.TextField(null=True)
#     point_18_defect_name_4 = models.TextField(null=True)
#     point_18_defect_name_5 = models.TextField(null=True)

#     point_19_defect_name_1 = models.TextField(null=True)
#     point_19_defect_name_2 = models.TextField(null=True)
#     point_19_defect_name_3 = models.TextField(null=True)
#     point_19_defect_name_4 = models.TextField(null=True)
#     point_19_defect_name_5 = models.TextField(null=True)

#     point_20_defect_name_1 = models.TextField(null=True)
#     point_20_defect_name_2 = models.TextField(null=True)
#     point_20_defect_name_3 = models.TextField(null=True)
#     point_20_defect_name_4 = models.TextField(null=True)
#     point_20_defect_name_5 = models.TextField(null=True)

#     point_21_defect_name_1 = models.TextField(null=True)
#     point_21_defect_name_2 = models.TextField(null=True)
#     point_21_defect_name_3 = models.TextField(null=True)
#     point_21_defect_name_4 = models.TextField(null=True)
#     point_21_defect_name_5 = models.TextField(null=True)

#     point_22_defect_name_1 = models.TextField(null=True)
#     point_22_defect_name_2 = models.TextField(null=True)
#     point_22_defect_name_3 = models.TextField(null=True)
#     point_23_defect_name_4 = models.TextField(null=True)
#     point_23_defect_name_5 = models.TextField(null=True)

#     point_24_defect_name_1 = models.TextField(null=True)
#     point_24_defect_name_2 = models.TextField(null=True)
#     point_24_defect_name_3 = models.TextField(null=True)
#     point_24_defect_name_4 = models.TextField(null=True)
#     point_24_defect_name_5 = models.TextField(null=True)

#     point_25_defect_name_1 = models.TextField(null=True)
#     point_25_defect_name_2 = models.TextField(null=True)
#     point_25_defect_name_3 = models.TextField(null=True)
#     point_25_defect_name_4 = models.TextField(null=True)
#     point_25_defect_name_5 = models.TextField(null=True)

#     point_26_defect_name_1 = models.TextField(null=True)
#     point_26_defect_name_2 = models.TextField(null=True)
#     point_26_defect_name_3 = models.TextField(null=True)
#     point_26_defect_name_4 = models.TextField(null=True)
#     point_26_defect_name_5 = models.TextField(null=True)

#     point_27_defect_name_1 = models.TextField(null=True)
#     point_27_defect_name_2 = models.TextField(null=True)
#     point_27_defect_name_3 = models.TextField(null=True)
#     point_27_defect_name_4 = models.TextField(null=True)
#     point_27_defect_name_5 = models.TextField(null=True)

#     point_28_defect_name_1 = models.TextField(null=True)
#     point_28_defect_name_2 = models.TextField(null=True)
#     point_28_defect_name_3 = models.TextField(null=True)
#     point_28_defect_name_4 = models.TextField(null=True)
#     point_28_defect_name_5 = models.TextField(null=True)

#     point_29_defect_name_1 = models.TextField(null=True)
#     point_29_defect_name_2 = models.TextField(null=True)
#     point_29_defect_name_3 = models.TextField(null=True)
#     point_29_defect_name_4 = models.TextField(null=True)
#     point_29_defect_name_5 = models.TextField(null=True)

#     point_30_defect_name_1 = models.TextField(null=True)
#     point_30_defect_name_2 = models.TextField(null=True)
#     point_30_defect_name_3 = models.TextField(null=True)
#     point_30_defect_name_4 = models.TextField(null=True)
#     point_30_defect_name_5 = models.TextField(null=True)

#     point_31_defect_name_1 = models.TextField(null=True)
#     point_31_defect_name_2 = models.TextField(null=True)
#     point_31_defect_name_3 = models.TextField(null=True)
#     point_31_defect_name_4 = models.TextField(null=True)
#     point_31_defect_name_5 = models.TextField(null=True)

#     point_32_defect_name_1 = models.TextField(null=True)
#     point_32_defect_name_2 = models.TextField(null=True)
#     point_32_defect_name_3 = models.TextField(null=True)
#     point_32_defect_name_4 = models.TextField(null=True)
#     point_32_defect_name_5 = models.TextField(null=True)

#     point_33_defect_name_1 = models.TextField(null=True)
#     point_33_defect_name_2 = models.TextField(null=True)
#     point_33_defect_name_3 = models.TextField(null=True)
#     point_33_defect_name_4 = models.TextField(null=True)
#     point_33_defect_name_5 = models.TextField(null=True)

#     point_34_defect_name_1 = models.TextField(null=True)
#     poin
    
 





    
