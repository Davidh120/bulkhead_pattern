from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()
engine = create_engine('sqlite:///database_with_bulkhead.db')
Session = sessionmaker(bind=engine)
session = Session()

class Producto(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    precio = Column(Integer, nullable=False)

class Pago(Base):
    __tablename__ = 'pagos'
    id = Column(Integer, primary_key=True)
    producto_id = Column(Integer, ForeignKey('productos.id'), nullable=False)
    cancelado = Column(Boolean, nullable=False)
    producto = relationship('Producto')

def inicializar_bd():
    Base.metadata.create_all(engine)