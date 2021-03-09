"""
solving the issue of 
No module named 'psycopg2'
(venv) deployment-user@app-server:~/polling$ sudo pip install psycopg2
(venv) deployment-user@app-server:~/polling$ sudo python3 manage.py migrate

https://serverfault.com/questions/619879/psycopg2-not-found-by-django-after-installing-in-virtualenv

"""

#Activate the virtual environment created for the project.
 E:\projects\devops-project> django-projects\Scripts\activate.bat


#run the command test
E:\projects\devops-project\django-projects\polling> pip install psycopg2


deployment-user@app-server:~$ source venv/bin/activate
(venv) deployment-user@app-server:~/polling$ sudo python3 manage.py test