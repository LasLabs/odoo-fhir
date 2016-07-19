# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Procedure(models.Model):	
    _name = "hc.res.procedure"	
    _description = "Procedure"

    name = fields.Char(string="Name", required="True", help="The patient's procedure described.")		
    identifier_ids = fields.One2many(comodel_name="hc.procedure.identifier", inverse_name="procedure_id", string="Identifiers", help="External Ids for this procedure.")		
    subject_type = fields.Selection(string="Procedure Subject Type", selection=[("patient", "Patient"), ("group", "Group")], help="Type of subject the procedure was performed on.")		
    subject_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Subject Patient", required="True", help="Patient who the procedure was performed on.")		
    subject_group_id = fields.Many2one(comodel_name="hc.res.group", string="Subject Group", required="True", help="Group who the procedure was performed on.")		
    status = fields.Selection(string="Procedure Status", required="True", selection=[("in-progress", "In-Progress"), ("aborted", "Aborted"), ("completed", "Completed"), ("entered-in-error", "Entered-In-Error")], help="State of the procedure.")		
    category_id = fields.Many2one(comodel_name="hc.vs.procedure.category", string="Category", help="Classification of the procedure.")		
    code_id = fields.Many2one(comodel_name="hc.vs.procedure.code", string="Code", required="True", help="Identification of the procedure.")		
    not_performed_id = fields.Many2one(comodel_name="hc.vs.procedure.not.performed", string="Not Performed", help="if procedure was not performed as scheduled.")		
    reason_not_peformed_ids = fields.One2many(comodel_name="hc.vs.procedure.not.performed.reason", inverse_name="procedure_id", string="Reason Not Peformed", help="Reason procedure was not performed.")		
    body_site_ids = fields.One2many(comodel_name="hc.vs.body.site", inverse_name="procedure_id", string="Body Site", help="Target body sites.")		
    reason_type = fields.Selection(string="Procedure Reason Type", selection=[("code", "Code"), ("condition", "Condition")], help="Type of reason the procedure was performed.")		
    reason_code_id = fields.Many2one(comodel_name="hc.vs.procedure.reason", string="Reason Code", help="Reason procedure performed.")		
    reason_condition_id = fields.Many2one(comodel_name="hc.res.condition", string="Reason Condition", help="The reference to the condition.")		
    performed = fields.Datetime(string="Performed Date", help="Date/Period the procedure was performed.")		
    start_date = fields.Datetime(string="Start Date", help="Start of the date/period the procedure was performed.")		
    encounter_id = fields.Many2one(comodel_name="hc.res.encounter", string="Encounter", help="The encounter associated with the procedure.")		
    location_id = fields.Many2one(comodel_name="hc.res.location", string="Location", help="Where the procedure happened.")		
    outcome_id = fields.Many2one(comodel_name="hc.vs.procedure.outcome", string="Outcome", help="The result of procedure")		
    report_diagnostic_report_ids = fields.One2many(comodel_name="hc.procedure.diagnostic.report", inverse_name="procedure_id", string="Report Diagnostic Reports", help="Any report resulting from the procedure.")		
    complication_ids = fields.One2many(comodel_name="hc.vs.condition.code", inverse_name="procedure_id", string="Complications", help="Complication following the procedure.")		
    follow_up_ids = fields.One2many(comodel_name="hc.vs.procedure.followup", inverse_name="procedure_id", string="Follow Ups", help="Instructions for follow up.")		
    request_type = fields.Selection(string="Procedure Request Type", selection=[("care plan", "Care Plan"), ("diagnostic order", "Diagnostic Order"),("procedure request", "Procedure Request"),("referral request", "Referral Request")], help="Type of request for this procedure.")		
    request_care_plan_id = fields.Many2one(comodel_name="hc.res.care.plan", string="Request Care Plan", help="CarePlan request for this procedure.")		
    request_diagnostic_order_id = fields.Many2one(comodel_name="hc.res.diagnostic.order", string="Request Diagnostic Order", help="DiagnosticOrder request for this procedure.")		
    request_procedure_request_id = fields.Many2one(comodel_name="hc.res.procedure.request", string="Request Procedure Request", help="ProcedureRequest request for this procedure.")		
    request_referral_request_id = fields.Many2one(comodel_name="hc.res.referral.request", string="Request Referral Request", help="ReferralRequest request for this procedure.")		
    notes_ids = fields.One2many(comodel_name="hc.procedure.notes", inverse_name="procedure_id", string="Notess", help="Additional information about the procedure.")		
    used_item_ids = fields.One2many(comodel_name="hc.procedure.used.item", inverse_name="procedure_id", string="Used Items", help="Items used during procedure.")		
    		
    performer_ids = fields.One2many(comodel_name="hc.procedure.performer", inverse_name="procedure_id", string="Performers", help="The people who performed the procedure.")		
    focal_device_ids = fields.One2many(comodel_name="hc.procedure.focal.device", inverse_name="procedure_id", string="Focal Devices", help="Device changed in procedure.")
    related_item_ids = fields.One2many(comodel_name="hc.procedure.related.item", inverse_name="procedure_id", string="Related Items", help="A procedure that is related to this one.")


