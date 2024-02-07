from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Tag
from .forms import PostCreateForm,PostEditForm
from bs4 import BeautifulSoup
import requests
from django.contrib import messages


# Create your views here.
def home_page(request,tag=None):
    if tag:
        posts = Post.objects.filter(tags__slug=tag)
        tag = get_object_or_404(Tag, slug=tag)
    else:
        posts = Post.objects.all()
        
    categories = Tag.objects.all()
        
    context = {'posts':posts, 'categories':categories,'tag':tag}
    return render(request,'app/home.html',context)

def create_post(request):
    form = PostCreateForm()
    
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            
            web_url = requests.get(form.data['url'])
            soup = BeautifulSoup(web_url.text, 'html.parser')
            
            find_image = soup.select('meta[content^="https://live.staticflickr.com/"]')
            image = find_image[0]['content']
            post.image = image
            
            find_artist = soup.select('a.owner-name')
            artist = find_artist[0].text.strip()
            post.artist = artist
            
            find_title = soup.select('h1.photo-title')
            title = find_title[0].text.strip()
            post.title = title
            
            post.save()
            form.save_m2m()
            return redirect('home')
        
    context = {'form':form}
    return render(request, 'app/post_create.html', context)

def delete_post(request,pk):
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request,'Deleted successfully!')
        return redirect('home')
    context = {'post':post}
    return render(request, 'app/post_delete.html',context)

def edit_post(request,pk):
    post = get_object_or_404(Post, id=pk)
    form = PostEditForm(instance=post)
    
    if request.method == 'POST':
        form = PostEditForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,'Updated successfully!')
            return redirect('home')
    context = {'post':post,'form':form}
    return render(request, 'app/post_edit.html', context)


def read_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    context = {'post':post}
    return render(request, 'app/post_read.html', context)





