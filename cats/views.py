from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib import messages
from django.views.generic import ListView, DeleteView
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, PostForm, ContactForm
from .models import Comment
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.core.mail import send_mail, BadHeaderError


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog_post.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


class PostLike(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse("post_detail", args=[slug]))


class PostComment(View):
    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm(data=request.POST)

        return render(
             request,
             "blog_post.html",
             {
                 "post": post,
                 "comments": comments,
                 "commented": True,
                 "comment_form": comment_form,
                 "liked": liked,
             },
         )


class NutritionPageView(View):
    template_name = 'obesity.html',


class healthPageView(View):
    template_name = 'health.html'


class FunnyPageView(View):
    template_name = 'funny.html',


def add_post(request):
    if not request.user.is_superuser:
        messages.error(request, "not authorised")
        return redirect("home")
    blog_form = PostForm(request.POST or None)
    user = get_object_or_404(User, username=request.user.username)
    if request.method == 'POST':
        if blog_form.is_valid():
            blog_form.instance.author = request.user
            form = blog_form.save()
            messages.success(request, "post added")
            return redirect("home")
    template = 'add_blog_post.html'
    context = {
        'blog_form': blog_form,
    }
    return render(request, template, context)


def edit_post(request, slug):
    if not request.user.is_superuser:
        messages.error(request, "not authorised")
        return redirect("home")
    post = get_object_or_404(Post, slug=slug)
    blog_form = PostForm(request.POST or None, instance=post)
    user = get_object_or_404(User, username=request.user.username)
    if request.method == 'POST':
        if blog_form.is_valid():
            blog_form.instance.author = request.user
            form = blog_form.save()
            messages.success(request, "post edited")
            return redirect(reverse('post_detail', kwargs={'slug': post.slug}))
    template = 'edit_blog_post.html'
    context = {
        'post': post,
        'blog_form': blog_form,
    }
    return render(request, template, context)


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_blog_post.html'
    success_url = reverse_lazy('home')


def delete_comment(request, cid, pid):
    if not request.user.is_superuser:
        messages.error(request, "not authorised")
        return redirect("home")
    comment = get_object_or_404(Comment, id=cid)
    post = get_object_or_404(Post, id=pid)
    messages.success(request, "comment deleted")
    comment.delete()
    return redirect(reverse('post_detail', kwargs={'slug': post.slug}))


def contact(request):
    if request.method == 'POST' :
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
            'name' : form.cleaned_data['name'],
            'email_address' : form.cleaned_data['email_address'],
            'phone' : form.cleaned_data['phone'],
            'message' : form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            return redirect ("main:homepage")

    form = ContactForm()
    return render(request, "contact.html", {'form':form})

