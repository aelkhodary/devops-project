'''
##aelkhodary@app-server
'''
~>sudo apt update
#after that enter password
#I want to run sudo without password
~>sudo visudo
 '''
# Before
# Allow members of group sudo to execute any command
%sudo   ALL=(ALL:ALL) ALL
#After
#Allow members of group of sudo to excute any command
%sudo ALL=(ALL)NOPASSWD: ALL
 '''
 ~>exit
 '''
#login agin througth putty
 '''
 ~>sudo apt update

  '''
 # You see that is successful without
 having to type password
 # Mean while ,the user running the sudo commands must be
 a member of the sudo group

  '''
