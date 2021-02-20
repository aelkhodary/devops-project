> sudo shutdown now

##aelkhodary-desktop
#to make desktop full screen
~> sudo apt install gcc make perl
# get the ip of machine
>ip a
#install openssh server to able to connect to desktop remotly
>sudo apt install openssh-server
# Connect to desktop ubuntu remotly througth cmd .
> ssh aelkhodary@192.168.56.101

#

##aelkhodary@aelkhodary-desktop
#create public key
~>ssh-keygen
~>la
~>ls .ssh
~>cat .ssh/id_rsa.pub
~>ctrl+C
##aelkhodary@app-server
#create .ssh file
~>mkdir .ssh
~>la
~>touch .ssh/authorized_keys
~>ls .ssh
~>nano .ssh/authorized_keys(# past the lines from id_rsa.pub)
##aelkhodary@aelkhodary-desktop
~>ssh aelkhodary@192.168.56.101 (#you note that pass not required)
