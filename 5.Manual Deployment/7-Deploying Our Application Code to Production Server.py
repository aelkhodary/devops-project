'''
Deploying Our Application Code to Production Server
'''

app-server:~>git clone git@gitlab.scad.com:aelkhodary/polling.git


"""
Configure the Application Settings file File on the Production Server
"""
deployment-user@app-server:~/polling$la
#https://djecrety.ir/  # generate django secret key
#I update the settings.py & .env files

deployment-user@app-server:~/polling$nano .env

deployment-user@app-server:~/polling$ sudo pip install -r requirements.txt

deployment-user@app-server:~/polling$sudo python3 manage.py migrate
"""
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying polls.0001_initial... OK
  Applying sessions.0001_initial... OK

"""
deployment-user@app-server:~/polling$ python3 manage.py createsuperuser

Username (leave blank to use 'deployment-user'):aelkhodary
Email address: aelkhodary@scad.com
Password:welcome1

deployment-user@app-server:~/polling$ python3 manage.py collectstatic
#132 static files copied to '/home/deployment-user/polling/static'.
#start server
deployment-user@app-server:~/polling$ python3 manage.py runserver 0.0.0.0:8000

"""
#Starting development server at http://0.0.0.0:8000/
#http://192.168.56.101:8000/polls/
#http://192.168.56.101:8000/admin
user:aelkhodary
pass:welcome1
"""

#Adding Contents from the Admin Area
#http://192.168.56.101:8000/polls/