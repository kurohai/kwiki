import os
import cherrypy
from cherrypy import wsgiserver
from cherrypy.process.plugins import Daemonizer,PIDFile
from flask.ext.script import Manager
from kwiki.kwikiapp import kwikifapp


manager = Manager(kwikifapp)


@manager.command
def db():
    Base.metadata.create_all(bind=engine)


@manager.command
def quick():
    d = wsgiserver.WSGIPathInfoDispatcher({'/': kwikifapp})
    server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', 80), d, server_name=kwikifapp.appname, )
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()


@manager.command
def go():
    kwikifapp.run(debug=True, host='0.0.0.0', port=8080)


if __name__ == '__main__':
    manager.run()
