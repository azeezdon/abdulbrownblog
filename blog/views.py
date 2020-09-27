from .models import Post
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.shortcuts import HttpResponseRedirect
from .forms import NewCommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'posts'
    ordering = ['-publish']
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        most_recent = Post.objects.order_by('-publish')[:5]
        context['most_recent'] = most_recent
        return context








    # class PostDetailView(DetailView):
     #model = Post
    #template_name = 'post_detail.html'
    #context_object_name = 'post'







#def post_detail(request, id):
 #   post = Post.objects.get(id=id)
  #  form = CommentForm()
   # if request.method == 'POST':
    #    form = CommentForm(request.POST)
     #   if form.is_valid():
      #      comment = Comment(
       #         user=form.cleaned_data["user"],
        #        content=form.cleaned_data["content"],
         #       post=post
          #  )
           # comment.save()

#    comments = Comment.objects.filter(post=post)
 #   context = {
  #      "post": post,
   #     "comments": comments,
    #    "form": form,
 #   }
  #  return render(request, "post_detail.html", context)









def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    most_recent = Post.objects.order_by('-publish')[:5]

    allcomments = post.comments.filter(status=True)
    page = request.GET.get('page', 1)

    paginator = Paginator(allcomments, 10)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('/' + post.slug)
    else:
        comment_form = NewCommentForm()

    return render(request, 'post_detail.html',
                  {'post': post, 'comments': user_comment, 'comments': comments, 'comment_form': comment_form,
                   'allcomments': allcomments, 'most_recent': most_recent, })


