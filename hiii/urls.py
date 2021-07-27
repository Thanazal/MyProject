from . import views
from django.urls import path
app_name='hiii'
urlpatterns = [
    path('hiii',views.hiii),
    path('',views.index),
    path('signup',views.signup,name='signup'),
    path('login',views.login,name='login'),
    path('home/<int:id>',views.home,name='home'),
    path('update/<int:id>',views.update,name='update'),
    path('changepassword/<int:id>',views.password_change,name='changepassword'),
    path('logout/',views.logout,name='logout'),
]

