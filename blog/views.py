# from importlib.resources import contents
# from multiprocessing import context
from django.shortcuts import render,redirect,get_list_or_404
from django.views.generic.base import View
from .forms import PostCreateForm
from .models import Post
class BlogListView(View):
    def get(self , request ,*args, **kwargs):
        context={
          
        }
        return render(request,'blog_list.html',context)

class BlogCreateView(View):
    def get(self,request,*args,**kwargs):
        form=PostCreateForm()
        context={
            'form':form
        }
        return render(request,'blog_create.html',context)
    def post(self,request,*args,**kwargs):
        if request.method=="POST":
            form = PostCreateForm(request.POST)
            # print("Post")
            # print(form.is_valid())
            if form.is_valid():
                title =  form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')
                # print("-----------------------------------")
                # print(title)
                # print(content)
                # print("-----------------------------------")
                p, created = Post.objects.get_or_create(title=title,content=content)
                p.save()
                return redirect('blog:home')

        context={

        }
        return render(request,'blog_create.html',context)
