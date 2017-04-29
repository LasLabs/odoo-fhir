# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Procedure(models.Model):  
    _name = "hc.res.procedure"  
    _description = "Procedure"          

    name = fields.Char(
        string="Event Name", 
        required="True", 
        help="Text representation of the procedure event. Subject Name + Code + Performed Date/Period.")                   
    identifier_ids = fields.One2many(
        comodel_name="hc.procedure.identifier", 
        inverse_name="procedure_id", 
        string="Identifiers", 
        help="External Ids for this procedure.")                                      
    definition_ids = fields.One2many(
        comodel_name="hc.procedure.definition", 
        inverse_name="procedure_id", 
        string="Definitions", 
        help="Instantiates protocol or definition.")
    based_on_ids = fields.One2many(
        comodel_name="hc.procedure.based.on", 
        inverse_name="procedure_id", 
        string="Based Ons", 
        help="A request for this procedure.")
    part_of_ids = fields.One2many(
        comodel_name="hc.procedure.part.of", 
        inverse_name="procedure_id", 
        string="Part Ofs", 
        help="Part of referenced event.")
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
    reason_code_ids = fields.Many2many(
        comodel_name="hc.vs.procedure.reason", 
        relation="procedure_reason_code_rel", 
        string="Reason Codes", 
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
    # Note: Causes UnicodeWarning: Unicode unequal comparison failed
    # complication_detail_ids = fields.One2many(
    #     comodel_name="hc.procedure.complication.detail", 
    #     inverse_name="procedure_id", 
    #     string="Complication Details", 
    #     help="A condition that is a result of the procedure.")
    follow_up_ids = fields.Many2many(
        comodel_name="hc.vs.procedure.follow.up", 
        string="Follow Ups", 
        help="Instructions for follow up.")                                 
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
                hc_res_procedure.performed_date_name = str(hc_res_procedure.performed_datetime)
            elif hc_res_procedure.performed_date_type == 'period':  
                hc_res_procedure.performed_date_name = 'Between' + str(hc_res_procedure.performed_start_date) + ' and ' + str(hc_res_procedure.performed_end_date)
            
class ProcedurePerformer(models.Model): 
    _name = "hc.procedure.performer"    
    _description = "Procedure Performer"            
    
    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this performer.")
    role_id = fields.Many2one(
        comodel_name="hc.vs.performer.role", 
        string="Role", 
        help="The The role the actor was in.")
    actor_type = fields.Selection(
        string="Actor Type", 
        required="True", 
        selection=[
            ("practitioner", "Practitioner"), 
            ("organization", "Organization"), 
            ("patient", "Patient"), 
            ("related_person", "Related Person"), 
            ("device", "Device")], 
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
    actor_device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Actor Device", 
        required="True", 
        help="The reference to the device.")
    on_behalf_of_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="On Behalf Of", 
        help="Organization the device or practitioner was acting for.")   

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
            elif hc_procedure_performer.actor_type == 'device':    
                hc_procedure_performer.actor_name = hc_procedure_performer.actor_device_id.name

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

class ProcedureIdentifier(models.Model):    
    _name = "hc.procedure.identifier"   
    _description = "Procedure Identifier"       
    _inherit = ["hc.basic.association", "hc.identifier"]    
    
    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this Procedure Identifier.")     

class ProcedureDefinition(models.Model):
    _name = "hc.procedure.definition"
    _description = "Procedure Definition"
    _inherit = ["hc.basic.association"]

    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this Procedure Procedure Definition.")                  
    definition_type = fields.Selection(
        string="Definition Type", 
        selection=[
            ("plan_definition", "Plan Definition"), 
            ("activity_definition", "Activity Definition"), 
            ("healthcare_service", "Healthcare Service")], 
        help="Type of instantiates protocol or definition.")
    subject_type = fields.Selection(
        string="Subject Type", 
        selection=[
            ("plan_definition", "Plan Definition"), 
            ("activity_definition", "Activity Definition"), 
            ("healthcare_service", "Healthcare Service")], 
        help="Type of subject the procedure was performed on.")                    
    definition_name = fields.Char(
        string="Definition", 
        compute="_compute_definition_name", 
        store="True", 
        help="Instantiates protocol or definition.")                   
    definition_plan_definition_id = fields.Many2one(
        comodel_name="hc.res.plan.definition", 
        string="Definition Plan Definition", 
        help="Plan Definition instantiates protocol or definition.")                    
    definition_activity_definition_id = fields.Many2one(
        comodel_name="hc.res.activity.definition", 
        string="Definition Activity Definition", 
        help="Activity Definition instantiates protocol or definition.")                    
    definition_healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Definition Healthcare Service", 
        help="Healthcare Service instantiates protocol or definition.")                    

