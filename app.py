import os
from flask import Flask,render_template, jsonify, Response, request, url_for, redirect
from sqlalchemy import create_engine, update, orm
from sqlalchemy.orm import sessionmaker, mapper
from database_setup import Base, Clients, RequestedFeatures
app = Flask(__name__)
NUMBER_OF_CLIENTS = 3

engine = create_engine('sqlite:///features.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.errorhandler(404)
def not_found(error):
	return "Wrong location"


@app.route('/requests')
def template_test():
	table = session.query(RequestedFeatures).order_by("client").all()
	#table = session.query(RequestedFeatures).filter_by(client='Client A').all()
	return render_template('requests.html',features=table)



@app.route('/', methods=['GET','POST'])
def feature_request():
	if request.method == 'POST':
		return render_template('newrequest.html',feature=session.query(RequestedFeatures).last())
	else:
		return render_template('index.html')





@app.route('/addedFeature', methods=['POST'])
def addedFeature():
	cl = ""
	increment = False
	clName = request.form['clientname']
	clPriority = request.form['clientpriority']
	print "inserting"

	feature = RequestedFeatures(title=request.form['title'],description=request.form['description'],client=request.form['clientname'],clientPriority=int(request.form['clientpriority']),date=request.form['targetDate'],url=request.form['targetLink'],productArea=request.form['productArea'])
	session.add(feature)
	session.commit()
	return render_template('newrequest.html',feature_data=feature.title)

@app.route('/getClientsJSON')
def returnJSON():
	cl1 = session.query(RequestedFeatures).filter_by(client='Client A').order_by(RequestedFeatures.clientPriority).all()
	cl2 = session.query(RequestedFeatures).filter_by(client='Client B').order_by(RequestedFeatures.clientPriority).all()
	cl3 = session.query(RequestedFeatures).filter_by(client='Client C').order_by(RequestedFeatures.clientPriority).all()
	return jsonify(Features=[[i.serialize for i in cl1],[i.serialize for i in cl2],[i.serialize for i in cl3]])





@app.route('/JSONData')
def JSONData():
	return render_template('JSONData.html')

@app.route('/sortedbyclients')
def sortedbyclients():
	cl1 = session.query(RequestedFeatures).filter_by(client='Client A').order_by(RequestedFeatures.clientPriority).all()
	cl2 = session.query(RequestedFeatures).filter_by(client='Client B').order_by(RequestedFeatures.clientPriority).all()
	cl3 = session.query(RequestedFeatures).filter_by(client='Client C').order_by(RequestedFeatures.clientPriority).all()

	return render_template('sortedbyclients.html',clients=[cl1, cl2, cl3])

def filterbyvalue(seq, value):
   for el in seq:
       if el.attribute==value: yield el

if __name__ == '__main__':
	app.debug = True
	app.run()