class ProcedureBodySite(models.Model):  
    _name = "hc.procedure.body.site"    
    _description = "Procedure Body Site"         

    procedure_id = fields.Many2one(comodel_name="hc.res.procedure", string="Procedure", help="Procedure performed on this body site.")                  
    body_site_id = fields.Many2one(comodel_name="hc.vs.body.site", string="Body Site", help="Body site where this procedure is performed.") 

class BodySite(models.Model):   
    _name = "hc.vs.body.site"   
    _description = "Body Site"      
    _inherit = ["hc.value.set.contains"]  

class ProcedureRelatedItem(models.Model):   
    _name = "hc.procedure.related item" 
    _description = "Procedure Related Item"

    procedure_id = fields.Many2one(comodel_name="hc.res.procedure", string="Procedure", required="True", help="Procedure associated with this related item.")       
    type = fields.Selection(string="Related Item Type", selection=[("caused-by", "Caused-By"), ("because-of", "Because-Of")], help="Type of related item.")     
    target_type = fields.Selection(string="Related Item Target Type", selection=[("allergy intolerance", "Allergy Intolerance"), ("care plan", "Care Plan"),("condition", "Condition"),("diagnostic report", "Diagnostic Report"),("family member history", "Family Member History"),("imaging study", "Imaging Study"),("immunization", "Immunization"), ("immunization recommendation", "Immunization Recommendation"),("medication administration", "Medication Administration"),("medication dispense", "Medication Dispense"),("medication prescription", "Medication Prescription"),("medication statement", "Medication Statement"),("observation", "Observation"),("procedure", "Procedure")], help="Type of related item.")        
    target_allergy_intolerance_id = fields.Many2one(comodel_name="hc.res.allergy.intolerance", string="Target Allergy Intolerance", help="Allergy Intolerance related item - e.g. a procedure.")       
    # target_care_plan_id = fields.Many2one(comodel_name="hc.res.care.plan", string="Target Care Plan", help="Care Plan related item - e.g. a procedure.")     
    # target_condition_id = fields.Many2one(comodel_name="hc.res.condition", string="Target Condition", help="Condition related item - e.g. a procedure.")        
    # target_diagnostic_report_id = fields.Many2one(comodel_name="hc.res.diagnostic.report", string="Target Diagnostic Report", help="Diagnostic Report related item - e.g. a procedure.")     
    target_family_member_history_id = fields.Many2one(comodel_name="hc.res.family.member.history", string="Target Family Member History", help="Family Member History related item - e.g. a procedure.")      
    # target_imaging_study_id = fields.Many2one(comodel_name="hc.res.imaging.study", string="Target Imaging Study", help="ImagingStudy related item - e.g. a procedure.")     
    # target_immunization_id = fields.Many2one(comodel_name="hc.res.immunization", string="Target Immunization", help="Immunization related item - e.g. a procedure.")        
    # target_immunization_recommendation_id = fields.Many2one(comodel_name="hc.res.immunization.recommendation", string="Target Immunization Recommendation", help="Immunization Recommendation related item - e.g. a procedure.")     
    # target_medication_admnistration_id = fields.Many2one(comodel_name="hc.res.medication.administration", string="Target Medication Admnistration", help="Medication Administration related item - e.g. a procedure.")       
    # target_medication_dispense_id = fields.Many2one(comodel_name="hc.res.medication.dispense", string="Target Medication Dispense", help="Medication Dispense related item - e.g. a procedure.")     
    # target_medication_order_id = fields.Many2one(comodel_name="hc.res.medication.order", string="Target Medication Order", help="Medication Order related item - e.g. a procedure.")     
    # target_medication_statement_id = fields.Many2one(comodel_name="hc.res.medication.statement", string="Target Medication Statement", help="Medication Statement related item - e.g. a procedure.")     
    # target_observation_id = fields.Many2one(comodel_name="hc.res.observation", string="Target Observation", help="Observation related item - e.g. a procedure.")        
    target_procedure_id = fields.Many2one(comodel_name="hc.res.procedure", string="Target Procedure", help="Procedure related item - e.g. a procedure.")        

                   

