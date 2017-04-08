# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Procedure(models.Model):  
    _name = "hc.res.procedure"  
    _description = "Procedure"          

    name = fields.Char(
        string="Name", 
        required="True", 
        help="Text representation of the procedure event. Subject Name + Code + Performed Date/Period.")                   
    identifier_ids = fields.One2many(
        comodel_name="hc.procedure.identifier", 
        inverse_name="procedure_id", 
        string="Identifiers", 
        help="External Ids for this procedure.")                                      
    status = fields.Selection(
        string="Status", 
        required="True", 
        selection=[
            ("in-progress", "In-Progress"), 
            ("aborted", "Aborted"), 
            ("completed", "Completed"), 
            ("entered-in-error", "Entered-In-Error")], 
        help="State of the procedure.")                 
    category_id = fields.Many2one(
        comodel_name="hc.vs.procedure.category", 
        string="Category", 
        help="Classification of the procedure.")                  
    code_id = fields.Many2one(
        comodel_name="hc.vs.procedure.code", 
        string="Code", 
        required="True", 
        help="Identification of the procedure.")                 
    subject_type = fields.Selection(
        string="Subject Type",
        required="True",  
        selection=[
            ("patient", "Patient"), 
            ("group", "Group")], 
        help="Type of subject the procedure was performed on.")                    
    subject_name = fields.Char(
        string="Subject",
        required="True", 
        compute="_compute_subject_name",
        store="True",  
        help="Who the procedure was performed on.")
    subject_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Subject Patient",  
        help="Patient who the procedure was performed on.")                  
    subject_group_id = fields.Many2one(
        comodel_name="hc.res.group", 
        string="Subject Group", 
        help="Group who the procedure was performed on.")
    encounter_id = fields.Many2one(
        comodel_name="hc.res.encounter", 
        string="Encounter",
        help="The encounter associated with the procedure.")
    performed_date_type = fields.Selection(
        string="Performed Date Type", 
        selection=[
            ("date_time", "Datetime"),  
            ("period", "Period")], 
        help="Date/Period the procedure was performed.")
    performed_date_name = fields.Char(
        string="Performed Date/Period",
        compute="_compute_performed_date_name",
        store="True",  
        help="Who the procedure was performed on.")                 
    performed_datetime = fields.Datetime(
        string="Performed Datetime", 
        help="Date the procedure was performed.")                 
    performed_start_date = fields.Datetime(
        string="Performed Start Date", 
        help="Start of the period when the procedure was performed.")                    
    performed_end_date = fields.Datetime(
        string="Performed End Date", 
        help="End of the period when the procedure was performed.")        
    location_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Location", 
        help="Where the procedure happened.") 
    reason_reference_ids = fields.One2many(
        comodel_name="hc.procedure.reason.reference", 
        inverse_name="procedure_id", 
        string="Reason References", 
        help="Condition that is the reason the procedure performed.")                 
    reason_code_id = fields.Many2one(
        comodel_name="hc.vs.procedure.reason", 
        string="Reason Code", 
        help="Coded reason procedure performed.")
    is_not_performed = fields.Boolean(
        string="Not Performed", 
        help="True if procedure was not performed as scheduled.")                    
    reason_not_peformed_ids = fields.Many2many(
        comodel_name="hc.vs.procedure.not.performed.reason", 
        string="Reasons Not Peformed", 
        help="Reason procedure was not performed.")                   
    body_site_ids = fields.Many2many(
        comodel_name="hc.vs.body.site", 
        string="Body Sites", 
        help="Target body sites.")                                    
    outcome_id = fields.Many2one(
        comodel_name="hc.vs.procedure.outcome", 
        string="Outcome", 
        help="The result of procedure")                  
    report_ids = fields.One2many(
        comodel_name="hc.procedure.report", 
        inverse_name="procedure_id", 
        string="Reports", 
        help="Any report resulting from the procedure.")                 
    complication_ids = fields.Many2many(
        comodel_name="hc.vs.condition.code", 
        string="Complications", 
        help="Complication following the procedure.")                  
    follow_up_ids = fields.Many2many(
        comodel_name="hc.vs.procedure.follow.up", 
        string="Follow Ups", 
        help="Instructions for follow up.")                 
    request_type = fields.Selection(
        string="Request Type", 
        selection=[
            # ("care_plan", "Care Plan"), 
            ("diagnostic_request", "Diagnostic Request"),
            ("procedure_request", "Procedure Request"),
            # ("referral_request", "Referral Request")
            ], 
        help="Type of request for this procedure.")                  
    request_name = fields.Char(
        string="Request", 
        compute="_compute_request_name",
        store="True",  
        help="Request reference for this procedure.")                    
    # request_care_plan_id = fields.Many2one(
    #     comodel_name="hc.res.care.plan", 
    #     string="Request Care Plan", 
    #     help="Care Plan request for this procedure.")                   
    request_diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Request Diagnostic Request", 
        help="Diagnostic Request for this procedure.")                   
    request_procedure_request_id = fields.Many2one(
        comodel_name="hc.res.procedure.request", 
        string="Request Procedure Request", 
        help="Procedure Request for this procedure.")                   
    # request_referral_request_id = fields.Many2one(
    #     comodel_name="hc.res.referral.request", 
    #     string="Request Referral Request", 
    #     help="Referral Request for this procedure.")                  
    notes_ids = fields.One2many(
        comodel_name="hc.procedure.note", 
        inverse_name="procedure_id", 
        string="Notes", 
        help="Additional information about the procedure.")                    
    used_reference_ids = fields.One2many(
        comodel_name="hc.procedure.used.reference", 
        inverse_name="procedure_id", 
        string="Used References", 
        help="Device used during procedure.")                   
    used_code_ids = fields.Many2many(
        comodel_name="hc.vs.procedure.used.code", 
        string="Used Codes", 
        help="Coded items used during the procedure.")                  
    component_ids = fields.One2many(
        comodel_name="hc.procedure.component", 
        inverse_name="procedure_id", 
        string="Components", 
        help="Events related to the procedure.")                                   
    performer_ids = fields.One2many(
        comodel_name="hc.procedure.performer", 
        inverse_name="procedure_id", 
        string="Performers", 
        help="The people who performed the procedure.")                    
    focal_device_ids = fields.One2many(
        comodel_name="hc.procedure.focal.device", 
        inverse_name="procedure_id", 
        string="Focal Devices", 
        help="Device changed in procedure.")

    @api.depends('subject_type')         
    def _compute_subject_name(self):         
        for hc_res_procedure in self:       
            if hc_res_procedure.subject_type == 'patient':  
                hc_res_procedure.subject_name = hc_res_procedure.subject_patient_id.name
            elif hc_res_procedure.subject_type == 'group':  
                hc_res_procedure.subject_name = hc_res_procedure.subject_group_id.name

    @api.depends('performed_date_type')         
    def _compute_performed_date_name(self):         
        for hc_res_procedure in self:       
            if hc_res_procedure.performed_date_type == 'date_time': 
                hc_res_procedure.performed_date_name = hc_res_procedure.performed_date_date_time_id.name
            elif hc_res_procedure.performed_date_type == 'period':  
                hc_res_procedure.performed_date_name = 'Between' + str(hc_res_procedure.performed_start_date) + ' and ' + str(hc_res_procedure.performed_end_date)

    @api.depends('request_type')
    def _compute_request_name(self):
        for hc_res_procedure in self:
            if hc_res_procedure.request_type == 'care_plan':
                hc_res_procedure.request_name = hc_res_procedure.request_care_plan_id.name
            elif hc_res_procedure.request_type == 'diagnostic_request':
                hc_res_procedure.request_name = hc_res_procedure.request_diagnostic_request_id.name
            elif hc_res_procedure.request_type == 'procedure_request':
                hc_res_procedure.request_name = hc_res_procedure.request_procedure_request_id.name
            elif hc_res_procedure.request_type == 'referral_request':
                hc_res_procedure.request_name = hc_res_procedure.request_referral_request_id.name

