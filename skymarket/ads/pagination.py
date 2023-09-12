from rest_framework.pagination import PageNumberPagination


class AdsPagination(PageNumberPagination):
    """
    Разбивает список объявлений на страницы с заданным количеством элементов на странице.
    """
    page_size = 4
    page_query_param = 'page_size'
    max_page_size = 8

