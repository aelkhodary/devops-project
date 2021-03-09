'''

Set up a Dedicated Deploy User on Production Server

'''

1-Run app-server
2-Create new user navigate to the root user
3-~>sudo su
4-aelkhodary>adduser deployment-user
5-type the password of user
6- add the new user to group sudo
7-aelkhodary>usermod -aG sudo deployment-user
8->aelkhodary>exit
9-Navigate to the new user 
10-~>sudo su deployment-user
11-aelkhodary>pwd
12-aelkhodary>cd
13-aelkhodary>pwd
14-~>sudo apt update
15-~>sudo apt upgrade