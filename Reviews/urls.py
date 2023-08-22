from django.contrib import admin
from django.urls import path
from Analysis import views as appviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',appviews.user_index,name='user_index'),
    path('login',appviews.user_login,name='user_login'),
    path('register',appviews.user_register,name='user_register'),
    path('otp',appviews.user_otp,name='user_otp'),
    path('dashboard',appviews.user_dashboard,name='user_dashboard'),
    path('about',appviews.user_about,name='user_about'),
    path('portfolio',appviews.user_portfolio,name='user_portfolio'),
    path('myprofile',appviews.user_myprofile,name='user_myprofile'),
    path('reviwes',appviews.user_reviews,name='user_reviews'),
    path('Review',appviews.user_review,name='user_review'),
    path('communications', appviews.communication, name='communications'),
    path('games', appviews.games, name='games'),
    path('socialmedia', appviews.socialmedia, name='socialmedia'),
    path('finanace', appviews.finance, name='finance'),
    path('education', appviews.education, name='education'),
    path('entertinment', appviews.entertinment, name='entertinment'),
    
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)