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

class HTMLRendererMixin(object):
    """IHTMLRenderer implementation
    """
    
    implements(IHTMLRenderer)
    
    def _tag(self, name_, value_, **kw):
        attrs = ' '.join('%s="%s"' % (key, value) for key, value in kw.items())
        attrs = attrs and ' %s' % attrs or ''
        return '<%(name)s%(attrs)s>\n%(value)s\n</%(name)s>\n' % {
            'name': name_, 'attrs': attrs, 'value': value_,
        }
    
    def _selection(self, name, css, vocab, multiple=False):
        options = ''
        for term in vocab:
            kw = {'value': term[0]}
            if term[2]:
                kw['selected'] = 'selected'
            option = self._tag('option', term[1], **kw)
            options = '%s%s' % (options, option)
        kw = {'name': name, 'class': css}
        if multiple:
            kw['multiple'] = 'multiple'
        return self._tag('select', options, **kw)
