'''
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04
'''

~>sudo apt update
~>sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx curl
~>sudo -u postgres psql
~>#CREATE DATABASE pollingdb;
~># \1 [ctl+enter] ##list all database created
~># CREATE USER pollinguser WITH PASSWORD 'password2020';
~># \du [ctl+enter] ## to list all user created
~># ALTER ROLE pollinguser SET client_encoding TO 'utf8';
~># ALTER ROLE pollinguser SET default_transaction_isolation TO 'read committed';
~># ALTER ROLE pollinguser SET timezone TO 'EST';
~># GRANT ALL PRIVILEGES ON DATABASE pollingdb TO pollinguser;
~># \q
~>python3 --version
~>pip3 --version