class ProcedureUsedReference(models.Model): 
    _name = "hc.procedure.used.reference"   
    _description = "Procedure Used Reference"
    _inherit = ["hc.basic.association"]           
    
    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this procedure used reference.")                   
    used_reference_type = fields.Selection(
        string="Used Reference Type", 
        selection=[
            ("device", "Device"), 
            ("medication", "Medication"), 
            ("substance", "Substance")], 
        help="Type of item used during the procedure")                 
    used_reference_name = fields.Char(
        string="Used Reference", 
        compute="_compute_used_reference_name",
        store="True",  
        help="The name of the item used during the procedure.")                   
    used_reference_device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Used Reference Device", 
        help="Device item used during procedure.")                    
    used_reference_medication_id = fields.Many2one(
        comodel_name="hc.res.medication", 
        string="Used Reference Medication", 
        help="Medication item used during procedure.")                 
    used_reference_substance_id = fields.Many2one(
        comodel_name="hc.res.substance", 
        string="Used Reference Substance", 
        help="Substance item used during procedure.")

    @api.depends('used_reference_type')          
    def _compute_used_reference_name(self):          
        for hc_procedure_used_reference in self:        
            if hc_procedure_used_reference.used_reference_type == 'device': 
                hc_procedure_used_reference.used_reference_name = hc_procedure_used_reference.used_reference_device_id.name
            elif hc_procedure_used_reference.used_reference_type == 'medication':   
                hc_procedure_used_reference.used_reference_name = hc_procedure_used_reference.used_reference_medication_id.name
            elif hc_procedure_used_reference.used_reference_type == 'substance':    
                hc_procedure_used_reference.used_reference_name = hc_procedure_used_reference.used_reference_substance_id.name           

