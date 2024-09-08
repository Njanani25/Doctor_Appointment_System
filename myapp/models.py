from django.db import models


class Userdata(models.Model):
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.email
    
class Doctorinfo(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_img=models.ImageField(upload_to='doctors/')
    doc_spec=models.TextField()

    def __str__(self):
        return self.doc_name

class Appointmentinfo(models.Model):
    user = models.ForeignKey(Userdata,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctorinfo,on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.IntegerField()
    date_time = models.CharField(max_length=100)
    symptoms = models.TextField()

    def _str_(self):
        return self.patient_name
