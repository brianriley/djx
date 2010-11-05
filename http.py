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