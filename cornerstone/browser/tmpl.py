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
    
    _div = """
        <div class="%(css)s">%(content)s</div>
    """
    
    def _selection(self, name, css, vocab, multiple=False):
        if multiple:
            selection = """
                <select name="%(name)s" class="%(css)s" multiple="multiple">
                    %(options)s
                </select>
            """
        else:
            selection = """
                <select name="%(name)s" class="%(css)s">
                    %(options)s
                </select>
            """
        option = """
            <option value="%(key)s">%(value)s</option>
        """
        optionselected = """
            <option value="%(key)s" selected="selected">%(value)s</option>
        """
        options = ''
        for term in vocab:
            kw = {
                'key': term[0],
                'value': term[1],
            }
            opt = term[2] and (optionselected % kw) or (option % kw)
            options = '%s\n%s' % (options, opt)
        return selection % {
            'name': name,
            'css': css,
            'options': options,
        }
    
    
    
    