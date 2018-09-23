from django.shortcuts import render,get_object_or_404
from django.utils import timezone
# Create your views here.
# woodpeck -add

from .models import Post

def post_list_view(request):
    post_all = Post.objects.all()
    post_all = post_all.filter(published_date__lte = timezone.now())
    post_all = post_all.order_by('published_date')

    return render(request, 'post_list.html', {'post_all' : post_all})

def post_detail_view(request,*args,**kwargs):
    #find_row = Post.objects.get(id=kwargs.get('id'))
    find_row = get_object_or_404(Post,id=kwargs.get('id'))
    return render(request,'post_detail.html',{'post':find_row})