from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from blog.models import blog as Blog
def home(request:HttpRequest):
    # return HttpResponse(request.COOKIES)
    # return HttpResponse("Welcome home")
    blog=Blog.objects.all().order_by('-created_at')[0:3]
    return render(request,'normal/index.html',context=
    {
        'maintitle':'Clean Blog',
        'title':'A Blog Theme by Start Bootstrap',
        'blogs':blog
    })
def about(request:HttpRequest):
    return render(request,'normal/about.html',context={
        'maintitle':'About Us'
        });

def contact(request:HttpRequest):
    return render(request,'normal/contact.html',context={
        'maintitle':'Contact Me',
        'title':'Have questions? I have answers.'
    })