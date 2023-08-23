from django.db import models

# Create your models here.
class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    UserFullname =models.CharField(max_length=50)
    UserEmail =models.EmailField(max_length=50)
    UserPassword =models.TextField(max_length=10)
    UserContact = models.TextField(max_length=10)
    UserImage=models.FileField(upload_to='media', null = True)
    User_Otp =models.TextField(max_length=1000,null=True)
    Otp_Status = models.TextField(max_length=20, default='pending')
    Review_Catgeory = models.TextField(max_length=50, null=True)
    Reviews=models.TextField(max_length=200,null=True)
    Ratings=models.TextField(max_length=100,null=True)
    count = models.IntegerField(null=True, default=0)
    class Meta:
        db_table="user"
    
class Reviews(models.Model):
    ReviewId = models.AutoField(primary_key=True)
    Username =models.CharField(max_length=50)
    Userreview = models.TextField(max_length=200)
    Rating = models.IntegerField()
    catgory =models.TextField(max_length=20)
    Sentiment =models.TextField(max_length=20, null = True)
    Date = models.DateTimeField(auto_now_add=True)
    Status = models.TextField(max_length=100, null=True)
    User_Foreign = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    
    
    class Meta:
        db_table="user_reviews"
