djx
---

A collection of tools that extend some of Django's core functionality or abstract 
common operations.

The following tools are available in this package:

http
====

HttpJSONResponse
~~~~~~~~~~~~~~~~

An HttpResponse of JSON content
    
Unlike a Django HttpResponse, this class can accept any JSON-serializable data type as content:
dictionaries, lists, strings, etc.

Example::

	def some_view(request):
		return HttpJSONResponse({'foo': 'bar'})

decorators
==========

paginated_view
~~~~~~~~~~~~~~

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