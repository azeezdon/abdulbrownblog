"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from filebrowser.sites import site
from django.conf.urls import url
from django.views.static import serve
from courses.views import CourseDetailView,CourseListView, Course1View, Course1_detailDetailView
from blog.views import PostListView, post_detail

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('mce_filebrowser/', site.urls),
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', PostListView.as_view(), name='index'),
    #path('course/', CourseListView.as_view(), name='course'),
    path('crash_course/', CourseListView.as_view(), name='crash_course'),
    path('course1/', Course1View.as_view(), name='course1'),
    path('<slug:post>/', post_detail, name='post_detail'),
   # path('<slug:slug>', post_detail, name='post_detail'),
    path('course/<int:pk>',CourseDetailView.as_view(), name='crash_course_detail'),
    path('course1/<int:pk>/',Course1_detailDetailView.as_view(), name='course1_detail'),
    url(r'^download/(P<path>.)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
