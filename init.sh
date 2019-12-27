  
#!/bin/bash

export LC_ALL=C.UTF-8
export LANG=C.UTF-8


echo "<<<<<<<< Database Setup and Migrations Starts >>>>>>>>>"

# Run database migrations
python3 manage.py makemigrations && python3 manage.py migrate

# the script to create data in the database


echo "<<<<<<<<<<<<<<<<<<<< START API >>>>>>>>>>>>>>>>>>>>>>>>"
sleep 3

# Start the API
gunicorn --workers 2 -t 3600 school.wsgi -b 0.0.0.0:8000 --access-logfile '-' --reload