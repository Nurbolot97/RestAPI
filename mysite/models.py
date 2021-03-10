from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import User
from my_user.models import User

class Company(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=25)
    info = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)


    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.company_name


class CompanyImages(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='logo')
    description = models.CharField(max_length=55)

    def __str__(self):
        if self.image:
            return self.image.url
        return ''


class Advertisement(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='ad_images', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - by {self.company}"























