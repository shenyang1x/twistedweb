# from urllib import urlretrieve

# def firstNonBlank(lines):
#     for eachLine in lines:
#         if not eachLine.strip():
#             continue
#         else:
#             return eachLine

# def firstLast(webpage):
#     f = open(webpage)
#     lines = f.readlines()
#     f.close()
#     print firstNonBlank(lines), lines.reverse()

# def download(url='https://www.baidu.com/', process=firstLast):
#     # try:
#     retval = urlretrieve(url)[0]
#     # except IOError:
#         # retval = None
#     # if retval:
#     #     process(retval)
#     print retval

# if __name__ == '__main__':
#     download()

# from twisted.web.server import Site
# from twisted.web.resource import Resource
# from twisted.internet import reactor
# from twisted.web.static import File

# root = Resource()
# root.putChild("tmp", File("c:/temp"))
# root.putChild("drv", File("c:/drivers"))
# root.putChild("win", File("c:/windows"))

# factory = Site(root)
# reactor.listenTCP(8888, factory)
# reactor.run()

# from twisted.web.server import Site
# from twisted.web.resource import Resource
# from twisted.internet import reactor

# from calendar import calendar

# class YearPage(Resource):
#     def __init__(self, year):
#         Resource.__init__(self)
#         self.year = year

#     def render_GET(self, request):
#         return "<html><body><pre>%s</pre></body></html>" % (calendar(self.year))

# class Calendar(Resource):
#   def getChild(self, name, request):
#       print name
#       return YearPage(int(name))

# root = Calendar()
# factory = Site(root)
# reactor.listenTCP(8880, factory)
# reactor.run()

# from twisted.internet import reactor
# from twisted.web.server import Site
# from twisted.web.resource import Resource
# import time

# class ClockPage(Resource):
#     isLeaf = True
#     def render_GET(self, request):
#         return "<html><body>%s</body></html>" % (time.ctime(),)

# resource = ClockPage()
# factory = Site(resource)
# reactor.listenTCP(8888, factory)
# reactor.run()

# from twisted.web.server import Site
# from twisted.web.resource import Resource, NoResource
# from twisted.internet import reactor

# from calendar import calendar

# class YearPage(Resource):
#     def __init__(self, year):
#         Resource.__init__(self)
#         self.year = year

#     def render_GET(self, request):
#         return "<html><body><pre>%s</pre></body></html>" % (
#             calendar(self.year), )

# class Calendar(Resource):
#     def getChild(self, name, request):
#         try:
#             year = int(name)
#         except ValueError:
#             return NoResource()
#         else:
#             return YearPage(year)

# root = Calendar()
# factory = Site(root)
# reactor.listenTCP(8880, factory)
# reactor.run()

# from twisted.web.server import Site
# from twisted.web.resource import Resource
# from twisted.internet import reactor

# import cgi

# class FormPage(Resource):
#     def render_GET(self, request):
#         return '<html><body><form method="POST" action="./form">Name:<input name="the-name" type="text" /> \
#         <br />Age:<input name="the-age" type="text" /><br /> \
#         <input type="submit" value="submit" /></form></body></html>'

#     def render_POST(self, request):
#         return '<html><body>You submitted: Name:%s,Age:%s</body></html>' % (cgi.escape(request.args["the-name"][0]),
#                                                                          cgi.escape(request.args["the-age"][0]),)

# root = Resource()
# root.putChild("form", FormPage())
# factory = Site(root)
# reactor.listenTCP(8880, factory)
# reactor.run()

# from twisted.internet import reactor
# from twisted.web.resource import Resource
# from twisted.web.server import Site

# class ShowSession(Resource):
#     def render_GET(self, request):
#         return 'Your session id is: ' + request.getSession().uid

# class ExpireSession(Resource):
#     def render_GET(self, request):
#         request.getSession().expire()
#         return 'Your session has been expired.'

# resource = ShowSession()
# resource.putChild("expire", ExpireSession())
# resource.putChild('getsession',ShowSession())

# factory = Site(resource)
# reactor.listenTCP(8880, factory)
# reactor.run()

# from twisted.internet import reactor
# from twisted.python.components import registerAdapter
# from twisted.web.resource import Resource
# from twisted.web.server import Session, Site
# from zope.interface import Interface, Attribute, implements

# class ICounter(Interface):
#     value = Attribute("An int value which counts up once per page view.")

# class Counter(object):
#     implements(ICounter)

#     def __init__(self, session):
#         self.value = 0

# registerAdapter(Counter, Session, ICounter)

# class CounterResource(Resource):
#     def render_GET(self, request):
#         session = request.getSession()
#         counter = ICounter(session)
#         counter.value += 1
#         return "Visit #%d for you!" % (counter.value, )

# resource = CounterResource()
# resource.putChild("count", CounterResource())
# factory = Site(resource)
# reactor.listenTCP(8880, factory)
# reactor.run()

# is_this_global = 'xyz'

# def foo():
#     global is_this_global
#     this_is_local = 'abc'
#     is_this_global = 'def'
#     print this_is_local + is_this_global

# foo()
# print is_this_global

# def foo():
#     m = 3

#     def bar():
#         n = 4
#         print m + n

# print m
# bar()

# def counter(start_at=0):
#     count = [start_at]

#     def incr():
#         count[0] += 1
#         return count[0]

#     return incr

# def info(object, spacing=10, collapse=1):
#     '''Test'''
#     methodList = [
#         method for method in dir(object) if callable(getattr(object, method))
#     ]
#     processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
#     print "\n".join([
#         "%s %s" % (method.ljust(spacing),
#                    processFunc(str(getattr(object, method).__doc__)))
#         for method in methodList
#     ])

# if __name__ == "__main__":
#     print info.__doc__

# li = []
# print info(li)

from twisted.web import server
from twisted.web.resource import Resource
from twisted.internet import reactor, endpoints


class Hello(Resource):
    isLeaf = True

    def getChild(self, name, request):
        if name == '':
            return self
        return Resource.getChild(self, name, request)

    def render_GET(self, request):

        return "Hello, world! I am located at %r." % (request.path, )


resource = Hello()
root = Hello()
# root.putChild('fred', Hello())
# root.putChild('bob', Hello())

site = server.Site(root)
endpoint = endpoints.TCP4ServerEndpoint(reactor, 8080)
endpoint.listen(site)
reactor.run()
