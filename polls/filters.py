from . models import Poll
import django_filters

class PollsListFilter(django_filters.FilterSet):
    """ 
    filter Polls using title, description, choice_text and order by expiry_date.
    """
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    choice_text  = django_filters.CharFilter(method='get_choice_text') 
    
    class Meta:
        model = Poll
        fields = ["title", "description", "choice_text"]
        order_by = ['-expiry_date', 'expiry_date']
        
    def get_choice_text(self, queryset, name, value, *args, **kwargs):
        """
        custom method to filter queryset to get polls by choice text.
        """
        return queryset.filter(choices__choice_text__icontains=value)

