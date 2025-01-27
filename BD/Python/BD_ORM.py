from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ORM import Base
if __name__=='__main__':
    engine = create_engine('postgresql://postgres:123456@localhost/jardineria_bkp')

    # Llamar a create_all en Base.metadata
    Base.metadata.create_all(engine)