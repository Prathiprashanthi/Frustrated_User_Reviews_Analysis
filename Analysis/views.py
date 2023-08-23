from django.shortcuts import render,redirect
from Analysis.models import *
import random
import string
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from django.contrib import messages
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
import urllib.request
import urllib.parse
import ssl
# Create your views here.
def user_index(request):
    return render(request, 'user/index.html')



def sendSMS(user, otp, mobile):
    data = urllib.parse.urlencode({
        'username': 'Codebook',
        'apikey': '56dbbdc9cea86b276f6c',
        'mobile': mobile,
        'message': f'Hello {user}, your OTP for account activation is {otp}. This message is generated from https://www.codebook.in server. Thank you',
        'senderid': 'CODEBK'
    })
    data = data.encode('utf-8')
    # Disable SSL certificate verification
    context = ssl._create_unverified_context()
    request = urllib.request.Request("https://smslogin.co/v3/api.php?")
    f = urllib.request.urlopen(request, data,context=context)
    return f.read()


def user_register(request):
    if request.method== 'POST':
        user_fullname=request.POST.get('First_name')
        user_email=request.POST.get('Email')
        user_password =request.POST.get('Password1')
        user_contact =request.POST.get('Contact')
        user_image =request.FILES['image']
        print(user_fullname,user_email,user_password,user_contact,user_image,'data')
        user_otp = str(random.randint(1000, 9999)) 
        print(user_otp)
        c = 0
        try:
            User.objects.get(UserEmail= user_email)
            messages.warning(request, 'mail already exists')
            return redirect("user_register")
        except:
            response = sendSMS(user_fullname, user_otp, user_contact)
            User.objects.create(User_Otp=user_otp,UserFullname=user_fullname,UserEmail= user_email,UserPassword=user_password,UserContact=user_contact,UserImage=user_image, count=c)        
            request.session['UserEmail'] = user_email
            mail_message = f'Registration Successfully\n Your 4 digit Pin is below\n {user_otp}'
            print(mail_message)
            send_mail("Student Password", mail_message , settings.EMAIL_HOST_USER, [user_email])
            
            messages.success(request, 'Register SUccessfull...!')
            return redirect('user_otp')
            
    return render(request,'user/register.html')




def user_login(request):
    if request.method =='POST':
        user_email=request.POST.get('Email')
        user_password = request.POST.get('pass')
        print( user_email,user_password)
        try:
            user_data = User.objects.get(UserEmail = user_email)
            print(user_data)
            if user_data.UserPassword == user_password:
                if user_data.Otp_Status =='verified':
                    request.session['UserId'] = user_data.UserId
                    messages.success(request, 'Login SUccessfull...!')
                    return redirect('user_dashboard')
                else:
                    messages.warning(request, 'verifyOTP...!')
                    
                    request.session['UserId'] = user_data.UserId
                    return redirect('user_otp')
            else:
                messages.error(request, 'incorrect password...!')
                return redirect('user_login')
            
        except:
            messages.info(request, "userdoesnot exist...!")
            print('except')
            return redirect('user_login')
    return render(request,'user/login.html')

def user_otp(request):
    user_id = request.session['UserEmail']
    user_o = User.objects.get(UserEmail = user_id)
    print(user_o)
    print(user_o.User_Otp, 'creaetd otp')
    if request.method == 'POST':
        u_otp = request.POST.get('otp')
        print(u_otp, 'enter otp')
        if u_otp == user_o.User_Otp:
            user_o.Otp_Status = 'verified'
            user_o.save()
            messages.success(request, 'OTP  verified successfully')
            return redirect('user_login')
        else:
            return redirect('user_otp')
    return render(request,'user/otp.html', {'user':user_o})

def user_dashboard(request):
    return render(request,'user/dashboard.html')

def user_about(request):
    return render(request,'user/about.html')

def user_portfolio(request):
    return render(request,'user/portfolio.html')

def user_myprofile(request):
    user_id = request.session['UserId']
    user = User.objects.get(UserId = user_id)
    print(user,'user')
    if request.method == 'POST':
      Userfullname = request.POST.get('fullname')
      useremail = request.POST.get('email')
      usercontact = request.POST.get('contact')
      print(Userfullname,useremail,usercontact)
     
      if len(request.FILES)!=0:
         image = request.FILES.get('image')
         user.UserImage = image
      user.UserFullname = Userfullname
      user.UserEmail= useremail
      user.UserContact = usercontact
      user.save()
      messages.success(request, 'Updated SUccessfully...!')
    return render(request,'user/myprofile.html', {'user_details' : user})

