import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, event, DDL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
 
Base = declarative_base()



engine = create_engine('sqlite:///features.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()



class RequestedFeatures(Base):
    __tablename__ = 'features'
   
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(250), nullable=False)
    description = Column(String(1000), nullable=False)
    client = Column(String(30))
    clientPriority = Column(Integer, nullable=False)
    date = Column(String(20), default="03/29/17",nullable=False)
    url = Column(String(400),nullable=False)
    productArea = Column(String(50),nullable=False)

    @property
    def serialize(self):
        return {
            'id'            : self.id,
            'title'         : self.title,
            'description'   : self.description,
            'client'        : self.client,
            'priority'      : self.clientPriority,
            'url'           : self.url,
        }


#Trigger when the same priority is being requested for same client
@event.listens_for(RequestedFeatures, 'before_insert')
def receive_before_insert(mapper, connection, target):
   
    qeury = "UPDATE features SET clientPriority = (clientPriority + 1)  WHERE client = '"
    qeury += target.client + "' AND  clientPriority >= " + str(target.clientPriority)
    qr = session.execute(qeury)
    session.commit()
    

    
class Clients(Base):
    __tablename__ = 'clients'
    
    id = Column(String(30), primary_key=True)
 



engine = create_engine('sqlite:///features.db')
Base.metadata.create_all(engine)
