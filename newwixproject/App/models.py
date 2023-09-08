from django.db import models

class WebInfo(models.Model):
    userIPAddress = models.GenericIPAddressField()
    Website = models.URLField(null=True,blank=True)
    
    def __str__(self):
       
        return self.userIPAddress
    
class Entry(models.Model):
    Page = models.CharField(null=True,blank=True,max_length=10000)
    AccessTime = models.DateTimeField()
    userIPAddress = models.ForeignKey(WebInfo,null=True,blank=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Page
    
class Hover(models.Model):
    X = models.IntegerField(null=True,blank=True)
    Y = models.IntegerField(null=True,blank=True)
    page = models.CharField(null=True,blank=True,max_length=10000)
    type = models.CharField(null=True,blank=True,max_length=121212)
    Time = models.DateTimeField()
    Location = models.CharField(null=True,blank=True,default="None",max_length=100000)
    Information = models.CharField(max_length=1000000000,null=True,blank=True,default="None")
    userIPAddress = models.ForeignKey(WebInfo,null=True,blank=True,on_delete=models.CASCADE)

    
    
    def __str__(self):
        return self.page
    
    
class Click(models.Model):
    XC = models.IntegerField(null=True,blank=True)
    YC = models.IntegerField(null=True,blank=True)
    pageC = models.CharField(null=True,blank=True,max_length=10000)
    TimeC = models.DateTimeField()
    LocationC = models.CharField(null=True,blank=True,default="None",max_length=100000)
    typeC = models.CharField(null=True,blank=True,max_length=123124214)
    userIPAddress = models.ForeignKey(WebInfo,null=True,blank=True,on_delete=models.CASCADE)
    
    def __str__(self): 
        return self.pageC
    
class Pages(models.Model):
    First_Page = models.CharField(null=True,blank=True,max_length=10100101)
    Other_Pages = models.CharField(null=True,blank=True,max_length=124124124)
    FirstPageAccessTime = models.DateTimeField()
    userIPAddress = models.ForeignKey(WebInfo,null=True,blank=True,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.First_Page