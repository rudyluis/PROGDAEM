from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import ORM
from ORM import Base

engine = create_engine('postgresql://postgres:123456@localhost/jardineria_bkp')

# Llamar a create_all en Base.metadata
Base.metadata.create_all(engine)
