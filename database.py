import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declaritive
import sqlalchemy.orm as _orm

DATABASE_URL = "postgresql://ubuntu:password@3.134.89.212:5432/suppliers"

engine = _sql.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declaritive.declarative_base()