from django.urls import path 
from .views import HomePage
#,PostDatail,SignupPage,LogoutUser,loginPage,contactPage
urlpatterns=[
    path('',HomePage,name='home'),
    # path('post/<int:id>/',PostDatail,name='post_detali'),
    # path('signup/',SignupPage,name='signup'),
    # path('logout/',LogoutUser,name="logout"),
    # path('login/',loginPage,name='login'),
    # path('contact/',contactPage,name='contact')

]

