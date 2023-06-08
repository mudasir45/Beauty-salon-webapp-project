from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    discription = models.TextField(max_length=50, null=True, blank=True)
    services = models.ManyToManyField('services', blank=True)
    img = models.ImageField(upload_to="service", null=True, blank=True)
    
    def __str__(self) -> str:
        return self.title


class services(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    discription = models.TextField(max_length=50, null=True, blank=True)
    service_ctg = models.ForeignKey(category, related_name='cervice_category', on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    img = models.ImageField(upload_to="service", null=True, blank=True)
    tag = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
class order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.ForeignKey(services, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=50, null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.first_name} - {self.service.title}'

class serviceImages(models.Model):
    service = models.ForeignKey(services, on_delete=models.CASCADE, related_name="service_image")
    img = models.ImageField(upload_to="service")


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    CNIC = models.IntegerField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    adress = models.TextField(null=True, blank=True)
    is_employee = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.first_name} -- employee = {self.is_employee}'
    