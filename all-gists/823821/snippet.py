import lxml.html

html = lxml.html.parse("http://pypi.python.org/pypi") # can take an url, a filename or an object with a .read() method
packages = html.xpath('//tr/td/a/text()') # get the text inside all "<tr><td><a ...>text</a></td></tr>"
print packages

Out[7]: 
[u'celery\xa02.2.3',
 u'django-celery\xa02.2.3',
 u'kombu\xa01.0.3',
 u'PyVirtualDisplay\xa00.0.1',
 u'django-allauth\xa00.1.0',
 u'scikits.scattpy\xa00.1.1',
 u'polib\xa00.6.2',
 u'pyramid_mailer\xa00.2.1',
 u'getpython3\xa00.1',
 u'ZODB3\xa03.10.2',
 u'pyscreenshot\xa00.1.5',
 u'timed\xa00.35',
 u'circuits\xa01.4',
 u'django-fab-deploy\xa00.3',
 u'blockdiag\xa00.6.7',
 u'renren\xa01.0.0',
 u'nose-progressive\xa00.1.2',
 u'sphinxjp.themes.htmlslide\xa00.1.0',
 u'sphinxjp.themes.s6\xa00.1.1',
 u'scunch\xa00.5.0',
 u'compare\xa00.2b',
 u'typetrainer\xa00.4.3',
 u'ladon\xa00.3.5',
 u'stalker\xa00.1.1.a6',
 u'peewee\xa00.3.2',
 u'funnelweb\xa01.0b7',
 u'transmogrify.siteanalyser\xa01.0b8',
 u'transmogrify.webcrawler\xa01.0b6dev',
 u'methodpickle\xa00.1.0',
 u'Flask-SQLAlchemy\xa00.10',
 u'py-moneyed\xa00.3',
 u'ordf\xa00.31',
 u'Divisi2\xa02.1.3',
 u'AppEngine-mlk\xa01.4.2',
 u'plumi.app\xa04.1rc1',
 u'ISAPIWSGIHelper\xa00.1.0',
 u'django-imagekit\xa00.3.4',
 u'ReviewBoard\xa01.5.3.1',
 u'plone.subrequest\xa01.6b1',
 u'Khufu-SQLAHelper\xa00.4a2']