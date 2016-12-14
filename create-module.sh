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
# Go to Ubuntu directory where odoo.py is located. For example:
# cd /odoo/odoo-server
# Place this script in the directory:
# sudo wget https://raw.githubusercontent.com/luigisison/healthcare/master/create-module.sh
# Make the file executable:
# sudo chmod +x create-module.sh
# Execute the script to create the module skeletons:
# ./create-module.sh
################################################################################# 

# ./odoo.py scaffold hc_account addons
# ./odoo.py scaffold hc_allergy_intolerance addons
./odoo.py scaffold hc_appointment addons
./odoo.py scaffold hc_appointment_response addons
./odoo.py scaffold hc_audit_event addons
./odoo.py scaffold hc_basic addons
./odoo.py scaffold hc_binary addons
./odoo.py scaffold hc_body_site addons
./odoo.py scaffold hc_bundle addons
./odoo.py scaffold hc_care_plan addons
./odoo.py scaffold hc_care_team addons
./odoo.py scaffold hc_claim addons
./odoo.py scaffold hc_claim_response addons
# ./odoo.py scaffold hc_clinical_impression addons
./odoo.py scaffold hc_code_system addons
./odoo.py scaffold hc_communication addons
./odoo.py scaffold hc_communication_request addons
./odoo.py scaffold hc_compartment_definition addons
./odoo.py scaffold hc_composition addons
./odoo.py scaffold hc_concept_map addons
# ./odoo.py scaffold hc_condition addons
./odoo.py scaffold hc_conformance addons
./odoo.py scaffold hc_contract addons
./odoo.py scaffold hc_coverage addons
./odoo.py scaffold hc_data_element addons
./odoo.py scaffold hc_decision_support_rule addons
./odoo.py scaffold hc_decision_support_service_module addons
# ./odoo.py scaffold hc_detected_issue addons
./odoo.py scaffold hc_device addons
./odoo.py scaffold hc_device_component addons
./odoo.py scaffold hc_device_metric addons
./odoo.py scaffold hc_device_use_request addons
./odoo.py scaffold hc_device_use_statement addons
./odoo.py scaffold hc_diagnostic_order addons
./odoo.py scaffold hc_diagnostic_report addons
./odoo.py scaffold hc_document_manifest addons
./odoo.py scaffold hc_document_reference addons
./odoo.py scaffold hc_eligibility_request addons
./odoo.py scaffold hc_eligibility_response addons
# ./odoo.py scaffold hc_encounter addons
./odoo.py scaffold hc_enrollment_request addons
./odoo.py scaffold hc_enrollment_response addons
# ./odoo.py scaffold hc_episode_of_care addons
./odoo.py scaffold hc_expansion_profile addons
./odoo.py scaffold hc_explanation_of_benefit addons
# ./odoo.py scaffold hc_family_member_history addons
# ./odoo.py scaffold hc_flag addons
./odoo.py scaffold hc_goal addons
./odoo.py scaffold hc_group addons
./odoo.py scaffold hc_guidance_response addons
./odoo.py scaffold hc_healthcare_service addons
./odoo.py scaffold hc_imaging_excerpt addons
./odoo.py scaffold hc_imaging_object_selection addons
./odoo.py scaffold hc_imaging_study addons
./odoo.py scaffold hc_immunization addons
./odoo.py scaffold hc_immunization_recommendation addons
./odoo.py scaffold hc_implementation_guide addons
./odoo.py scaffold hc_library addons
./odoo.py scaffold hc_linkage addons
./odoo.py scaffold hc_list addons
./odoo.py scaffold hc_location addons
./odoo.py scaffold hc_measure addons
./odoo.py scaffold hc_measure_report addons
./odoo.py scaffold hc_media addons
./odoo.py scaffold hc_medication addons
./odoo.py scaffold hc_medication_administration addons
./odoo.py scaffold hc_medication_dispense addons
./odoo.py scaffold hc_medication_order addons
./odoo.py scaffold hc_medication_statement addons
./odoo.py scaffold hc_message_header addons
./odoo.py scaffold hc_module_definition addons
./odoo.py scaffold hc_naming_system addons
./odoo.py scaffold hc_nutrition_order addons
./odoo.py scaffold hc_observation addons
./odoo.py scaffold hc_operation_definition addons
./odoo.py scaffold hc_operation_outcome addons
./odoo.py scaffold hc_order addons
./odoo.py scaffold hc_order_response addons
./odoo.py scaffold hc_order_set addons
# ./odoo.py scaffold hc_organization addons
./odoo.py scaffold hc_parameters addons
# ./odoo.py scaffold hc_patient addons
./odoo.py scaffold hc_payment_notice addons
./odoo.py scaffold hc_payment_reconciliation addons
# ./odoo.py scaffold hc_person addons
# ./odoo.py scaffold hc_practitioner addons
./odoo.py scaffold hc_practitioner_role addons
# ./odoo.py scaffold hc_procedure addons
./odoo.py scaffold hc_procedure_request addons
./odoo.py scaffold hc_process_request addons
./odoo.py scaffold hc_process_response addons
./odoo.py scaffold hc_protocol addons
./odoo.py scaffold hc_provenance addons
./odoo.py scaffold hc_questionnaire addons
./odoo.py scaffold hc_questionnaire_response addons
./odoo.py scaffold hc_request addons
# ./odoo.py scaffold hc_related_person addons
./odoo.py scaffold hc_risk_assessment addons
./odoo.py scaffold hc_schedule addons
./odoo.py scaffold hc_search_parameter addons
./odoo.py scaffold hc_sequence addons
./odoo.py scaffold hc_slot addons
./odoo.py scaffold hc_sequence addons
./odoo.py scaffold hc_specimen addons
./odoo.py scaffold hc_structure_definition addons
./odoo.py scaffold hc_structure_map addons
./odoo.py scaffold hc_subscription addons
# ./odoo.py scaffold hc_substance addons
./odoo.py scaffold hc_supply_delivery addons
./odoo.py scaffold hc_supply_request addons
./odoo.py scaffold hc_task addons
./odoo.py scaffold hc_test_script addons
# ./odoo.py scaffold hc_value_set addons
./odoo.py scaffold hc_vision_prescription addons

