"""
#Testing the Pipeline and Installing Blue Ocean
Blue Ocean : is a jenkins extension that let us run and 
see the results of our jenkins pipeline .
"""
#http://192.168.56.104:8080/updateCenter/

Dashboard >Plugin Manager>Blue Ocean
Installing Plugins/Upgrades
# after restart the jenkins 
# http://192.168.56.104:8080/job/polling-pipeline/
# http://192.168.56.104:8080/blue/organizations/jenkins/polling-pipeline/

#Configure Jenkinfile: Deploy

http://192.168.56.104:8080/blue/organizations/jenkins/polling-pipeline/detail/polling-pipeline/20/pipeline
#jenkins server
jenkins@jenkins-server:~$ cat .ssh/id_rsa.pub
#app sever
deployment-user@app-server:~$ nano .ssh/authorized_keys

#http://192.168.56.101/admin/