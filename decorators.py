def paginated_view(default_per_page=10, max_per_page=50):
    """
    When applied to a view, the following two GET parameters are accepted:

    ``per_page``

    The number of items to show per page. If not present, this will default to 
    the decorator's ``default_per_page`` argument (10). ``per_page`` cannot exceed 
    the decorator's ``max_per_page`` argument (50).

    ``page``

    The page number. Defaults to 1 if not present.

    Example::

        http://example.com/feed/?per_page=12&page=2

    The decorated view's Request object wil then have a ``pagination`` attribute, which 
    is a dictionary with the ``per_page`` and ``page`` values.

    Example::

        @paginated_view()
        def some_view(request):
            paginator = Paginator(Model.objects.all(), request.pagination['per_page'])
            try:
                items = paginator.page(request.pagination['page'])
            except (EmptyPage, InvalidPage):
                items = paginator.page(paginator.num_pages)
            ...
    """
    def decorator(func):
        def inner(request, *args, **kwargs):
            try:
                per_page = int(request.GET.get('per_page', default_per_page))
            except ValueError:
                per_page = default_per_page

            # Prevent returning the entire table
            per_page = per_page > max_per_page and default_per_page or per_page

            try:
                page = int(request.GET.get('page', '1'))
            except ValueError:
                page = 1

            request.pagination = {
                'per_page': per_page,
                'page': page
            }
            return func(request, *args, **kwargs)

        return inner
    return decorator