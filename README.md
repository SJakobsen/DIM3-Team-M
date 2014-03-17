DIM3-Team-M
===========

Level 3 DIM Team Project

Go!Fish

We are using the standard version of python described in the Tango With Django book.

To run this project on your own machine, enter the go_fish_project directory and run the following commands:

python manage.py syncdb

(Create an admin account if you wish to use the administration page)

python populate_gofish.py

python manage.py runserver

Now, to view the project in your browser, simply navigate to http://127.0.0.1:8000/gofish/
Your admin account is not linked to a player, so be sure to register and then login in order to start playing. 
