#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kurohai
# @Date:   2015-11-18 21:47:31
# @Last Modified by:   root
# @Last Modified time: 2015-11-18 21:50:06

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect
from sqlalchemy import MetaData, Table
from flask import Flask
import datetime
import os
import logging
from logging.handlers import RotatingFileHandler


# data_models = [
#     'arcustmr', 
#     'sainvlin', 
#     'sainvhdr',
#     'division',
#     'artransf',
# ]



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
