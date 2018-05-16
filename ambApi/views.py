from django.shortcuts import render
from django.http import JsonResponse
from ambApi.models import Post
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def submit_post(request):
    if request.method=='POST':
        new_text=request.POST.get('text')
        Post.objects.create(text=new_text,likes=0)
        return JsonResponse({'result':1})
@csrf_exempt
def submit_like(request):
    if request.method=='POST':
        post_id=request.POST.get('post_id')
        post=Post.objects.get(id=post_id)
        post.increment()
        return JsonResponse({'result':1})

def get_posts(request):
    if request.method=='GET':
        posts=Post.objects.all()
        posts_dict_list=[]   
        for post in posts:
            posts_dict_list.append(post.as_dict())
        return JsonResponse(posts_dict_list,safe=False)

