import os
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

db_configuration = os.getenv("db_conf")
if not db_configuration:
    raise Exception('db connection info should be '
        'specified as env variable "db_conf"')

base = automap_base()

engine = create_engine(db_configuration)

base.prepare(engine, reflect=True)

orders = base.classes.orders

session = Session(engine)