class ProcedureBasedOn(models.Model): 
    _name = "hc.procedure.based.on"
    _description = "Procedure Based On"
    _inherit = ["hc.basic.association"]

    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this Procedure Procedure Based On.")                    
    based_on_type = fields.Selection(
        string="Based On Type", 
        selection=[
            # ("care_plan", "Care Plan"), 
            ("procedure_request", "Procedure Request"), 
            # ("referral_request", "Referral Request")
            ], 
        help="Type of request for this procedure.")                    
    based_on_name = fields.Char(
        string="Based On", 
        compute="_compute_based_on_name", 
        store="True", 
        help="A request for this procedure.")                    
    # based_on_care_plan_id = fields.Many2one(
    #     comodel_name="hc.res.care.plan", 
    #     string="Based On Care Plan", 
    #     help="Care Plan for this procedure.")                   
    based_on_procedure_request_id = fields.Many2one(
        comodel_name="hc.res.procedure.request", 
        string="Based On Procedure Request", 
        help="Procedure Request for this procedure.")                   
    # based_on_referral_request_id = fields.Many2one(
    #     comodel_name="hc.res.referral.request", 
    #     string="Based On Referral Request", 
    #     help="Referral Request for this procedure.")                   

class ProcedurePartOf(models.Model):
    _name = "hc.procedure.part.of"
    _description = "Procedure Part Of"
    _inherit = ["hc.basic.association"]

    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this Procedure Procedure Part Of.")                 
    part_of_type = fields.Selection(
        string="Part Of Type", 
        selection=[
            ("procedure", "Procedure"), 
            ("observation", "Observation"), 
            ("medication_administration", "Medication Administration")], 
        help="Type of part of referenced event.")
    part_of_name = fields.Char(
        string="Part Of", 
        compute="_compute_part_of_name", 
        store="True", 
        help="Part of referenced event.")                   
    part_of_procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Part Of Procedure", 
        help="Procedure of referenced event.")                  
    part_of_observation_id = fields.Many2one(
        comodel_name="hc.res.observation", 
        string="Part Of Observation", 
        help="Observation of referenced event.")                  
    part_of_medication_administration_id = fields.Many2one(
        comodel_name="hc.res.medication.administration", 
        string="Part Of Medication Administration", 
        help="Medication Administration of referenced event.")                  

class ProcedureReasonReference(models.Model):   
    _name = "hc.procedure.reason.reference" 
    _description = "Procedure Reason Reference"     
    _inherit = ["hc.basic.association"] 
    
    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this Procedure Reason Reference.")                   
    reason_reference_id = fields.Many2one(
        comodel_name="hc.res.condition", 
        string="Reason Reference", 
        help="Condition associated with this Procedure Reason Reference.")  

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
    #     help="Diagnostic Report associated with this Procedure Report.")
                 
# Note: Causes UnicodeWarning: Unicode unequal comparison failed
# class ProcedureComplicationDetail(models.Model):
#     _name = "hc.procedure.complication.detail"
#     _description = "Procedure Complication Detail"
#     _inherit = ["hc.basic.association"]

#     procedure_id = fields.Many2one(
#         comodel_name="hc.res.procedure",
#         string="Procedure",
#         help="Procedure associated with this Procedure Complication Detail.")
#     complication_detail_id = fields.Many2one(
#         comodel_name="hc.res.condition", 
#         string="Complication Detail", 
#         help="Condition associated with this Procedure Complication Detail.")                 
                                                    
class ProcedureNote(models.Model): 
    _name = "hc.procedure.note"    
    _description = "Procedure Note"        
    _inherit = ["hc.basic.association", "hc.annotation"]    

    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this Procedure Note.")                    

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

