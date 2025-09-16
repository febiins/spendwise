from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Category(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    class Meta:
        unique_together=('user','name')
    def __str__(self):
        return self.name

class Expense(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    category= models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    amount= models.DecimalField(max_digits=10, decimal_places=2)
    note = models.CharField(max_length=200,blank=True) 
    date = models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
     return f"{self.user} - {self.amount} ({self.date})"

          




