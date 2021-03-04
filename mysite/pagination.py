from rest_framework.pagination import LimitOffsetPagination


class ListPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 1000


class AdvertisementPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 1000