class ProcedureComponent(models.Model): 
    _name = "hc.procedure.component"    
    _description = "Procedure Component"        
    _inherit = ["hc.basic.association"]

    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this procedure component.")             
    component_type = fields.Selection(
        string="Component Type", 
        selection=[
            ("medication_administration", "Medication Administration"), 
            ("procedure", "Procedure"), 
            ("observation", "Observation")], 
        help="Type of events related to the procedure.")             
    component_name = fields.Char(
        string="Component", 
        compute="_compute_component_name", 
        store="True", 
        help="Event related to the procedure.")               
    component_medication_administration_id = fields.Many2one(
        comodel_name="hc.res.medication.administration", 
        string="Component Medication Administration", 
        help="Medication Administration event related to the procedure.")              
    component_procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Component Procedure", 
        help="Procedure event related to the procedure.")              
    component_observation_id = fields.Many2one(
        comodel_name="hc.res.observation", 
        string="Component Observation", 
        help="Observation event related to the procedure.")              

    @api.depends('component_type')          
    def _compute_component_name(self):           
        for hc_procedure_component in self:     
            if hc_procedure_component.component_type == 'procedure':  
                hc_procedure_component.component_name = hc_procedure_component.component_procedure_id.name
            elif hc_procedure_component.component_type == 'observation':    
                hc_procedure_component.component_name = hc_procedure_component.component_observation_id.name
            elif hc_procedure_component.component_type == 'medication_administration':    
                hc_procedure_component.component_name = hc_procedure_component.component_medication_administration_id.name
            
class ProcedurePerformer(models.Model): 
    _name = "hc.procedure.performer"    
    _description = "Procedure Performer"            
    
    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this performer.")
    actor_type = fields.Selection(
        string="Performer Actor Type", 
        selection=[
            ("practitioner", "Practitioner"), 
            ("organization", "Organization"),
            ("patient", "Patient"),
            ("related_person", "Related Person")], 
        help="Type of practitioner who was involved in the procedure.") 
    actor_name = fields.Char(
        string="Actor", 
        compute="_compute_actor_name",
        help="The name of the entity who performs the procedure.")                                   
    actor_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Actor Practitioner", 
        help="The practitioner who was involved in the procedure.")                    
    actor_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Actor Organization", 
        help="The reference to the organization.")                 
    actor_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Actor Patient", 
        help="The reference to the patient.")                 
    actor_related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Actor Related Person", 
        help="The reference to the related person.")                 
    role_id = fields.Many2one(
        comodel_name="hc.vs.performer.role", 
        string="Role", 
        help="The The role the actor was in.")                   

    @api.depends('actor_type')          
    def _compute_actor_name(self):           
        for hc_procedure_performer in self:     
            if hc_procedure_performer.actor_type == 'practitioner': 
                hc_procedure_performer.actor_name = hc_procedure_performer.actor_practitioner_id.name
            elif hc_procedure_performer.actor_type == 'organization':   
                hc_procedure_performer.actor_name = hc_procedure_performer.actor_organization_id.name
            elif hc_procedure_performer.actor_type == 'patient':    
                hc_procedure_performer.actor_name = hc_procedure_performer.actor_patient_id.name
            elif hc_procedure_performer.actor_type == 'related_person': 
                hc_procedure_performer.actor_name = hc_procedure_performer.actor_related_person_id.name

