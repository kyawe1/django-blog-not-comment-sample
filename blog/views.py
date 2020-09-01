from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest,Http404
from django.core.exceptions import PermissionDenied
from blog.models  import blog
from django.contrib.auth.decorators import login_required
from django.views.decorators import csrf
# Create your views here.
@login_required
def all(request):
    b=blog.objects.latest_all_blog()
    return HttpResponse(b)

def one(request:HttpRequest,id:int):
    ok=blog.objects.getone(id)
    if ok:
        return render(request,'blog/post.html',context={
            'blog':ok,
            'single': request.user.username==ok.user.username
        })
    else:
        raise Http404
@csrf.csrf_protect
@login_required
def create(request:HttpRequest):
    if (request.method=='POST'):
        b=blog.objects.createBlog(title=request.POST['title'],body=request.POST['body'],user=request.user)
        b=blog.objects.last()
        return redirect('blog:get_one',b.id)
    return render(request,'blog/create.html')

@login_required
def edit(request:HttpRequest,id:int):
    b=blog.objects.getone(id)
    if request.user==b.user:
        if (request.method=='POST'):
            b.title=request.POST['title']
            b.body=request.POST['body']
            b.save()
            return redirect('blog:get_one',id)
        return render(request,'blog/update.html',context={
            'blog':b
        })
    else:
        raise PermissionDenied

@login_required
def delete(request:HttpRequest,id:int):
    b=blog.objects.getone(id)
    if request.user==b.user or request.user.is_superuser:
        b.delete()
        return HttpResponse('deleted')
   
    else:
        raise PermissionDenied
