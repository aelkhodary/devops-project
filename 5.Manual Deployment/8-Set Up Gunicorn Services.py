"""
Set Up Gunicorn Services
"""
#stop the sever ctl+c
"""
https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04
"""
#,Used this command for production enviroment
deployment-user@app-serve

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

"""
server {
    listen 80;
    server_name 192.168.56.101 polling.test;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/deployment-user/polling;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}

"""

deployment-user@app-server:~/polling$ sudo ln -s /etc/nginx/sites-available/polling /etc/nginx/sites-enabled

deployment-user@app-server:~/polling$ sudo nginx -t
#nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
#nginx: configuration file /etc/nginx/nginx.conf test is successful

deployment-user@app-server:~/polling$ sudo systemctl restart nginx

deployment-user@app-server:~/polling$ sudo systemctl stop nginx