from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm
from .models import Comment
from django.views.generic.edit import UpdateView, DeleteView


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


class EditCommentView(UpdateView):
    """ View to handle editing a blog post """
    model = Comment
    form_class = CommentForm
    success_url = '/blog/'
    template_name = 'edit-blog-post.html'

   
    
#class DeleteCommentView(DeleteView):
   # model = Comment
    #success_url = Comment('delete_comment')

#class CommentDelete(View):
  #  def delete_comment(request, comment_id):
     #   comment = get_object_or_404(Comment, id=comment_id)
      #  comment.delete()
       # messages.success(request, 'Comment deleted')
      #  return HttpResponeRedirect(reverse('post_detail', args=[comment.post.slug]))

#def delete_comment(request):
    #id = request.POST['comment_id']
   # pk = request.POST['post_id']
   # if request.method == 'POST':
     #   comment = get_object_or_404(Comment, id=id, pk=pk)
    #    try:
           # comment.delete()
           # messages.success(request, 'You have successfully deleted the comment')
     #   except:
         #   messages.warning(request, 'The comment could not be deleted.')
       # return redirect('get_posts')

#class EditComment(View):
   # def edit_comment(request, comment_id):
      #  comment = get_object_or_404(Comment, id=comment_id)
       # comment.edit()
       # messages.success(request, 'Comment updated')
      #  return HttpResponeRedirect(reverse('post_detail', args=[comment.post.slug]))


   # def edit_comment(request, comment_id):
     #   comment = get_object_or_404(comment, id=comment_id)
       # if request.method == "POST":
           # form = CommentForm(request.POST, indtance=comment)
          #  if form.is_valid():
          #      fomr.save()
          #  return redirect('view_comment')

     #   form = CommentForm(instance=comment)

   #     context = {
    #        'form' : form
     #   }
      #  return render(request, 'templates/edit_comment.html', context)


class NutritionPageView(View):
    template_name = 'obesity.html',

class healthPageView(View):
    template_name = 'health.html'

class FunnyPageView(View):
    template_name = 'funny.html',
