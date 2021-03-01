'''

https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04
Set Up a Virtual Environment on the Production Server

'''

~>sudo -H pip3 install --upgrade pip
~>sudo -H pip3 install virtualenv
# create a Python virtual environment by typing at home directrly
~>virtualenv venv
~>ls -la
#Activate the virtual environment
~>source venv/bin/activate
#install Django, Gunicorn, and the psycopg2 PostgreSQL adaptor with the local instance of pip:
~>pip install django gunicorn psycopg2-binary pillow
~>python3 -m pip install --upgrade pip