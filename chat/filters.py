from rest_framework import filters


class UserFilterChat(filters.BaseFilterBackend):
    """Фильтрует сообщения по пользователю"""

    def filter_queryset(self, request, queryset, view):
        return queryset.filter(user=request.user)
