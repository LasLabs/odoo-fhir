#!/bin/bash
################################################################################
# Script to create Odoo module skeletons of FHIR resources.
# Author: Luigi Sison
#-------------------------------------------------------------------------------
# Scaffolding is the automated creation of a skeleton structure to simplify bootstrapping 
# (of new modules, in the case of Odoo). While not necessary it avoids the tedium of setting up basic structures 
# and looking up what all starting requirements are.
#
# Scaffolding is available via the odoo.py scaffold subcommand.
#-------------------------------------------------------------------------------
# Go to Ubuntu directory where modules are located. For example:
# cd /odoo/odoo-server/addons
# Place this script in the directory:
# sudo wget https://raw.githubusercontent.com/luigisison/healthcare/master/Renamefile.sh
# Make the file executable:
# sudo chmod +x Renamefile.sh
# Execute the script to create the module skeletons:
# ./Renamefile.sh
################################################################################# 

sudo mv hc_account/models/models.py hc_account/models/hc_res_account.py
sudo mv hc_account/views/views.xml hc_account/views/hc_res_account_views.xml
sudo mv hc_account/views/templates.xml hc_account/views/hc_res_account_templates.xml

sudo mv hc_clinical_impression/models/models.py hc_clinical_impression/models/hc_res_clinical_impression.py
sudo mv hc_clinical_impression/views/views.xml hc_clinical_impression/views/hc_res_clinical_impression_views.xml
sudo mv hc_clinical_impression/views/templates.xml hc_clinical_impression/views/hc_res_clinical_impression_templates.xml

sudo mv hc_detected_issue/models/models.py hc_detected_issue/models/hc_res_detected_issue.py
sudo mv hc_detected_issue/views/views.xml hc_detected_issue/views/hc_res_detected_issue_views.xml
sudo mv hc_detected_issue/views/templates.xml hc_detected_issue/views/hc_res_detected_issue_templates.xml

sudo mv hc_encounter/models/models.py hc_encounter/models/hc_res_encounter.py
sudo mv hc_encounter/views/views.xml hc_encounter/views/hc_res_encounter_views.xml
sudo mv hc_encounter/views/templates.xml hc_encounter/views/hc_res_encounter_templates.xml

sudo mv hc_substance/models/models.py hc_substance/models/hc_res_substance.py
sudo mv hc_substance/views/views.xml hc_substance/views/hc_res_substance_views.xml
sudo mv hc_substance/views/templates.xml hc_substance/views/hc_res_substance_templates.xml

sudo mv hc_episode_of_care/models/models.py hc_episode_of_care/models/hc_res_episode_of_care.py
sudo mv hc_episode_of_care/views/views.xml hc_episode_of_care/views/hc_res_episode_of_care_views.xml
sudo mv hc_episode_of_care/views/templates.xml hc_episode_of_care/views/hc_res_episode_of_care_templates.xml

sudo mv hc_flag/models/models.py hc_flag/models/hc_res_flag.py
sudo mv hc_flag/views/views.xml hc_flag/views/hc_res_flag_views.xml
sudo mv hc_flag/views/templates.xml hc_flag/views/hc_res_flag_templates.xml
