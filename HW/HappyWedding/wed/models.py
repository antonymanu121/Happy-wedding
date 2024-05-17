from django.db import models

 

 
class vendorcategory(models.Model):
    name=models.CharField(max_length=30)
    photo=models.ImageField(upload_to="images",null=True)




    
    def __str__(self):
        return self.name
    
    

class district(models.Model):
    name=models.CharField(max_length=30)

    
    
    def __str__(self):
        return self.name
    
class vendors(models.Model):
    username=models.CharField(max_length=30,null=False,blank=False)
    District=models.ForeignKey(district,on_delete=models.CASCADE,null=True)
    phone_number= models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=30,null=False)

    def __str__(self):
        return self.username
    

class vendorlisting(models.Model):
    Name=models.CharField(max_length=30)
    vendor = models.ForeignKey(vendors, on_delete=models.CASCADE)
    category = models.ForeignKey(vendorcategory, on_delete=models.CASCADE,null=True,blank=False)
    company_name=models.CharField(max_length=30)
    About=models.TextField(max_length=1000,null=False,blank=False)
    District=models.ForeignKey(district,on_delete=models.CASCADE,null=True)
    address = models.CharField(max_length=200)
    package=models.IntegerField(null=True)
    image=models.ImageField(upload_to="image",null=False)
   

    def __str__(self):
        return self.Name
    


    

class enquiry(models.Model):
    Name=models.CharField(max_length=30)
    vendor=models.ForeignKey(vendors,on_delete=models.CASCADE)
    phone_number= models.CharField(max_length=20)
    district=models.ForeignKey(district,on_delete=models.CASCADE,null=True)
    Event_date=models.CharField(max_length=20)
    Event_detail=models.TextField(max_length=2000)


    def __str__(self):
        return self.Name




    
    























    



    







    

