'''
https://about.gitlab.com/install/#ubuntu
#new machine name
aelkhodary@gitlab-server
'''
# 1. Install and configure the necessary dependencies
~>sudo apt-get update
~>sudo apt-get install -y curl openssh-server ca-certificates tzdata perl
#2. Add the GitLab package repository and install the package
# Add the GitLab package repository.
~>curl https://packages.gitlab.com/install/repositories/gitlab/gitlab-ee/script.deb.sh | sudo bash

~>sudo EXTERNAL_URL="http://gitlab.scad.com" apt-get install gitlab-ee
