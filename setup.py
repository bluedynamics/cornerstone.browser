#
# Copyright 2008, Blue Dynamics Alliance, Austria - http://bluedynamics.com
#
# GNU General Public Licence Version 2 or later

__author__ = """Robert Niederreiter <rnix@squarewave.at>"""
__docformat__ = 'plaintext'

from setuptools import setup, find_packages
import sys, os

version = '1.3.5'
shortdesc = "Common browser utils for ZOPE"
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(name='cornerstone.browser',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Environment :: Web Environment',
            'Framework :: Zope2',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',            
      ], # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Robert Niederreiter',
      author_email='rnix@squarewave.at',
      url='https://svn.plone.org/svn/collective/cornerstone.browser',
      license='General Public Licence',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['cornerstone'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools', 
          'repoze.formapi',
          'Products.CMFCore', # only needed for hotspot.js !        
          # several zope eggs missing, coming soon (atm fake-eggs
      ],
      extras_require={
          'test': [
              'interlude',
              # several zope eggs missing, coming soon (atm fake-eggs            
          ]
      },      
      entry_points="""
      """,
      )
