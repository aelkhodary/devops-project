aelkhodary@jenkins-server:~$ sudo apt update
aelkhodary@jenkins-server:~$ python3 -V
aelkhodary@jenkins-server:~$ sudo apt install python3-pip
aelkhodary@jenkins-server:~$ pip3 -V
aelkhodary@jenkins-server:~$ sudo su jenkins
jenkins@jenkins-server:/home/aelkhodary$ pwd
jenkins@jenkins-server:/home/aelkhodary$ cd
jenkins@jenkins-server:~$ ls
jenkins@jenkins-server:~$ ls workspace
jenkins@jenkins-server:~$ cd workspace/polling-pipeline
jenkins@jenkins-server:~/workspace/polling-pipeline$ ls -a
# install requirments 
jenkins@jenkins-server:~/workspace/polling-pipeline$ pip3 install -r requirments.txt

jenkins@jenkins-server:~/workspace/polling-pipeline$ pip3 -V