class ProcedureDiagnosticReport(models.Model):  
    _name = "hc.procedure.diagnostic.report"    
    _description = "Procedure Diagnostic Report"        
    _inherit = ["hc.basic.association"] 

    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this identifier.")                  

class ProcedureIdentifier(models.Model):    
    _name = "hc.procedure.identifier"   
    _description = "Procedure Identifier"       
    _inherit = ["hc.basic.association", "hc.identifier"]

    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this identifier.")                  

class ProcedureMedication(models.Model):    
    _name = "hc.procedure.medication"   
    _description = "Procedure Medication"       
    _inherit = ["hc.basic.association"] 

    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this identifier.")                  

class ProcedureSubstance(models.Model): 
    _name = "hc.procedure.substance"    
    _description = "Procedure Substance"        
    _inherit = ["hc.basic.association"] 

    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this identifier.")                  

class ProcedureComplication(models.Model):  
    _name = "hc.procedure.complication" 
    _description = "Procedure Complication"     
    _inherit = ["hc.basic.association"] 

    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this identifier.")                  

class ProcedureCode(models.Model):  
    _name = "hc.vs.procedure.code"  
    _description = "Procedure Code"     
    _inherit = ["hc.value.set.contains"]    

class ProcedureNotPerformedReason(models.Model):    
    _name = "hc.vs.procedure.not.performed.reason"  
    _description = "Procedure Not Performed Reason"     
    _inherit = ["hc.value.set.contains"]    

class ProcedureNotPerformed(models.Model):  
    _name = "hc.vs.procedure.not.performed" 
    _description = "Procedure Not Performed"        
    _inherit = ["hc.value.set.contains"]    

  

class ProcedureCategory(models.Model):  
    _name = "hc.vs.procedure.category"  
    _description = "Procedure Category"     
    _inherit = ["hc.value.set.contains"]    

class ProcedureReason(models.Model):    
    _name = "hc.vs.procedure.reason"    
    _description = "Procedure Reason"       
    _inherit = ["hc.value.set.contains"]    

class ProcedureOutcome(models.Model):   
    _name = "hc.vs.procedure.outcome"   
    _description = "Procedure Outcome"      
    _inherit = ["hc.value.set.contains"]    

class ConditionCode(models.Model):  
    _name = "hc.vs.condition.code"  
    _description = "Condition Code"     
    _inherit = ["hc.value.set.contains"]    

class ProcedureFollowUp(models.Model):  
    _name = "hc.vs.procedure.follow.up" 
    _description = "Procedure Follow Up"        
    _inherit = ["hc.value.set.contains"]    

