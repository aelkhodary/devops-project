'''
Add Deploy User SSH Key to GitLab Account

'''
#make sure yoy are in the home
~>pwd
/home/deployment-user
#Generate the keys ssh disk gen .
~>ssh-keygen
~>la .ssh
~>cat .ssh/id_rsa.pub

#copy the key generated and add this key to gitlab