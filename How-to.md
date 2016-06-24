#Odoo

##Install Odoo in Ubuntu Desktop

* Go to Ubuntu directory where you want to install the software. For example: ```cd /opt```
* Place install script in the directory
```
# Odoo 9 Enterprise
sudo wget https://raw.githubusercontent.com/luigisison/moxylus/master/Odoo9Enterprise/odoo-install.sh

#Odoo 9 Community
sudo wget https://raw.githubusercontent.com/luigisison/moxylus/master/Odoo9Community/install-odoo9c.sh

#Odoo 8
sudo wget https://raw.githubusercontent.com/luigisison/moxylus/master/Odoo8/odoo-install.sh
```
* (Optional) Edit the file to change parameters: ```sudo nano odoo-install.sh```
* Save changes and then make the file executable: ```sudo chmod +x odoo-install.sh```
* Execute the script to install Odoo: ```./odoo-install.sh```
* When prompted, enter your GitHub username and password to download the enterprise package.

#Linux

## Cheatsheet

```
sudo mkdir mydir --create directory
sudo rm -rf mydir --delete directory
clear --clear the terminal screen
```
* Update GIT
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install git
sudo git --version
```

# GitHub

* Reference: [How to Install Git on Ubuntu] (https://www.digitalocean.com/community/tutorials/how-to-install-git-on-ubuntu-14-04)
* Reference: [Git - Installng Git] (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
* Reference: [Ubuntu Server Guide] (https://help.ubuntu.com/lts/serverguide/git.html)

## Setup - Do once

### Install Git dependencies
```
sudo apt-get install build-essential libssl-dev libcurl4-gnutls-dev libexpat1-dev gettext unzip
```

### Install Git
```
cd /opt
sudo wget https://github.com/git/git/archive/v2.8.0.zip -O git.zip
sudo unzip git.zip
cd git-*
sudo make prefix=/usr/local install
```
### Register GitHub account
```
git config --list
git config --global user.name "Luigi Sison"
git config --global user.email lsison@moxylus.com
```

### Initialize odoo-fhir with content from GitHub
```
cd /odoo
sudo git clone --depth 1 https://github.com/luigisison/odoo-fhir.git
```

### Setup addons directory /odoo/odoo-fhir/addons
```
sudo nano /etc/odoo-server.conf
addons_path=/odoo/enterprise/addons,/odoo/odoo-server/addons,/odoo/odoo-fhir/addons
```

## Do every time a change occurs

### Upload changes
```
cd /odoo/odoo-fhir
sudo git add .
sudo git commit -m "Initial Commit" -a
sudo git push origin master
```

###Update local repository 

When remote repository changes or when error "! [rejected] master -> master (fetch first) error" occurs
```
sudo git fetch origin
sudo git pull origin master
```

##Create database
```
cd /odoo/odoo-server
createdb FHIR-DEV
./odoo.py -d FHIR-DEV --addons-path /odoo/odoo-fhir/addons
```
##Update Changes

syntax: ./odoo.py -d <database> --addons-path <directories> -i <modules>
```
cd /odoo/odoo-server
sudo service odoo-server stop
./odoo.py -d FHIR-DEV --addons-path /odoo/odoo-fhir/addons,/odoo/odoo-server/addons -u hc_base
```

##Error

###ERROR ? openerp.service.server: Failed to load server-wide module `web_kanban`
```
opt/openerp/server$ ./openerp-server --addons-path=web/addons
```

now you can assign multiple addons path,
```
opt/openerp/server$ ./openerp-server --addons-path=web/addons,../addons1,../addons2
```

##Save terminal output to a file

* Start a ```script``` session and save output to ```output.txt``` in the current directory.
```
script output.txt
```

* End a script session
```
exit
```

##Synching fork with master

* Go to local repository (e.g., /odoo/odoo-fhir)
```
cd /odoo/odoo-fhir
```
* Add master repository to upstream and check if added
```
sudo git remote add upstream https://github.com/luigisison/odoo-fhir.git
sudo git remote -v
```
* Fetch master repository and then checkout local master
```
sudo git fetch upstream
sudo git checkout master
```
* Combine the changes from the master repository with your local one, then push the changes
```
sudo git merge upstream/master
sudo git push origin master
```
