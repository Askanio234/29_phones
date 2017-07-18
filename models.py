import os
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

db_configuration = os.getenv("DB_URI")
if not db_configuration:
    raise EnvironmentError('db URI should be '
        'specified as env variable "DB_URI"')

base = automap_base()

engine = create_engine(db_configuration)

base.prepare(engine, reflect=True)

orders = base.classes.orders

session = Session(engine)
