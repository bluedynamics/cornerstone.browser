#
# Copyright 2008, Blue Dynamics Alliance, Austria - http://bluedynamics.com
#
# GNU General Public Licence Version 2 or later

__author__ = """Robert Niederreiter <rnix@squarewave.at>"""
__docformat__ = 'plaintext'

from zope.interface import Interface
from zope.interface import Attribute

class IRequestMixin(Interface):
    """A request helper mixin.
    
    An implementation of this interface is supposed to be derived from when
    request operations are desired.
    
    The convention is to provide self.context and self.request on the deriving
    object.
    """
    
    def makeUrl(context=None, url=None, resource=None, query=None):
        """Make a URL.
        
        @param context - a context to get the URL from, if not given, 
                         url or self.context.absolute_url() is used.
        @param url - a URL to use, if not given, self.context.absolute_url()
                     is used
        @param resource - a template, browser resource or similar to append
                          to the url
        @param query - a query to append to the url
        @return string - the URL
        """
    
    def makeQuery(additionals=None, ignores=None,
                  considerexisting=False, considerspecific=None):
        """Make a query string.
        
        @param additionals - a dict containing additional request params
        @param ignores - a list of param names to ignore
        @param considerexisting - When set to True, this forces to consider all
                                  existing parameters from request.form, but
                                  additionals overrule them anyway.
        @param considerspecific - list of param names to consider specific.
                                  only takes effect if considerexisting is set
                                  to False. this attribute rules ignores.
        @return string - the query
        """


class ConflictingHotspot(Exception):
    """Thrown if conflicting hotspot declarations are recognized for a resource.
    """


class IHotspotHitEvent(Interface):
    """Fired when a resource was recognized as hotspot.
    """
    
    context = Attribute(u"Hotspot context")
    
    request = Attribute(u"Request object")
    
    hotspoturl = Attribute(u"URL defining the hotspot")


class IHotspot(Interface):
    """Interface for the hotspot utilities
    """
    
    obj = Attribute(u"Hotspot applies to object")
    
    interface = Attribute(u"Hotspot applies to interface")
    
    resource = Attribute(u"Hotspot applies to resouce")
    
    considerparams = Attribute(u"Consider params from request")
    
    def weight(obj, request):
        """Return the weight of object for this hotspot.
        """


class IHotspotCheck(Interface):
    """Interface to check hotspots.
    """
    
    def __call__():
        """Fire IHotspotHitEvent if a resource is recognized as hotspot.
        """
