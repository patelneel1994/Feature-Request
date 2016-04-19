all: setData run

setData:
	rm -f features.db
	python AddRecordsToDB.py

run:
	python app.py