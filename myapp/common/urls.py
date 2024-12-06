from django.urls import path
from . import views

urlpatterns = [
   
    path('signup/',views.employee_signup,name='employee_signup'),
    path('',views.employee_compare,name='employee_compare'),

]
