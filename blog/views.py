from django.shortcuts import render, HttpResponse, redirect
from blog.models import Post, BlogComment
from django.contrib import messages


# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    print(allPosts)
    context = {'allPosts' : allPosts}

    return render(request, 'blog/blogHome.html', context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    print("post : ",post)
    comments = BlogComment.objects.filter(post=post)
    # print(post)
    print(request.user)
    context = {'post' : post, 'comments' : comments, 'user' : request.user}
    return render(request, 'blog/blogPost.html', context)

def postComment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user =  request.user
        postSno =  request.POST.get("postSno")
        post =  Post.objects.get(sno=postSno)
        parentSno =  request.POST.get("parentSno")

        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post= post)
            comment.save()
            messages.success(request, "Your comment has been posted sucessfully!")
        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post= post, parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted sucessfully!")






    # print(post)
    return redirect(f"/blog/{post.slug}")


