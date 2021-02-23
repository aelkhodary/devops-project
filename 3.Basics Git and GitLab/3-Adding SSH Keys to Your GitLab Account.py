'''
# we need to access our remote repositories
througth ssh
# access this path through bash terminal "c/Users/amelkhodary"
'''
~>ls -a
~>ls .ssh
#I need to access the key that i will be using "id_rsa.pub"
#if it's not found you need to run the below command
~>ssh-keygen
#after running the above command the private and public key created
~>ls .ssh
# id_rsa  id_rsa.pub  known_hosts
~>cat .ssh/id_rsa.pub
'''
#copy the code generated
#Go to gitlab web page (SSH Keys)and add past the ssh public key
my PC name is "amelkhodary@SC-AD-LA-0910"

'''
