'''
aelkhodary@aelkhodary-desktop
create public key
'''
~>ssh-keygen
~>la
~>ls .ssh
~>cat .ssh/id_rsa.pub
~>ctrl+C

'''
##aelkhodary@app-server
#create .ssh file
'''
~>mkdir .ssh
~>la
~>touch .ssh/authorized_keys
~>ls .ssh
~>nano .ssh/authorized_keys(# past the lines from id_rsa.pub)
'''
##aelkhodary@aelkhodary-desktop
'''
~>ssh aelkhodary@192.168.56.101 (#you note that pass not required)
