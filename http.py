from django.http import HttpResponse
try:
    import json
except ImportError:
    from django.utils import simplejson as json

class HttpJSONResponse(HttpResponse):
    """
    An HttpResponse of JSON content
    
    Unlike a Django HttpResponse, this class can accept any JSON-serializable data type as content:
    dictionaries, lists, strings, etc.
    
    Example::
    
        def some_view(request):
            return HttpJSONResponse({'foo': 'bar'})
    """
    def __init__(self, content=''):
        super(HttpJSONResponse, self).__init__(content=json.dumps(content), mimetype='application/json')

class HttpResponseCreated(HttpResponse):
    """
    HTTP 201 response. Should return the URI of the resource created.
    
    See `HTTP/1.1 Status Code Definitions <http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.2>`_.
    """
    status_code = 201

class HttpJSONResponseBadRequest(HttpJSONResponse):
    """
    HTTP 400 response. Can return details of the errors with the request in the response body.
    """
    status_code = 400