def user_review(request):
    reviews = Reviews.objects.all()
    return render(request,'user/Review.html', {'reviews':reviews})

def communication(req):
    reviews = Reviews.objects.filter(catgory = 'Communication')
    user_id = req.session['UserId']
    user = User.objects.get(UserId = user_id)
    user.Ratings = ''
    user.Reviews = ''
    user.Review_Catgeory = ''
    user.save()
    paginator = Paginator(reviews, 10) 
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render(req, 'user/communication.html', {'reviews' : post})

def games(req):
    reviews = Reviews.objects.filter(catgory = 'games')
    user_id = req.session['UserId']
    user = User.objects.get(UserId = user_id)
    user.Ratings = ''
    user.Reviews = ''
    user.Review_Catgeory = ''
    user.save()
    paginator = Paginator(reviews, 10) 
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render(req, 'user/games.html', {'reviews' : post})

def socialmedia(req):
    reviews = Reviews.objects.filter(catgory = 'socialmedia')
    user_id = req.session['UserId']
    user = User.objects.get(UserId = user_id)
    user.Ratings = '0'
    user.Reviews = ''
    user.Review_Catgeory = ''
    user.save()
    paginator = Paginator(reviews, 10) 
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render(req, 'user/socialmedia.html', {'reviews' : post})

def finance(req):
    reviews = Reviews.objects.filter(catgory = 'Finance')
    user_id = req.session['UserId']
    user = User.objects.get(UserId = user_id)
    user.Ratings = ''
    user.Reviews = ''
    user.Review_Catgeory = ''
    user.save()
    paginator = Paginator(reviews, 10) 
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render(req, 'user/finance.html', {'reviews' : post})

def education(req):
    reviews = Reviews.objects.filter(catgory = 'Education')
    user_id = req.session['UserId']
    user = User.objects.get(UserId = user_id)
    user.Ratings = ''
    user.Reviews = ''
    user.Review_Catgeory = ''
    user.save()
    paginator = Paginator(reviews, 10) 
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render(req, 'user/education.html', {'reviews' : post})

def entertinment(req):
    reviews = Reviews.objects.filter(catgory = 'Entertinment')
    user_id = req.session['UserId']
    user = User.objects.get(UserId = user_id)
    user.Ratings = ''
    user.Reviews = ''
    user.Review_Catgeory = ''
    user.save()
    paginator = Paginator(reviews, 10) 
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render(req, 'user/entertinment.html', {'reviews' : post})

def user_reviews(request):
    user_id = request.session['UserId']
    user = User.objects.get(UserId = user_id)
    if request.method == 'POST':
        userreview = request.POST.get('review')
        rating =request.POST.get('rating')
        print(type(rating), rating)
        catgory=request.POST.get('category')
        if not rating:
            # messages.info(request,'give rating')
            return redirect('user_reviews')
        sid=SentimentIntensityAnalyzer()
        score=sid.polarity_scores(userreview)
        sentiment=None
        if score['compound']>0 and score['compound']<=0.5:
            sentiment='positive'
        elif score['compound']>=0.5:
            sentiment='very positive'
        elif score['compound']<-0.5:
            sentiment='very negative'
        elif score['compound']<0 and score['compound']>=-0.5:
            sentiment='negative'
        else :
            sentiment='neutral'
        user.Review_Catgeory=catgory
        user.Reviews=userreview
        user.Ratings= rating
        c = user.count
        c = int(c)
        c+=1
        user.count = c
        # user.save()
        user.save()
        Reviews.objects.create(User_Foreign=user, Username=user.UserFullname,Userreview=userreview,Rating=rating,catgory=catgory, Sentiment = sentiment)
        messages.success(request, 'Reviews Submited...!')
    Rev =Reviews.objects.filter(Username=user.UserFullname)
    
    code=Rev
    # print(code.Rating)
    
    context={'u':code, 'user':user}
        # return redirect('user_reviews', review_id=code.ReviewId)
    return render(request,'user/reviwes.html', context)

