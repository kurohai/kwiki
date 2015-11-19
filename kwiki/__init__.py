#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kurohai
# @Date:   2015-11-18 21:47:31
# @Last Modified by:   root
# @Last Modified time: 2015-11-18 22:24:33


from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy import create_engine, inspect
from sqlalchemy import MetaData, Table
from sqlalchemy.ext.declarative import *
from flask import Flask
import datetime
import os
from dicto import dicto
import flask.ext.restless
from flask.ext.socketio import SocketIO
from flask.ext.admin import Admin
from flask.ext.admin.contrib.sqla import ModelView


appname = 'Kwiki App'
appnamed = 'kwiki'
pwd = os.path.abspath(os.curdir)

dbpath = '{dir}/{app}.db'.format(dir=pwd, app=appnamed)
dburi = 'sqlite:///{db}'.format(db=dbpath)


@as_declarative()
class BaseBase(dicto):

    def __hash__(self):
        return hash(self.id)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


Base = BaseBase

engine = create_engine(dburi)
metadata = MetaData(bind=engine)
session = Session(engine)
db_session = scoped_session(
    sessionmaker(
        autocommit=True,
        autoflush=True,
        bind=engine
    )
)

Base.metadata = metadata
Base.query = db_session.query_property()


from models import *
from kwikiapp import kwikifapp



# engine = create_engine("oracle://arigsby:OraDBImodule@brv5db:1521/VMS5")

# insp = inspect(engine)

# metadata = MetaData(bind=engine, schema='dsgi')

# metadata.reflect(engine, only=data_models)

# Base = automap_base(metadata=metadata)

# from models import *

# Base.prepare()


# get all table names
# tables = insp.get_table_names(schema='dsgi')


# get all column names
# arcustmr.columns = insp.get_columns('arcustmr', schema='dsgi')
# sainvlin.columns = insp.get_columns('sainvlin', schema='dsgi')
# sainvhdr.columns = insp.get_columns('sainvhdr', schema='dsgi')
# division.columns = insp.get_columns('division', schema='dsgi')
# artransf.columns = insp.get_columns('artransf', schema='dsgi')


# set up application
# session = Session(engine)

from forms import *
from views import blueprint
kwikifapp.register_blueprint(blueprint)
