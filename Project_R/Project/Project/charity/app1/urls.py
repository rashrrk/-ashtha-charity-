from django.urls import path
from .import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.index),
    path('/',views.index),
    path('donate/',views.donateView),
    path('about/',views.aboutView),
    path('campaign/',views.campaignView),
    path('fundraise/',views.fundraiseView),
    path('volunteer/',views.volunteerView),
    path('contact/',views.contactView),
    path('gallery/',views.galleryView),
    path('login/',views.login),
    path('registerpage/',views.registerPage,name="registration"),
    path('adminLogin/',views.adminView),
    path('adminReg/',views.adminRegView),
    path('adminDonate/',views.adminDonateView),
    path('adminFund/',views.adminFundView),
    path('adminCamp/',views.adminCampView),
    path('adminVol/',views.adminVolView),
    path('adminLg/',views.adminLoginPageView)
    
    
   
    
    
    ]

