import email
from pyexpat import model
from django.db import models
# Create your models here.

class Resume(models.Model):
    STATE_CHOICE=(
    ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("MH","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal")
    )
    name=models.CharField(max_length=70)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    gender=models.CharField(max_length=10)
    locality=models.CharField(max_length=70)
    city=models.CharField(max_length=20)
    pin=models.PositiveIntegerField()
    state=models.CharField(choices=STATE_CHOICE,max_length=2)
    mobile=models.PositiveIntegerField()
    email=models.EmailField(max_length=100)
    job_city=models.CharField(max_length=70)
    profile_image=models.ImageField(upload_to='profileimg/',blank=True)
    my_file=models.FileField(upload_to='doc/',blank=True)