class PerformerRole(models.Model):  
    _name = "hc.vs.performer.role"  
    _description = "Performer Role"     
    _inherit = ["hc.value.set.contains"]    

class DeviceAction(models.Model):   
    _name = "hc.vs.device.action"   
    _description = "Device Action"      
    _inherit = ["hc.value.set.contains"]    

class ProcedureRequest(models.Model):   
    _name = "hc.res.procedure.request"  
    _description = "Procedure Request"          
    
    identifier_ids = fields.One2many(comodel_name="hc.procedure.request.identifier", inverse_name="procedure_request_id", string="Identifiers", help="Identifier.")                 
    subject_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Subject Patient", required="True", help="Subject.")                 
    type_id = fields.Many2one(comodel_name="hc.vs.procedure.request.type", string="Type", required="True", help="Procedure Type.")                  

# class ProcedureRequestBodySite(models.Model):   
#     _name = "hc.procedure.request.body.site"    
#     _description = "Procedure Request Body Site"            

#     site_id = fields.Many2one(comodel_name="hc.vs.procedure.request.body.site.site", string="Site", required="True", help="CodeableConcept target body site.")                  
#     body_site_id = fields.Many2one(comodel_name="hc.res.body.site", string="Body Site", required="True", help="BodySite target body site.")                 
#     indication_ids = fields.One2many(comodel_name="hc.vs.procedure.request.indication", inverse_name="procedure_request_id", string="Indications", help="Indication.")                  
#     timing = fields.Datetime(string="Timing Date", help="dateTime procedure timing schedule.")                  
#     start_date = fields.Datetime(string="Start Date", help="Start of the procedure timing schedule.")                   
#     end_date = fields.Datetime(string="End Date", help="End of the procedure timing schedule.")                 
#     timing_timing_ids = fields.Many2one(comodel_name="hl7.", string="Timing Timings", help="Timing procedure timing schedule.")                 
#     encounter_id = fields.Many2one(comodel_name="hc.res.encounter", string="Encounter", help="Encounter.")                  
#     performer_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Performer Practitioner", help="Practitioner performer.")                    
#     performer_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Performer Organization", help="Organization performer.")                    
#     performer_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Performer Patient", help="Patient performer.")                    
#     performer_related_person_id = fields.Many2one(comodel_name="hc.res.related.person", string="Performer Related Person", help="Related Person performer.")                 
#     status = fields.Selection(string="Procedure Request Status", selection=[("proposed", "Proposed"), ("draft", "Draft"), ("requested", "Requested"), ("received", "Received"), ("accepted", "Accepted"), ("in-progress", "In-Progress"), ("completed", "Completed"), ("suspended", "Suspended"), ("rejected", "Rejected"), ("aborted", "Aborted")], help="0")                  
#     notes_ids = fields.One2many(comodel_name="hc.procedure.request.identifier", inverse_name="procedure_request_id", string="Notes", help="Notes.")                 
#     is_as_needed = fields.Boolean(string="As Needed", help="boolean prn.")                  
#     as_needed_id = fields.Many2one(comodel_name="hc.vs.procedure.request.as.needed", string="As Needed", help="CodeableConcept prn.")                   
#     ordered_on = fields.Datetime(string="Ordered On Date", help="When Requested.")                  
#     orderer_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Orderer Practitioner", help="Practitioner ordering party.")                   
#     orderer_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Orderer Patient", help="Patient ordering party.")                   
#     orderer_related_person_id = fields.Many2one(comodel_name="hc.res.related.person", string="Orderer Related Person", help="Related Person ordering party.")                    
#     orderer_device_id = fields.Many2one(comodel_name="hc.res.device", string="Orderer Device", help="Device ordering party.")                   
#     priority = fields.Selection(string="Procedure Request Priority", selection=[("routine", "Routine"), ("urgent", "Urgent"), ("stat", "Stat"), ("asap", "Asap")], help="0")                    
		
