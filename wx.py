# -*- coding: UTF-8 -*-
#!/usr/bin/python

import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        web.header('Content-Type','text/html; charset=UTF-8')
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()