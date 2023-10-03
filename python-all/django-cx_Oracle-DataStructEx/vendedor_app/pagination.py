from rest_framework import pagination, response

class CustomPageNumberPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'count'
    max_page_size = 100
    page_query_param = 'page'
    
    def get_paginated_response(self, data):
        return response.Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })