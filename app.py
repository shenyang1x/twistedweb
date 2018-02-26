#!/usr/bin/env python
# encoding=utf-8

import os

from twisted.web.server import Site, NOT_DONE_YET
from twisted.web.resource import Resource
from twisted.web.static import File
from twisted.internet import reactor
import time
# from mako.template import Template
# from mako.lookup import TemplateLookup
from jinja2 import Environment, FileSystemLoader

app_dir = os.path.dirname(__file__)
static_dir = os.path.join(app_dir, 'static')
template_dir = os.path.join(app_dir, 'templates')

app_title = 'TestDemo'

# lookup = TemplateLookup(
#     directories=[template_dir],
#     input_encoding='utf-8',
#     output_encoding='utf-8')

env = Environment(loader=FileSystemLoader(template_dir))


class Root(Resource):
    def getChild(self, name, request):
        if name == 'static':
            return File(static_dir)
        #session = request.getSession()

        else:
            return self

    def render_GET(self, request):
        # tpl = lookup.get_template('index.html')
        request.setHeader("Content-Type", "text/html;charset=utf-8")
        tpl = env.get_template('index.html')
        return tpl.render(
            app_title=app_title, page_title='aaa').encode('utf-8')


def Echo():
    reactor.stop()
    print "the reactor is stop"


if __name__ == '__main__':

    factory = Site(Root())
    reactor.listenTCP(8880, factory)
    reactor.callLater(30, Echo)
    reactor.run()
    print "abc"
    print "test"
    print "abcdefg"
    print "ddd"
    print "abcdd"