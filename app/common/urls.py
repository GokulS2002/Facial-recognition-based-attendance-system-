from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('',views.check,name='check'),
    path('video/',views.video,name='video'),
    path('signup/',views.employee_signup,name='employee_signup'),
    path('compare/',views.employee_compare,name='employee_compare'),

]
