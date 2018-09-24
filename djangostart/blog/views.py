from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
# Create your views here.
# woodpeck -add

from .models import Post
from .forms import PostForm

def post_list_view(request):
    post_all = Post.objects.all()
    post_all = post_all.filter(published_date__lte = timezone.now())
    post_all = post_all.order_by('published_date')

    return render(request, 'post_list.html', {'post_all' : post_all})

def post_detail_view(request,*args,**kwargs):
    #find_row = Post.objects.get(id=kwargs.get('id'))
    find_row = get_object_or_404(Post,id=kwargs.get('id'))
    return render(request,'post_detail.html',{'post':find_row})

def post_new_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            #print(request.user)
            #form.save()
            post = form.save(commit=False)

            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail',post.id)

    else:
        form = PostForm()
    return render(request,'post_new.html',{'form':form})

def post_edit_view(request,*args,**kwargs):
    #find_row = Post.objects.get(id=kwargs.get('id'))
    find_row = get_object_or_404(Post,id=kwargs.get('id'))

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=find_row)
        if form.is_valid():
            # print(request.user)
            # form.save()
            post = form.save(commit=False)

            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post.id)

    else:
        form = PostForm(instance=find_row)

    return render(request,'post_edit.html',{'form':form})