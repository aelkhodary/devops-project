"""
Installing Jenkins
https://www.jenkins.io/doc/book/installing/linux/
https://www.jenkins.io/doc/book/installing/linux/#debianubuntu
"""

aelkhodary@jenkins-server:~$ sudo apt update
aelkhodary@jenkins-server:~$ java -version
aelkhodary@jenkins-server:~$ sudo apt install openjdk-8-jdk
aelkhodary@jenkins-server:~$ wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
aelkhodary@jenkins-server:~$ sudo sh -c 'echo deb https://pkg.jenkins.io/debian binary/ > \
>     /etc/apt/sources.list.d/jenkins.list'
aelkhodary@jenkins-server:~$ sudo apt-get update
aelkhodary@jenkins-server:~$ sudo apt-get install jenkins

aelkhodary@jenkins-server:~$ sudo cat /var/lib/jenkins/secrets/initialAdminPa
ssword 

#Install suggested plugins
#Instance Configuration http://jenkins.scad.ae:8080/

