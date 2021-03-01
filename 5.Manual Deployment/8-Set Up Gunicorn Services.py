"""
Set Up Gunicorn Services
"""
#stop the sever ctl+c
"""
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04
"""
#,Used this command for production enviroment
deployment-user@app-server:~/polling$ gunicorn --bind 0.0.0.0:8000 polling.wsgi

~>ctr+c
deployment-user@app-server:~/polling$ deactivate
deployment-user@app-server:~/polling$ sudo nano /etc/systemd/system/gunicorn.socket
deployment-user@app-server:~/polling$ sudo nano /etc/systemd/system/gunicorn.service
"""
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=deployment-user
Group=www-data
WorkingDirectory=/home/deployment-user/polling
ExecStart=/home/deployment-user/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/gunicorn.sock \
          polling.wsgi:application

[Install]
WantedBy=multi-user.target

"""

deployment-user@app-server:~/polling$ sudo systemctl start gunicorn.socket
deployment-user@app-server:~/polling$ sudo systemctl enable gunicorn.socket

deployment-user@app-server:~/polling$ sudo systemctl daemon-reload
deployment-user@app-server:~/polling$ sudo systemctl restart gunicorn

deployment-user@app-server:~/polling$ sudo systemctl status gunicorn

deployment-user@app-server:~/polling$sudo nano /etc/nginx/sites-available/polling

