#!/bin/env python

import os
import cherrypy
from cherrypy import wsgiserver
from cherrypy.process.plugins import Daemonizer,PIDFile
from flask.ext.script import Manager
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.app import app as flasky
from app.app import Base, engine, User, db, session

manager = Manager(flasky)

# Session = sessionmaker(bind=engine)
# session = Session()



@manager.command
def defaults():
    basic_data()
    superuser()


@manager.command
def create_tables():
    """Create relational database tables."""
    Base.metadata.create_all(bind=engine)


@manager.command
def drop_tables():
    """Drop all project relational database tables. THIS DELETES DATA."""
    Base.metadata.drop_all(bind=engine)


@manager.command
def redo():
    drop_tables()
    create_tables()
    defaults()


@manager.command
def superuser():
    """Create superuser"""
    admin = User()
    admin.email='root'
    admin.password='secret'
    admin.name = 'root'
    session.add(admin)
    session.commit()


@manager.command
def basic_data():
    """Initialize basic DB data."""
    # db.session.add(data)
    # db.session.commit()
    pass


@manager.command
def start():
    d = wsgiserver.WSGIPathInfoDispatcher({'/flasky/':flasky})
    server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', 80), d, server_name='flasky', )
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()


@manager.command
def daemon():
    default_pid = os.path.join('/var/run', 'flasky.pid')

    cherrypy.config.update({
        'server.socket_host':'0.0.0.0',
        'server.socket_port':80,
    })

    cherrypy.tree.graft(vmms, '/vmms/')
    Daemonizer(cherrypy.engine).subscribe()
    PIDFile(cherrypy.engine, default_pid).subscribe()

    cherrypy.engine.start()


@manager.command
def stop():
    import cherrypy
    cherrypy.engine.stop()


if __name__ == '__main__':
    manager.run()
