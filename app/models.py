from time import timezone
from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from django.forms import ModelForm
from app.views import ProductView


class customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
def __str__(self):
 return str(self.id)
 
CATEGORY_CHOICES=(
    ('b','boots'),
    ('h','heels'),
    ('s','sneakers'),
)
class productDetail(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField((""))
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to='productimg')
def __str__(self):
 return str(self.id)

class cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(productDetail, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
def __str__(self):
 return str(self.id)

STATUS_CHOICES= (
    ('accepted','accepted'),
    ('packed','packed'),
    ('on the way','on the way'),
    ('cancel','cancel')
) 
class orderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    product = models.ForeignKey(productDetail, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')

def __str__(self):
 return str(self.id)

# class Comment(models.Model):
#     STATUS=(
#         ('New','New'),
#         ('True','True'),
#         ('False','False'),
#     )
#     product = models.ForeignKey(productDetail, on_delete=models.CASCADE)
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     subject=models.CharField(max_length=50,blank=True)
#     comment=models.CharField(max_length=50,blank=True)
#     rate=models.IntegerField(default=1)
#     ip=models.CharField(max_length=20,blank=True)
#     status=models.CharField(max_length=10,choices=STATUS)
#     create_at = models.DateTimeField(auto_now_add=True)
#     update_at = models.DateTimeField(auto_now=True)

# def __str__(self):
#  return self.subject

# class CommentForm(ModelForm):
#     class Meta:
#         model=Comment
#         fields=['subject','comment','rate']


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)

