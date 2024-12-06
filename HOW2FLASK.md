okay so start with 

pip install flask flask-cors
pip install psycopg-binary configparser
python
import flask

then exit out of the python terminal thing

download postman (for testing connection)
continue as guest u dont need to sign up for anything

run app.py 

in postman, enter the default link and click send
default link is http://127.0.0.1:5000/

if that works, try this http://127.0.0.1:5000/movies/search?query=Inception
* you can change Inception to any movie lol


notes:
- i didn't use the config file, so you will have to change the db_connection.py file based on how u do it in db_helper.py
- same thing for db_helper.py, if ryan's works, you can use that
- if you use mine, then just make sure to change the variables in DB=CONFIG and the db_connection file