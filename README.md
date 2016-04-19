## Feature-Request
===================
###Features of the app
* This app alows user to add client ("Client A, B, and C") requested feature for an existing software. 
* If the same client requests another feature with the same priority the previous feature rquest priority will be pushed down.
"Request, Requested Features, Sorted by Clients, JSON Data"

* Request allows user to request a feature. 

* Requested Features shows all the feature requests from all the clients

* Sorted by Clients give Feature Requests by Clients

* JSON Data provides json data of three clients


####To run the project 
You simply use "make" command from 'Feature-Request' directory. Before you run you need to make sure you have the following packages installed on your machine. 

This project is only intended to run on Mac OS X El Capitan Version 10.11.4 
INSTALLATION
------------
####You will need to have "pip" installed 
######Pip is a package management system used to install and manage software packages written in Python.
Here is the link to install "pip" https://pip.pypa.io/en/stable/installing/
#######OR follow these instructions
Download file from (Save Page as by right clicking) https://bootstrap.pypa.io/get-pip.py
#######From terminal simply type 
`sudo python get-pip.py`
####You will need to install SQLAlchemy, Flask

#######To install  SQLAlchemy: 
`sudo pip install SQLAlchemy`

#######To install Flask: 
`sudo pip install Flask`

 

To provide server functionality I have used Python. Framework called Flask is mainly used in this with SQLAlachemy to keep up with the data. 
