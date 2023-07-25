from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()


class Menu(Base):
    __tablename__ = 'menu'

    id = Column(Integer, primary_key=True)
    title  = Column(String, nullable=False, unique=True)
    description = Column(String)
    submenus = relationship(
        "SubMenu", 
        back_populates="menu", 
        cascade="all, delete-orphan"
    )


class SubMenu(Base):
    __tablename__ = 'submenu'

    id = Column(Integer, primary_key=True)
    title  = Column(String, nullable=False, unique=True)
    description = Column(String)
    menu = relationship("Menu", back_populates="submenus")
    menu_id = Column(Integer, ForeignKey('menu.id'))
    dishes = relationship(
        "Dish", 
        back_populates="submenu", 
        cascade="all, delete-orphan"
    )


class Dish(Base):
    __tablename__ = 'dish'

    id = Column(Integer, primary_key=True)
    title  = Column(String, nullable=False, unique=True)
    description = Column(String)
    price = Column(String, nullable=False)
    submenu = relationship("SubMenu", back_populates="dishes")
    submenu_id = Column(Integer, ForeignKey('submenu.id'))
