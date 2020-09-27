from .models import Course
import django_filters


class CourseFilter(django_filters.FilterSet):
    title = django_filters.CharFilter()
    class Meta:
        model = Course
        fields = [ 'title', 'publish', ]