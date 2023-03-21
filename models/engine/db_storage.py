#!/usr/bin/python3
"""This represents the DB storage class"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity


class DBStorage:
    """Representst the DB class"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(os.getenv("HBNB_MYSQL_USER"),
                                             os.getenv("HBNB_MYSQL_PWD"),
                                             os.getenv("HBNB_MYSQL_HOST"),
                                             os.getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True
                                      )
        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query the cuurent DB base on the cls value"""
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls)
        else:
            objs.self__session.query(State).all()
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        return {"{}.{}".format(type(obj).__name__, obj.id):
                obj for obj in objs}

    def new(self, obj):
        """Add Obj to current DB session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to DB"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current DB session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database and initialize a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
