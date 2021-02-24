'''
https://www.djangoproject.com/
https://docs.djangoproject.com/en/3.1/intro/install/
https://docs.djangoproject.com/en/3.1/topics/install/#installing-official-release
https://docs.djangoproject.com/en/3.1/howto/windows/
https://tutorial.djangogirls.org/en/django_admin/
'''

# first activate your enviroment with this command
#Activate the virtual environment created for the project.
~> django-projects\Scripts\activate.bat
~>py -m pip install Django
#check version
~>py -m django --version
# we are building a pooling application
django-projects~>django-admin startproject polling
django-projects~>ls #now you see your website polling
django-projects~>cd polling
django-projects\polling~>python manage.py migrate
django-projects\polling~>py manage.py runserver
#http://127.0.0.1:8000/
#https://tutorial.djangogirls.org/en/django_admin/
django-projects\polling~> py manage.py createsuperuser

#Username (leave blank to use 'amelkhodary'): admin
#Email address: admin@yahoo.com
#Password:admin

django-projects\polling~>pip install python-decouple
