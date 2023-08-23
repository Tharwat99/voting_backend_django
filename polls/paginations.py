from rest_framework.pagination import PageNumberPagination

class PollsListPagination(PageNumberPagination):
    """
    Paginate Polls.
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20