class ProcedureFocalDevice(models.Model):   
    _name = "hc.procedure.focal.device" 
    _description = "Procedure Focal Device"         
    
    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this focal device.")                   
    action_id = fields.Many2one(
        comodel_name="hc.vs.device.action", 
        string="Action", 
        help="Kind of change to device.")                  
    manipulated_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Manipulated", 
        required="True", 
        help="Device that was changed.")                  

class ProcedureReport(models.Model):  
    _name = "hc.procedure.report"    
    _description = "Procedure Report"        
    _inherit = ["hc.basic.association"] 
    
    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this Procedure Report.")                   
    # report_id = fields.Many2one(
    #     comodel_name="hc.res.diagnostic.report", 
    #     string="Report", 
    #     help="Report associated with this Procedure Report.")
                 

class ProcedureIdentifier(models.Model):    
    _name = "hc.procedure.identifier"   
    _description = "Procedure Identifier"       
    _inherit = ["hc.basic.association", "hc.identifier"]    
    
    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this Procedure Identifier.")                                                  

class ProcedureReasonReference(models.Model):   
    _name = "hc.procedure.reason.reference" 
    _description = "Procedure Reason Reference"     
    _inherit = ["hc.basic.association"] 
    
    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this Procedure Reason Reference.")                   
    condition_id = fields.Many2one(
        comodel_name="hc.res.condition", 
        string="Condition", 
        help="Condition associated with this Procedure Reason Reference.")                   

class ProcedureNote(models.Model): 
    _name = "hc.procedure.note"    
    _description = "Procedure Note"        
    _inherit = ["hc.basic.association", "hc.annotation"]    

    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this Procedure Note.")                    

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

class ProcedureUsedCode(models.Model):  
    _name = "hc.vs.procedure.used.code" 
    _description = "Procedure Used Code"        
    _inherit = ["hc.value.set.contains"]    

class PerformerRole(models.Model):  
    _name = "hc.vs.performer.role"  
    _description = "Performer Role"     
    _inherit = ["hc.value.set.contains"]    

class DeviceAction(models.Model):   
    _name = "hc.vs.device.action"   
    _description = "Device Action"      
    _inherit = ["hc.value.set.contains"]    

# External Reference

class EncounterIndication(models.Model):    
    _inherit = "hc.encounter.indication"
    
    indication_procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Indication Procedure", 
        help="Procedure reason the encounter takes place (resource).")

class AppointmentIndication(models.Model):  
    _inherit = "hc.appointment.indication" 
                                   
    # indication_type = fields.Selection(
    #     string="Indication Type", 
    #     selection=[
    #         ("condition", "Condition"), 
    #         ("procedure", "Procedure")], 
    #     help="Type of reason the appointment is to take place (resource).")                   
    # indication_name = fields.Char(
    #     string="Indication", 
    #     compute="_compute_indication_name", 
    #     store="True", 
    #     help="Reason the appointment is to take place (resource).")                                     
    indication_condition_id = fields.Many2one(
        comodel_name="hc.res.condition", 
        string="Indication Condition", 
        help="Condition reason the appointment is to take place (resource).")  
    indication_procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Indication Procedure", 
        help="Procedure reason the appointment is to take place (resource).")

    @api.depends('indication_type')         
    def _compute_indication_name(self):         
        for hc_res_appointment in self:     
            if hc_res_appointment.indication_type == 'condition':   
                hc_res_appointment.indication_name = hc_res_appointment.indication_condition_id.name
            elif hc_res_appointment.indication_type == 'procedure': 
                hc_res_appointment.indication_name = hc_res_appointment.indication_procedure_id.name
 
