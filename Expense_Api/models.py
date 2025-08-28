from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Expense(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return f"{self.category} - ₹{self.amount}"
      
class ExpensePage(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return f"{self.category} - ₹{self.amount}"