class ProcedureNotPerformedReason(models.Model):    
    _name = "hc.vs.procedure.not.performed.reason"  
    _description = "Procedure Not Performed Reason"     
    _inherit = ["hc.value.set.contains"]    

    name = fields.Char(
        string="Name", 
        help="Name of this procedure not performed reason.")
    code = fields.Char(
        string="Code", 
        help="Code of this procedure not performed reason.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.procedure.not.performed.reason", 
        string="Parent", 
        help="Parent procedure not performed reason.")

class ProcedureNotPerformed(models.Model):  
    _name = "hc.vs.procedure.not.performed" 
    _description = "Procedure Not Performed"        
    _inherit = ["hc.value.set.contains"]      

    name = fields.Char(
        string="Name", 
        help="Name of this procedure not performed.")
    code = fields.Char(
        string="Code", 
        help="Code of this procedure not performed.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.procedure.not.performed", 
        string="Parent", 
        help="Parent procedure not performed.")

class ProcedureCategory(models.Model):  
    _name = "hc.vs.procedure.category"  
    _description = "Procedure Category"     
    _inherit = ["hc.value.set.contains"]     

    name = fields.Char(
        string="Name", 
        help="Name of this procedure category.")
    code = fields.Char(
        string="Code", 
        help="Code of this procedure category.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.procedure.category", 
        string="Parent", 
        help="Parent procedure category.")

class ProcedureOutcome(models.Model):   
    _name = "hc.vs.procedure.outcome"   
    _description = "Procedure Outcome"      
    _inherit = ["hc.value.set.contains"]    

    name = fields.Char(
        string="Name", 
        help="Name of this procedure outcome.")
    code = fields.Char(
        string="Code", 
        help="Code of this procedure outcome.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.procedure.outcome", 
        string="Parent", 
        help="Parent procedure outcome.")

class ConditionCode(models.Model):  
    _name = "hc.vs.condition.code"  
    _description = "Condition Code"     
    _inherit = ["hc.value.set.contains"]    

    name = fields.Char(
        string="Name", 
        help="Name of this condition code.")
    code = fields.Char(
        string="Code", 
        help="Code of this condition code.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.condition.code", 
        string="Parent", 
        help="Parent condition code.")

class ProcedureFollowUp(models.Model):  
    _name = "hc.vs.procedure.follow.up" 
    _description = "Procedure Follow Up"        
    _inherit = ["hc.value.set.contains"]    

    name = fields.Char(
        string="Name", 
        help="Name of this procedure follow up.")
    code = fields.Char(
        string="Code", 
        help="Code of this procedure follow up.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.procedure.follow.up", 
        string="Parent", 
        help="Parent procedure follow up.")

class ProcedureUsedCode(models.Model):  
    _name = "hc.vs.procedure.used.code" 
    _description = "Procedure Used Code"        
    _inherit = ["hc.value.set.contains"]    

    name = fields.Char(
        string="Name", 
        help="Name of this procedure used code.")
    code = fields.Char(
        string="Code", 
        help="Code of this procedure used code.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.procedure.used.code", 
        string="Parent", 
        help="Parent procedure used code.")

class PerformerRole(models.Model):  
    _name = "hc.vs.performer.role"  
    _description = "Performer Role"     
    _inherit = ["hc.value.set.contains"]    

    name = fields.Char(
        string="Name", 
        help="Name of this performer role.")
    code = fields.Char(
        string="Code", 
        help="Code of this performer role.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.performer.role", 
        string="Parent", 
        help="Parent performer role.")

class DeviceAction(models.Model):   
    _name = "hc.vs.device.action"   
    _description = "Device Action"      
    _inherit = ["hc.value.set.contains"]    

    name = fields.Char(
        string="Name", 
        help="Name of this device action.")
    code = fields.Char(
        string="Code", 
        help="Code of this device action.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.device.action", 
        string="Parent", 
        help="Parent device action.")

# External Reference

class EncounterIndication(models.Model):    
    _inherit = "hc.encounter.indication"
    
    indication_procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Indication Procedure", 
        help="Procedure reason the encounter takes place (resource).")

class AppointmentIndication(models.Model):  
    _inherit = "hc.appointment.indication" 
                                                                        
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
 
