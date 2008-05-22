#
# Copyright 2008, Blue Dynamics Alliance, Austria - http://bluedynamics.com
#
# GNU General Public Licence Version 2 or later

__author__ = """Robert Niederreiter <rnix@squarewave.at>"""
__docformat__ = 'plaintext'

from zope.interface import implements
from Products.Five import BrowserView
from ZTUtils import make_query
from interfaces import IRequestMixin

class RequestMixin(object):
    """IRequestMixin implementation.
    """
    
    implements(IRequestMixin)
    
    def makeUrl(self, context=None, url=None, resource=None, query=None):
        if url and context:
            raise ValueError, 'Need either context or url, both was given.'
        if context:
            url = context.absolute_url()
        if not url:
            url = self.context.absolute_url()
        if resource:
            url = '%s/%s' % (url, resource)
        if query:
            url = '%s?%s' % (url, query)
        return url
    
    def makeQuery(self, additionals=None, ignores=None,
                  considerexisting=False, considerspecific=None):
        params = {}
        if considerexisting:
            form = self.request.form
            for key in form.keys():
                if ignores:
                    if key in ignores:
                        continue
                if key != '-C':
                    params[key] = form[key]
        
        if considerspecific and not considerexisting:
            form = self.request.form
            for param in considerspecific:
                value = form.get(param)
                if value:
                    params[param] = value
        
        if additionals:
            params.update(additionals)
        
        return make_query(params)


class RequestTool(RequestMixin):
    """Derived from RequestMixin, it provides simply the required signature.
    """
    
    def __init__(self, context, request):
        self.context = context
        self.request = request


class XBrowserView(BrowserView, RequestMixin):
    """An extended BrowserView providing the RequestMixin functions.
    """
