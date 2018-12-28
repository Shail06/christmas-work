# ChristmasWork
This project aims to compare the money received by using the International Money Transfer Services like TransferWise, Xendpay etc.

The Database models will handle all the APIs, parameters, headers for the request.

BASIC STRUCTURE

moneycompare
	|-- src		(directory containing the files implementing the API request response handler)
	|-- templates	(directory containing HTML files that present on the web) 
	|-- migrations	(directory containing python files that implement Database Models declared in models.py)
	|-- admin.py	(Controls the Administrative website of the project. All the Database Administration can be done from Admin website)
	|-- models.py	(Contains declaration of the Database models)
	|-- urls.py	(contains URLs/paths for the webpages in the project)
	|-- views.py	(This file renders the Views or templates of the project)


RUNNING THE PROJECT

#### It is better to have python3, pip, virtualenv / virtualenvwrapper installed before performing the steps #######

1) Clone the Project on your local system
	git clone https://github.com/Shail06/ChristmasWork.git

2) Inside the 'ChristmasWork' execute the following:
	pip install -r requirements.txt

3) Go to DjangoProject and execute following:
	python manage.py makemigrations		## This will create models and SQLite Database file
	python manange.py migrate		## This will register the models to admin

4) Run the project
	python manage.py runserver

5) Add the relevant data in the models at: http://localhost:8000/admin/

6) Check the browser: http://localhost:8000/moneycompare/


