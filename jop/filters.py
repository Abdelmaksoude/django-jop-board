import django_filters
from .models import Jop
class JopFilter(django_filters.FilterSet):
    Description = django_filters.CharFilter(lookup_expr='icontains')
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Jop
        fields = '__all__'
        exclude = ['owner' , 'Published_at' , 'Vacancy' , 'Salary' , 'image' , 'slug']