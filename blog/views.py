from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
# from django.contrib.auth import login,logout,authenticate
from .models import Post


def HomePage(request):
    Posts = Post.objects.all()
    return render (request,'index.html',{'posts':Posts})


# def contactPage(request):
#     contact=Contact()
#     if request.method == 'POST':
#        contact.username=request.POST.get('name')
#        contact.email=request.POST.get('email')
#        contact.message=request.POST.get('message')
#        contact.save()
#        print('Contact Saqlandi')
#        return render (request,'contact.html')




# def PostDatail(request,id=id):
#     Posts = Post.objects.get(id=id)
#     return render(request,'post_detail.html',{"post":Posts})



# def SignupPage(request):

#     if request.method == 'POST':
#       user=User()
#       username = request.POST.get('Your Name')
#       useremail = request.POST.get('Your Email')
#       if request.POST.get('Password') == request.POST.get('Password2'):
#           password = request.POST.get('Password2')
#           user=User.objects.create_user(username=username,email=useremail,password=password)
#           user.save()
#           return redirect('home')
         
#     return render (request,'singnup.html')

# def loginPage(request):
#     if request.method =='POST':
#         username = request.POST.get('Your Namel')
#         password = request.POST.get('Passwordl')
#         user= authenticate(request,username=username,password=password)
#         user.save()
#         if user is not None:
#             login(request,user)
#             return redirect('home')

#     return render(request,'login.html')


# def LogoutUser(request):
#     logout(request)
#     return redirect('home')

