#
# Copyright 2008, Blue Dynamics Alliance, Austria - http://bluedynamics.com
#
# GNU General Public Licence Version 2 or later

__author__ = """Robert Niederreiter <rnix@squarewave.at>"""
__docformat__ = 'plaintext'

from zope.interface import Interface
from zope.interface import implements
from zope.component import adapts

from interfaces import ISelectionVocab
from interfaces import IHTMLRenderer

class SelectionVocabBase(object):
    """ISelectionVocab implementation
    """
    
    implements(ISelectionVocab)
    adapts(Interface)
    
    def __init__(self, context):
        self.context = context
    
    def __call__(self):
        raise NotImplementedError(u"``__call__()`` must be implemented by "
                                  "subclass")

class HTMLRendererMixin(object):
    """IHTMLRenderer implementation
    """
    
    implements(IHTMLRenderer)
    
    def _tag(self, name_, *args, **kw):
        attrs = ' '.join('%s="%s"' % (key.strip('_'), value) \
                                          for key, value in kw.items())
        attrs = attrs and ' %s' % attrs or ''
        return '<%(name)s%(attrs)s>\n%(value)s\n</%(name)s>\n' % {
            'name': name_, 'attrs': attrs, 'value': ' '.join(c for c in args),
        }
    
    def _selection(self, vocab_, **kw):
        options = list()
        for term in vocab_:
            optkw = {'value': term[0]}
            if term[2]:
                optkw['selected'] = 'selected'
            option = self._tag('option', term[1], **optkw)
            options.append(option)
        return self._tag('select', *options, **kw)
