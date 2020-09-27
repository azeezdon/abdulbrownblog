from .models import Course, Comment
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.shortcuts import HttpResponseRedirect
from .forms import NewCommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


#def crash_course(request):

#    page = request.GET.get('page', 1)
#    posts=Course.objects.filter()
#    paginator = Paginator(posts, 4)
 #   try:
  #      posts = paginator.page(page)
   # except PageNotAnInteger:
#        posts = paginator.page(1)
 #   except EmptyPage:
  #      posts = paginator.page(paginator.num_pages)
    

   # context = {

    #    'crash_course': posts

    #}

    #return render(request, 'crash_course.html', context)

class CourseListView(ListView):
    model = Course
    paginate_by = 4 # number of posts will load
    context_object_name = 'crash_course'
    template_name = 'crash_course.html'
    ordering = ['-publish']

class CourseDetailView(DetailView):
    model = Course
    template_name = 'crash_course_detail.html'





class Course1View(ListView):
    model = Course
    paginate_by = 4 # number of posts will load
    context_object_name = 'course1'
    template_name = 'course1.html'
    ordering = ['-publish']


class Course1_detailDetailView(DetailView):
    model = Course
    template_name = 'course1_detail.html'


    