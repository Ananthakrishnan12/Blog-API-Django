from rest_framework.pagination import PageNumberPagination

class BloglistViewPagination(PageNumberPagination):
    page_size = 3
    page_query_param="previous"
    page_size_query_param = 'page_size'
    last_page_strings="Next"
    