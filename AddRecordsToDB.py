from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from database_setup import Clients, RequestedFeatures, Base
 
engine = create_engine('sqlite:///features.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()






#Features
feature = RequestedFeatures(title='Add iOS app', description='Just need an iOS app for the web app.......',client='Client A',clientPriority='1',date='09/20/17',url='google.com',productArea='Policies')
session.add(feature)
session.commit()

feature1 = RequestedFeatures(title='Add Android app', description='Just need an Android app for the web app.......',client='Client B',clientPriority='1',date='09/20/17',url='google.com',productArea='Policies')
session.add(feature1)
session.commit()

feature2 = RequestedFeatures(title='Add BlackBerry app', description='Just need an BlackBerry app for the web app.......',client='Client C',clientPriority='3',date='09/20/17',url='google.com',productArea='Policies')
session.add(feature2)
session.commit()

feature3 = RequestedFeatures(title='Web Application', description='I need a web app with Javascript blahhhh',client='Client A',clientPriority='1',date='09/20/17',url='google.com',productArea='Claims')
session.add(feature3)
session.commit()

feature4 = RequestedFeatures(title='Java Chat App', description='Client needs a Java based Chat app',client='Client A',clientPriority='3',date='09/20/17',url='google.com',productArea='Policies')
session.add(feature4)
session.commit()


feature5 = RequestedFeatures(title='Python file transfer', description='I need python File transfer system',client='Client C',clientPriority='1',date='09/20/17',url='google.com',productArea='Policies')
session.add(feature5)
session.commit()

feature6 = RequestedFeatures(title='AWS app', description='Client needs to implment a server app, alskdjflakjjfaslk; alskfdjla fjlsalf asfsjlf ',client='Client C',clientPriority='2',date='09/20/17',url='google.com',productArea='Policies')
session.add(feature6)
session.commit()
