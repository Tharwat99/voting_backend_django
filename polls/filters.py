from . models import Poll
import django_filters

class PollsListFilter(django_filters.FilterSet):
    """ 
    filter Polls using title, and description and order by expiry_date.
    """
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    
    
    class Meta:
        model = Poll
        fields = ["title", "description"]
        order_by = ['-expiry_date', 'expiry_date']

