#
# Copyright 2008, Blue Dynamics Alliance, Austria - http://bluedynamics.com
#
# GNU General Public Licence Version 2 or later

__author__ = """Robert Niederreiter <rnix@squarewave.at>"""
__docformat__ = 'plaintext'

from zope.interface import Interface
from zope.interface import Attribute

REQUEST = 1
COOKIE = 2
SESSION = 3

class IRequestMixin(Interface):
    """A request helper mixin.
    
    An implementation of this interface is supposed to be derived from when
    request operations are desired.
    
    The convention is to provide self.context and self.request on the deriving
    object.
    """
    
    nameprefix = Attribute(u"prefix for param keys")
    
    checkboxpostfix = Attribute(u"postfix for detecting emplty checkbox values")
    
    def writeFormData(additionals=None, ignores=None, considerexisting=False,
                      considerspecific=None, nameprefix=False, checkboxes=[],
                      writechain=(COOKIE)):
        """Write data to storages defined in chain.
        
        @param additionals - a dict containing additional request params.
        @param ignores - a list of param names to ignore.
        @param considerexisting - When set to True, this forces to consider all
                                  existing parameters from request.form, but
                                  additionals overrule them anyway.
        @param considerspecific - list of param names to consider specific.
                                  only takes effect if considerexisting is set
                                  to False. this attribute rules ignores.
        @nameprefix - An alternative nameprefix. If explicit set to None,
                      nameprefix is ignored.
        @param checkboxes - list of names representing checkboxes. If set,
                            check for param 'name_checkboxpostfix' as well.
        @param writechain - storage chain to write to.
        """
    
    def makeUrl(context=None, url=None, resource=None, query=None):
        """Make a URL.
        
        @param context - a context to get the URL from, if not given, 
                         url or self.context.absolute_url() is used.
        @param url - a URL to use, if not given, self.context.absolute_url()
                     is used.
        @param resource - a template, browser resource or similar to append
                          to the url.
        @param query - a query to append to the url.
        @return string - the URL.
        """
    
    def makeQuery(additionals=None, ignores=None, considerexisting=False,
                  considerspecific=None, nameprefix=False):
        """Make a query string.
        
        @param additionals - a dict containing additional request params.
        @param ignores - a list of param names to ignore.
        @param considerexisting - When set to True, this forces to consider all
                                  existing parameters from request.form, but
                                  additionals overrule them anyway.
        @param considerspecific - list of param names to consider specific.
                                  only takes effect if considerexisting is set
                                  to False. this attribute rules ignores.
        @param nameprefix - An alternative nameprefix. If explicit set to None,
                            nameprefix is ignored.
        @return string - the query.
        """
    
    def formvalue(name, default=None, checkbox=False, nameprefix=False):
        """Return value for name from form or default.
        
        @param name - the name of the requested parameter.
        @param default - default value to return if param by name not exists.
        @param checkbox - Flag defining wether expected value comes from
                          checkbox. If set to True, check for param
                          'name_checkboxpostfix' as well.
        @param nameprefix - An alternative nameprefix. If explicit set to None,
                            nameprefix is ignored.
        @return value - the requested value or default.
        """
    
    def cookievalue(name, default=None, nameprefix=False):
        """Return value for name from cookie or default.
        
        @param name - the name of the requested parameter.
        @param default - default value to return if param by name not exists.
        @param nameprefix - An alternative nameprefix. If explicit set to None,
                            nameprefix is ignored.
        @return value - the requested value or default.
        """
    
    def sessionvalue(name, default=None, nameprefix=False):
        """Return value for name from session or default.
        
        @param name - the name of the requested parameter.
        @param default - default value to return if param by name not exists.
        @param nameprefix - An alternative nameprefix. If explicit set to None,
                            nameprefix is ignored.
        @return value - the requested value or default.
        """
    
    def requestvalue(name, default=None, checkbox=False,
                     chain=(REQUEST, COOKIE), nameprefix=False):
        """Return value for name or default.
        
        Try to read value either from request.form, from cookie or from session,
        order is defined by chain, first one found is returned. If no one is
        found the default value is returned.
        
        @param name - the name of the requested parameter.
        @param default - default value to return if param by name not exists.
        @param checkbox - Flag defining wether expected value comes from
                          checkbox. If set to True, check for param
                          'name_checkboxpostfix' as well.
        @param chain - chain defines the lookup order.
        @param nameprefix - An alternative nameprefix. If explicit set to None,
                            nameprefix is ignored.
        @return value - the requested value or default.
        """
    
    def xrequestvalue(name, default=None, checkbox=False,
                      chain=(REQUEST, COOKIE), nameprefix=False):
        """Extended requestvalue function.
        
        Return value for name or default.
        
        Try to read value either from request.form, from cookie or from session,
        order is defined by chain, first one found is returned.
        
        Additional, if nothing is found try:
        
          * to lookup named adapter for IRequestDefaultValue by nameprefix on
            self.context.
          * if nameprefix not set, try too lookup IRequestDefaultValue as
            regular adapter.
          * if adapter returned, try to read value by name from
            IRequestDefaultValue implementation
        
        If nothing was found anyway the default value is returned.
        
        @param name - the name of the requested parameter.
        @param default - default value to return if param by name not exists.
        @param checkbox - Flag defining wether expected value comes from
                          checkbox. If set to True, check for param
                          'name_checkboxpostfix' as well.
        @param chain - chain defines the lookup order.
        @param nameprefix - An alternative nameprefix. If explicit set to None,
                            nameprefix is ignored.
        @return value - the requested value or default.
        """
    
    #@deprecation.deprecate("selected() will be removed in version 2.0.")
    def selected(name, value, cookiewins=False):
        """Check wether request contains param by name and if value is value
        of this param.
        
        @param name - the name of the request parameter
        @param value - the value to check against
        @param cookiewins - flag wether to prefer value from cookie
        @return bool - wether requested parameter contains value equal to value
        """
    
    def formselected(name, value, nameprefix=False):
        """Check wether request contains param by name and if value is value
        of this param.
        
        @param name - the name of the requested parameter.
        @param value - the value to check against.
        @param nameprefix - An alternative nameprefix. If explicit set to None,
                            nameprefix is ignored.
        @return bool - wether requested parameter contains value equal to value.
        """
    
    def cookieselected(name, value, nameprefix=False):
        """Check wether cookie contains param by name and if value is value
        of this param.
        
        @param name - the name of the requestrd parameter.
        @param value - the value to check against.
        @param nameprefix - An alternative nameprefix. If explicit set to None,
                            nameprefix is ignored.
        @return bool - wether requested parameter contains value equal to value.
        """
    
    def sessionselected(name, value, nameprefix=False):
        """Check wether session contains param by name and if value is value
        of this param.
        
        @param name - the name of the requested parameter.
        @param value - the value to check against.
        @param nameprefix - An alternative nameprefix. If explicit set to None,
                            nameprefix is ignored.
        @return bool - wether requested parameter contains value equal to value.
        """
    
    def requestselected(name, value,
                        chain=(REQUEST, COOKIE),
                        nameprefix=False):
        """Check for requested param by name and if value is value
        of this param.
        
        Try to read value either from request.form, from cookie or from session,
        order is defined by chain, first one found is used (remaining are
        ignored).
        
        @param name - the name of the requested parameter.
        @param value - the value to check against.
        @param chain - chain defines the lookup order.
        @param nameprefix - An alternative nameprefix. If explicit set to None,
                            nameprefix is ignored.
        @return bool - wether requested parameter contains value equal to value.
        """
    
    def xrequestselected(name, value,
                         chain=(REQUEST, COOKIE),
                         nameprefix=False):
        """Extended requestselected function.
        
        Check for requested param by name and if value is value of this param.
        
        Try to read value either from request.form, from cookie or from session,
        order is defined by chain, first one found is used (remaining are
        ignored).
        
        Additional, try:
        
          * to lookup named adapter for IRequestDefaultValue by nameprefix on
            self.context.
          * if nameprefix not set, try too lookup IRequestDefaultValue as
            regular adapter.
          * if adapter returned, try to read value by name from
            IRequestDefaultValue implementation
        
        @param name - the name of the requested parameter.
        @param value - the value to check against.
        @param chain - chain defines the lookup order.
        @param nameprefix - An alternative nameprefix. If explicit set to None,
                            nameprefix is ignored.
        @return bool - wether requested parameter contains value equal to value.
        """
    
    def cookieset(name, value, nameprefix=False):
        """Set value to cookie by name.
        
        @param name - the name of the param to set.
        @param value - the value to set for param.
        @param nameprefix - An alternative nameprefix. If explicit set to None,
                            nameprefix is ignored.
        """
    
    def sessionset(name, value, nameprefix=False):
        """Set value to session by name.
        
        @param name - the name of the param to set.
        @param value - the value to set for param.
        @param nameprefix - An alternative nameprefix. If explicit set to None,
                            nameprefix is ignored.
        """
    
    def redirect(url):
        """Redirect to url.
        
        @param url - the url to redirect to.
        """


class IRequestDefaultValue(Interface):
    """
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
