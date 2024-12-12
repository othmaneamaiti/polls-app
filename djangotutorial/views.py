# Imports
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader


##
# Handle 404 Errors
# @param request WSGIRequest list with all HTTP Request
def error404(request, exception):
    return HttpResponseRedirect('polls/')
