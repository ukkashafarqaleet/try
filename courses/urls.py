
from django.contrib import admin
from django.urls import path , include
from courses.views import   MyCoursesList,  HomePageView ,verifyPayment ,  coursePage , SignupView , LoginView , signout , checkout
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from courses.views import newsletter

from django.urls import path
urlpatterns = [
    path('', HomePageView.as_view() , name = 'home'),
    path('logout', signout , name = 'logout'),
    path('my-courses', MyCoursesList.as_view() , name = 'my-courses'),
    path('signup', SignupView.as_view() , name = 'signup'),
    path('login', LoginView.as_view() , name = 'login'),
    path('course/<str:slug>', coursePage , name = 'coursepage'),
    path('check-out/<str:slug>', checkout , name = 'check-out'),
    path('verify_payment', verifyPayment , name = 'verify_payment'),
    path('', newsletter.index, name='letter-index'),
    path('mail_letter/', newsletter.mail_letter, name='mail-letter')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)