cd addons
# sudo mv hc_account /odoo/odoo-fhir/addons/hc_account
# sudo mv hc_allergy_intolerance /odoo/odoo-fhir/addons/hc_allergy_intolerance
sudo mv hc_appointment /odoo/odoo-fhir/addons/hc_appointment
sudo mv hc_appointment_response /odoo/odoo-fhir/addons/hc_appointment_response
sudo mv hc_audit_event /odoo/odoo-fhir/addons/hc_audit_event
sudo mv hc_basic /odoo/odoo-fhir/addons/hc_basic
sudo mv hc_binary /odoo/odoo-fhir/addons/hc_binary
sudo mv hc_body_site /odoo/odoo-fhir/addons/hc_body_site
sudo mv hc_bundle /odoo/odoo-fhir/addons/hc_bundle
sudo mv hc_care_plan /odoo/odoo-fhir/addons/hc_care_plan
sudo mv hc_care_team /odoo/odoo-fhir/addons/hc_care_team
sudo mv hc_claim /odoo/odoo-fhir/addons/hc_claim
sudo mv hc_claim_response /odoo/odoo-fhir/addons/hc_claim_response
# sudo mv hc_clinical_impression /odoo/odoo-fhir/addons/hc_clinical_impression
sudo mv hc_code_system /odoo/odoo-fhir/addons/hc_code_system
sudo mv hc_communication /odoo/odoo-fhir/addons/hc_communication
sudo mv hc_communication_request /odoo/odoo-fhir/addons/hc_communication_request
sudo mv hc_compartment_definition /odoo/odoo-fhir/addons/hc_compartment_definition
sudo mv hc_composition /odoo/odoo-fhir/addons/hc_composition
sudo mv hc_concept_map /odoo/odoo-fhir/addons/hc_concept_map
# sudo mv hc_condition /odoo/odoo-fhir/addons/hc_condition
sudo mv hc_conformance /odoo/odoo-fhir/addons/hc_conformance
sudo mv hc_contract /odoo/odoo-fhir/addons/hc_contract
sudo mv hc_coverage /odoo/odoo-fhir/addons/hc_coverage
sudo mv hc_data_element /odoo/odoo-fhir/addons/hc_data_element
sudo mv hc_decision_support_rule /odoo/odoo-fhir/addons/hc_decision_support_rule
sudo mv hc_decision_support_service_module /odoo/odoo-fhir/addons/hc_decision_support_service_module
# sudo mv hc_detected_issue /odoo/odoo-fhir/addons/hc_detected_issue
sudo mv hc_device /odoo/odoo-fhir/addons/hc_device
sudo mv hc_device_component /odoo/odoo-fhir/addons/hc_device_component
sudo mv hc_device_metric /odoo/odoo-fhir/addons/hc_device_metric
sudo mv hc_device_use_request /odoo/odoo-fhir/addons/hc_device_use_request
sudo mv hc_device_use_statement /odoo/odoo-fhir/addons/hc_device_use_statement
sudo mv hc_diagnostic_order /odoo/odoo-fhir/addons/hc_diagnostic_order
sudo mv hc_diagnostic_report /odoo/odoo-fhir/addons/hc_diagnostic_report
sudo mv hc_document_manifest /odoo/odoo-fhir/addons/hc_document_manifest
sudo mv hc_document_reference /odoo/odoo-fhir/addons/hc_document_reference
sudo mv hc_eligibility_request /odoo/odoo-fhir/addons/hc_eligibility_request
sudo mv hc_eligibility_response /odoo/odoo-fhir/addons/hc_eligibility_response
# sudo mv hc_encounter /odoo/odoo-fhir/addons/hc_encounter
sudo mv hc_enrollment_request /odoo/odoo-fhir/addons/hc_enrollment_request
sudo mv hc_enrollment_response /odoo/odoo-fhir/addons/hc_enrollment_response
# sudo mv hc_episode_of_care /odoo/odoo-fhir/addons/hc_episode_of_care
sudo mv hc_expansion_profile /odoo/odoo-fhir/addons/hc_expansion_profile
sudo mv hc_explanation_of_benefit /odoo/odoo-fhir/addons/hc_explanation_of_benefit
# sudo mv hc_family_member_history /odoo/odoo-fhir/addons/hc_family_member_history
# sudo mv hc_flag /odoo/odoo-fhir/addons/hc_flag
sudo mv hc_goal /odoo/odoo-fhir/addons/hc_goal
sudo mv hc_group /odoo/odoo-fhir/addons/hc_group
sudo mv hc_guidance_response /odoo/odoo-fhir/addons/hc_guidance_response
sudo mv hc_healthcare_service /odoo/odoo-fhir/addons/hc_healthcare_service
sudo mv hc_imaging_excerpt /odoo/odoo-fhir/addons/hc_imaging_excerpt
sudo mv hc_imaging_object_selection /odoo/odoo-fhir/addons/hc_imaging_object_selection
sudo mv hc_imaging_study /odoo/odoo-fhir/addons/hc_imaging_study
sudo mv hc_immunization /odoo/odoo-fhir/addons/hc_immunization
sudo mv hc_immunization_recommendation /odoo/odoo-fhir/addons/hc_immunization_recommendation
sudo mv hc_implementation_guide /odoo/odoo-fhir/addons/hc_implementation_guide
sudo mv hc_library /odoo/odoo-fhir/addons/hc_library
sudo mv hc_linkage /odoo/odoo-fhir/addons/hc_linkage
sudo mv hc_list /odoo/odoo-fhir/addons/hc_list
sudo mv hc_location /odoo/odoo-fhir/addons/hc_location
sudo mv hc_measure /odoo/odoo-fhir/addons/hc_measure
sudo mv hc_measure_report /odoo/odoo-fhir/addons/hc_measure_report
sudo mv hc_media /odoo/odoo-fhir/addons/hc_media
sudo mv hc_medication /odoo/odoo-fhir/addons/hc_medication
sudo mv hc_medication_administration /odoo/odoo-fhir/addons/hc_medication_administration
sudo mv hc_medication_dispense /odoo/odoo-fhir/addons/hc_medication_dispense
sudo mv hc_medication_order /odoo/odoo-fhir/addons/hc_medication_order
sudo mv hc_medication_statement /odoo/odoo-fhir/addons/hc_medication_statement
sudo mv hc_message_header /odoo/odoo-fhir/addons/hc_message_header
sudo mv hc_module_definition /odoo/odoo-fhir/addons/hc_module_definition
sudo mv hc_naming_system /odoo/odoo-fhir/addons/hc_naming_system
sudo mv hc_nutrition_order /odoo/odoo-fhir/addons/hc_nutrition_order
sudo mv hc_observation /odoo/odoo-fhir/addons/hc_observation
sudo mv hc_operation_definition /odoo/odoo-fhir/addons/hc_operation_definition
sudo mv hc_operation_outcome /odoo/odoo-fhir/addons/hc_operation_outcome
sudo mv hc_order /odoo/odoo-fhir/addons/hc_order
sudo mv hc_order_response /odoo/odoo-fhir/addons/hc_order_response
sudo mv hc_order_set /odoo/odoo-fhir/addons/hc_order_set
# sudo mv hc_organization /odoo/odoo-fhir/addons/hc_organization
sudo mv hc_parameters /odoo/odoo-fhir/addons/hc_parameters
# sudo mv hc_patient /odoo/odoo-fhir/addons/hc_patient
sudo mv hc_payment_notice /odoo/odoo-fhir/addons/hc_payment_notice
sudo mv hc_payment_reconciliation /odoo/odoo-fhir/addons/hc_payment_reconciliation
# sudo mv hc_person /odoo/odoo-fhir/addons/hc_person
# sudo mv hc_practitioner /odoo/odoo-fhir/addons/hc_practitioner
sudo mv hc_practitioner_role /odoo/odoo-fhir/addons/hc_practitioner_role
# sudo mv hc_procedure /odoo/odoo-fhir/addons/hc_procedure
sudo mv hc_procedure_request /odoo/odoo-fhir/addons/hc_procedure_request
sudo mv hc_process_request /odoo/odoo-fhir/addons/hc_process_request
sudo mv hc_process_response /odoo/odoo-fhir/addons/hc_process_response
sudo mv hc_protocol /odoo/odoo-fhir/addons/hc_protocol
sudo mv hc_provenance /odoo/odoo-fhir/addons/hc_provenance
sudo mv hc_questionnaire /odoo/odoo-fhir/addons/hc_questionnaire
sudo mv hc_questionnaire_response /odoo/odoo-fhir/addons/hc_questionnaire_response
sudo mv hc_request /odoo/odoo-fhir/addons/hc_request
# sudo mv hc_related_person /odoo/odoo-fhir/addons/hc_related_person
sudo mv hc_risk_assessment /odoo/odoo-fhir/addons/hc_risk_assessment
sudo mv hc_schedule /odoo/odoo-fhir/addons/hc_schedule
sudo mv hc_search_parameter /odoo/odoo-fhir/addons/hc_search_parameter
sudo mv hc_sequence /odoo/odoo-fhir/addons/hc_sequence
sudo mv hc_slot /odoo/odoo-fhir/addons/hc_slot
sudo mv hc_sequence /odoo/odoo-fhir/addons/hc_sequence
sudo mv hc_specimen /odoo/odoo-fhir/addons/hc_specimen
sudo mv hc_structure_definition /odoo/odoo-fhir/addons/hc_structure_definition
sudo mv hc_structure_map /odoo/odoo-fhir/addons/hc_structure_map
sudo mv hc_subscription /odoo/odoo-fhir/addons/hc_subscription
# sudo mv hc_substance /odoo/odoo-fhir/addons/hc_substance
sudo mv hc_supply_delivery /odoo/odoo-fhir/addons/hc_supply_delivery
sudo mv hc_supply_request /odoo/odoo-fhir/addons/hc_supply_request
sudo mv hc_task /odoo/odoo-fhir/addons/hc_task
sudo mv hc_test_script /odoo/odoo-fhir/addons/hc_test_script
# sudo mv hc_value_set /odoo/odoo-fhir/addons/hc_value_set
sudo mv hc_vision_prescription /odoo/odoo-fhir/addons/hc_vision_prescription

# cd /odoo/odoo-fhir/addons/hc_concept_map
# sudo mv models/models.py models/hc_res_concept_map.py
# sudo mv views/views.xml views/hc_res_concept_map_views.xml
# sudo mv views/templates.xml views/hc_res_concept_map_templates.xml


echo "-----------------------------------------------------------"
echo "Done! The module directories have been created."
echo "-----------------------------------------------------------"
