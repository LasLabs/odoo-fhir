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
addons_path=/odoo/odoo-server/openerp/addons,/odoo/odoo-server/addons,/odoo/odoo-fhir/addons,/odoo/odoo-server/addons/web_kanban
```

## Do every time a change occurs

### Upload changes
```
cd /odoo/odoo-fhir
sudo git add .
sudo git status
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
##Install Times Roman Font

* create **fonts** folder in `/usr/lib/python2.7/dist-packages/reportlab/`
```
cd /usr/lib/python2.7/dist-packages/reportlab/
sudo mkdir fonts
```

* download [pfbfer.zip] (http://www.reportlab.com/ftp/fonts/pfbfer.zip) to download folder
* extract it
* Put all files in `/usr/lib/python2.7/dist-packages/reportlab/fonts/`

```
sudo mv _abi____.pfb /usr/lib/python2.7/dist-packages/reportlab/fonts/_abi____.pfb
sudo mv _ab_____.pfb /usr/lib/python2.7/dist-packages/reportlab/fonts/_ab_____.pfb
sudo mv _ai_____.pfb /usr/lib/python2.7/dist-packages/reportlab/fonts/_ai_____.pfb
sudo mv _a______.pfb /usr/lib/python2.7/dist-packages/reportlab/fonts/_a______.pfb
sudo mv cobo____.pfb /usr/lib/python2.7/dist-packages/reportlab/fonts/cobo____.pfb
sudo mv cob_____.pfb /usr/lib/python2.7/dist-packages/reportlab/fonts/cob_____.pfb
sudo mv com_____.pfb /usr/lib/python2.7/dist-packages/reportlab/fonts/com_____.pfb
sudo mv coo_____.pfb /usr/lib/python2.7/dist-packages/reportlab/fonts/coo_____.pfb
sudo mv _ebi____.pfb /usr/lib/python2.7/dist-packages/reportlab/fonts/_ebi____.pfb
sudo mv _eb_____.pfb /usr/lib/python2.7/dist-packages/reportlab/fonts/_eb_____.pfb
sudo mv _ei_____.pfb /usr/lib/python2.7/dist-packages/reportlab/fonts/_ei_____.pfb
sudo mv _er_____.pfb /usr/lib/python2.7/dist-packages/reportlab/fonts/_er_____.pfb
sudo mv sy______.pfb /usr/lib/python2.7/dist-packages/reportlab/fonts/sy______.pfb
sudo mv zd______.pfb /usr/lib/python2.7/dist-packages/reportlab/fonts/zd______.pfb
sudo mv zx______.pfb /usr/lib/python2.7/dist-packages/reportlab/fonts/zx______.pfb
sudo mv zy______.pfb /usr/lib/python2.7/dist-packages/reportlab/fonts/zy______.pfb
```

##Create Data Set
*Create model file `sudo nano /odoo/odoo-fhir/addons/hc_base/models/hc_participation_type.py`
*Add model file to `__openerp__.py/data` `'data/hc_vs_participation_type_type.xml',`
*Create view file `sudo nano /odoo/odoo-fhir/addons/hc_base/views/hc_participation_type_views.xml`

##Create Module

*Rename files
```
cd /odoo/odoo-fhir/addons/hc_res_practitioner_role
sudo mv models/models.py models/hc_res_practioner_role.py
sudo mv views/views.xml views/hc_res_practioner_role_views.xml
sudo mv views/templates.xml views/hc_res_practioner_role_templates.xml
```
*Modify manifest files
```
#models/__init__.py
from . import hc_res_practitioner_role

#hc_practitioner_role/__openerp__.py
'views/hc_res_practitioner_role_views.xml',
'views/hc_res_practitioner_role_templates.xml',
```