# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Procedure(models.Model):  
    _name = "hc.res.procedure"  
    _description = "Procedure"          

    name = fields.Char(
        string="Name", 
        required="True", 
        help="The patient's procedure described.")                   
    identifier_ids = fields.One2many(
        comodel_name="hc.procedure.identifier", 
        inverse_name="procedure_id", 
        string="Identifiers", 
        help="External Ids for this procedure.")                    
    subject_type = fields.Selection(
        string="Procedure Subject Type",
        required="True",  
        selection=[
            ("patient", "Patient"), 
            ("group", "Group")], 
        help="Type of subject the procedure was performed on.")                    
    subject_name = fields.Char(
        string="Subject Name",
        required="True", 
        compute="compute_subject_name",  
        help="Who the procedure was performed on.")
    subject_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Subject Patient",  
        help="Patient who the procedure was performed on.")                  
    subject_group_id = fields.Many2one(
        comodel_name="hc.res.group", 
        string="Subject Group", 
        help="Group who the procedure was performed on.")                  
    status = fields.Selection(
        string="Procedure Status", 
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
    is_not_performed = fields.Boolean(
        string="Not Performed", 
        help="True if procedure was not performed as scheduled.")                    
    reason_not_peformed_ids = fields.Many2many(
        comodel_name="hc.vs.procedure.not.performed.reason", 
        string="Reason Not Peformed", 
        help="Reason procedure was not performed.")                   
    body_site_ids = fields.Many2many(
        comodel_name="hc.vs.body.site", 
        string="Body Site", 
        help="Target body sites.")                 
    reason_reference_ids = fields.One2many(
        comodel_name="hc.procedure.reason.reference", 
        inverse_name="procedure_id", 
        string="Reason References", 
        help="Condition that is the reason the procedure performed.")                 
    reason_code_id = fields.Many2one(
        comodel_name="hc.vs.procedure.reason.code", 
        string="Reason Code", 
        help="Coded reason procedure performed.")                    
    performed_date_type = fields.Selection(
        string="Procedure Performed Date Type", 
        selection=[
            ("dateTime", "Datetime"),  
            ("Period", "Period")], 
        help="Type of performed date.")                  
    performed_datetime = fields.Datetime(
        string="Performed Datetime", 
        help="Date the procedure was performed.")                 
    performed_start_date = fields.Datetime(
        string="Performed Start Date", 
        help="Start of the period when the procedure was performed.")                    
    performed_end_date = fields.Datetime(
        string="Performed End Date", 
        help="End of the period when the procedure was performed.")                  
    # encounter_id = fields.Many2one(
    #     comodel_name="hc.res.encounter", 
    #     string="Encounter", 
    #     help="The encounter associated with the procedure.")                    
    # location_id = fields.Many2one(
    #     comodel_name="hc.res.location", 
    #     string="Location", 
    #     help="Where the procedure happened.")                  
    outcome_id = fields.Many2one(
        comodel_name="hc.vs.procedure.outcome", 
        string="Outcome", 
        help="The result of procedure")                  
    report_diagnostic_report_ids = fields.One2many(
        comodel_name="hc.procedure.diagnostic.report", 
        inverse_name="procedure_id", 
        string="Report Diagnostic Reports", 
        help="Any report resulting from the procedure.")                 
    complication_ids = fields.Many2many(
        comodel_name="hc.vs.condition.code", 
        string="Complications", 
        help="Complication following the procedure.")                  
    follow_up_ids = fields.Many2many(
        comodel_name="hc.vs.procedure.follow.up", 
        string="Follow Ups", 
        help="Instructions for follow up.")                 
    # request_type = fields.Selection(
    #     string="Procedure Request Type", 
    #     selection=[
    #         ("care plan", "Care Plan"), 
    #         ("diagnostic order", "Diagnostic Order"),
    #         ("procedure request", "Procedure Request"),
    #         ("referral request", "Referral Request")], 
    #     help="Type of request for this procedure.")                  
    # request_name = fields.Char(
    #     string="Request Name", 
    #     compute="compute_request_name",
    #     help="Request reference for this procedure.")                    
    # request_care_plan_id = fields.Many2one(
    #     comodel_name="hc.res.care.plan", 
    #     string="Request Care Plan", 
    #     help="Care Plan request for this procedure.")                   
    # request_diagnostic_order_id = fields.Many2one(
    #     comodel_name="hc.res.diagnostic.order", 
    #     string="Request Diagnostic Order", 
    #     help="Diagnostic Order request for this procedure.")                   
    # request_procedure_request_id = fields.Many2one(
    #     comodel_name="hc.res.procedure.request", 
    #     string="Request Procedure Request", 
    #     help="Procedure Request request for this procedure.")                   
    # request_referral_request_id = fields.Many2one(
    #     comodel_name="hc.res.referral.request", 
    #     string="Request Referral Request", 
    #     help="Referral Request referral request request for this procedure.")                  
    note_ids = fields.One2many(
        comodel_name="hc.procedure.note", 
        inverse_name="procedure_id", 
        string="Note", 
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
    # related_item_ids = fields.One2many(
    #     comodel_name="hc.procedure.related.item", 
    #     inverse_name="procedure_id", 
    #     string="Related Items", 
    #     help="A procedure that is related to this one.")                  
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

    @api.multi          
    def compute_subject_name(self):         
        for hc_res_procedure in self:       
            if hc_res_procedure.subject_type == 'patient':  
                hc_res_procedure.subject_name = hc_res_procedure.subject_patient_id.name
            elif hc_res_procedure.subject_type == 'group':  
                hc_res_procedure.subject_name = hc_res_procedure.subject_group_id.name

    # @api.multi
    # def compute_request_name(self):
    #     for hc_res_procedure in self:
    #         if hc_res_procedure.request_type == 'care plan':
    #             hc_res_procedure.request_name = hc_res_procedure.request_care_plan_id.name
    #         elif hc_res_procedure.request_type == 'diagnostic order':
    #             hc_res_procedure.request_name = hc_res_procedure.request_diagnostic_order_id.name
    #         elif hc_res_procedure.request_type == 'procedure request':
    #             hc_res_procedure.request_name = hc_res_procedure.request_procedure_request_id.name
    #         elif hc_res_procedure.request_type == 'referral request':
    #             hc_res_procedure.request_name = hc_res_procedure.request_referral_request_id.name

class ProcedureUsedReference(models.Model): 
    _name = "hc.procedure.used.reference"   
    _description = "Procedure Used Reference"           
    
    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this procedure used reference.")                   
    # used_reference_type = fields.Selection(
    #     string="Used Reference Type", 
    #     selection=[
    #         ("Device", "Device"), 
    #         ("Medication", "Medication"), 
    #         ("Substance", "Substance")], 
    #     help="Type of item used during the procedure")                 
    # used_reference_name = fields.Char(
    #     string="Used Reference Name", 
    #     compute="compute_used_reference_name",
    #     help="The name of the item used during the procedure.")                   
    # used_reference_device_id = fields.Many2one(
    #     comodel_name="hc.res.device", 
    #     string="Used Reference Device", 
    #     help="Device item used during procedure.")                    
    # used_reference_medication_id = fields.Many2one(
    #     comodel_name="hc.res.medication", 
    #     string="Used Reference Medication", 
    #     help="Medication item used during procedure.")                 
    # used_reference_substance_id = fields.Many2one(
    #     comodel_name="hc.res.substance", 
    #     string="Used Reference Substance", 
    #     help="Substance item used during procedure.")

    # @api.multi          
    # def compute_used_reference_name(self):          
    #     for hc_procedure_used_reference in self:        
    #         if hc_procedure_used_reference.used_reference_type == 'Device': 
    #             hc_procedure_used_reference.used_reference_name = hc_procedure_used_reference.used_reference_device_id.name
    #         elif hc_procedure_used_reference.used_reference_type == 'Medication':   
    #             hc_procedure_used_reference.used_reference_name = hc_procedure_used_reference.used_reference_medication_id.name
    #         elif hc_procedure_used_reference.used_reference_type == 'Substance':    
    #             hc_procedure_used_reference.used_reference_name = hc_procedure_used_reference.used_reference_substance_id.name           

class ProcedureComponent(models.Model): 
    _name = "hc.procedure.component"    
    _description = "Procedure Component"        
    _inherit = ["hc.basic.association"] 
    
    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this procedure component.")                    
    # component_type = fields.Selection(
    #     string="Component Type", 
    #     selection=[
    #         ("Medication Administration", "Medication Administration"), 
    #         ("Procedure", "Procedure"), 
    #         ("Observation", "Observation")], 
    #     help="Type of item used during the procedure")                   
    # component_name = fields.Char(
    #     string="Component Name", 
    #     compute="compute_component_name",
    #     help="The name of the event related to the procedure.")                  
    # component_medication_administration_id = fields.Many2one(
    #     comodel_name="hc.res.medication.administration", 
    #     string="Component Medication Administration", 
    #     help="Medication Administration event related to the procedure .")                  
    # component_procedure_id = fields.Many2one(
    #     comodel_name="hc.res.procedure", 
    #     string="Component Procedure", 
    #     help="Procedure event related to the procedure .")                  
    # component_observation_id = fields.Many2one(
    #     comodel_name="hc.res.observation", 
    #     string="Component Observation", 
    #     help="Observation event related to the procedure .")                  

    # @api.multi          
    # def compute_component_name(self):           
    #     for hc_procedure_component in self:     
    #         if hc_procedure_component.component_type == 'Medication Administration':    
    #             hc_procedure_component.component_name = hc_procedure_component.component_medication_administration_id.name
    #         elif hc_procedure_component.component_type == 'Procedure':  
    #             hc_procedure_component.component_name = hc_procedure_component.component_procedure_id.name
    #         elif hc_procedure_component.component_type == 'Observation':    
    #             hc_procedure_component.component_name = hc_procedure_component.component_observation_id.name

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
            ("related person", "Related Person")], 
        help="Type of practitioner who was involved in the procedure.") 
    actor_name = fields.Char(
        string="Actor Name", 
        compute="compute_actor_name",
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
        help="The practitioner who was involved in the procedure.")                   

    @api.multi          
    def compute_actor_name(self):           
        for hc_procedure_performer in self:     
            if hc_procedure_performer.actor_type == 'practitioner': 
                hc_procedure_performer.actor_name = hc_procedure_performer.actor_practitioner_id.name
            elif hc_procedure_performer.actor_type == 'organization':   
                hc_procedure_performer.actor_name = hc_procedure_performer.actor_organization_id.name
            elif hc_procedure_performer.actor_type == 'patient':    
                hc_procedure_performer.actor_name = hc_procedure_performer.actor_patient_id.name
            elif hc_procedure_performer.actor_type == 'related person': 
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
    # manipulated_ids = fields.Many2one(
    #     comodel_name="hc.res.device", 
    #     string="Manipulated", 
    #     required="True", 
    #     help="Device that was changed.")                 

# class ProcedureRelatedItem(models.Model):   
#     _name = "hc.procedure.related.item" 
#     _description = "Procedure Related Item"         
    
#     procedure_id = fields.Many2one(
#         comodel_name="hc.res.procedure", 
#         string="Procedure", 
#         required="True", 
#         help="Procedure associated with this related item.")                   
#     type = fields.Selection(
#         string="Related Item Type", 
#         selection=[
#             ("caused-by", "Caused-By"), 
#             ("because-of", "Because-Of")], 
#         help="Type of related item.")                 
#     target_type = fields.Selection(
#         string="Related Item Target Type", 
#         selection=[
#             ("allergy intolerance", "Allergy Intolerance"), 
#             ("care plan", "Care Plan"),
#             ("condition", "Condition"),
#             ("diagnostic report", "Diagnostic Report"),
#             ("family member history", "Family Member History"),
#             ("imaging study", "Imaging Study"),("immunization", "Immunization"), 
#             ("immunization recommendation", "Immunization Recommendation"),
#             ("medication administration", "Medication Administration"),
#             ("medication dispense", "Medication Dispense"),
#             ("medication prescription", "Medication Prescription"),
#             ("medication statement", "Medication Statement"),
#             ("observation", "Observation"),
#             ("procedure", "Procedure")], 
#         help="Type of related item.")                    
#     target_allergy_intolerance_id = fields.Many2one(
#         comodel_name="hc.res.allergy.intolerance", 
#         string="Target Allergy Intolerance", 
#         help="Allergy Intolerance related item.")                   
#     target_care_plan_id = fields.Many2one(
#         comodel_name="hc.res.care.plan", 
#         string="Target Care Plan", 
#         help="Care Plan related item.")                   
#     target_condition_id = fields.Many2one(
#         comodel_name="hc.res.condition", 
#         string="Target Condition", 
#         help="Condition related item.")                   
#     target_diagnostic_report_id = fields.Many2one(
#         comodel_name="hc.res.diagnostic.report", 
#         string="Target Diagnostic Report", 
#         help="Diagnostic Report related item.")                   
#     target_family_member_history_id = fields.Many2one(
#         comodel_name="hc.res.family.member.history", 
#         string="Target Family Member History", 
#         help="Family Member history related item.")                   
#     target_imaging_study_id = fields.Many2one(
#         comodel_name="hc.res.imaging.study", 
#         string="Target Imaging Study", 
#         help="Imaging Study related item.")                   
#     target_immunization_id = fields.Many2one(
#         comodel_name="hc.res.immunization", 
#         string="Target Immunization", 
#         help="Immunization related item.")                   
#     target_immunization_recommendation_id = fields.Many2one(
#         comodel_name="hc.res.immunization.recommendation", 
#         string="Target Immunization Recommendation", 
#         help="Immunization Recommendation related item.")                   
#     target_medication_admnistration_id = fields.Many2one(
#         comodel_name="hc.res.medication.administration", 
#         string="Target Medication Admnistration", 
#         help="Medication Administration related item.")                 
#     target_medication_dispense_id = fields.Many2one(
#         comodel_name="hc.res.medication.dispense", 
#         string="Target Medication Dispense", 
#         help="Medication Dispense related item.")                   
#     target_medication_order_id = fields.Many2one(
#         comodel_name="hc.res.medication.order", 
#         string="Target Medication Order", 
#         help="Medication Order related item.")                   
#     target_medication_statement_id = fields.Many2one(
#         comodel_name="hc.res.medication.statement", 
#         string="Target Medication Statement", 
#         help="Medication Statement related item.")                   
#     target_observation_id = fields.Many2one(
#         comodel_name="hc.res.observation", 
#         string="Target Observation", 
#         help="Observation related item.")                   
#     target_procedure_id = fields.Many2one(
#         comodel_name="hc.res.procedure", 
#         string="Target Procedure", 
#         help="Procedure related item.")                   

class ProcedureBodySite(models.Model):  
    _name = "hc.procedure.body.site"    
    _description = "Procedure Body Site"        
    _inherit = ["hc.basic.association"] 
    
    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure performed on this Body Site.")                  
    # body_site_id = fields.Many2one(
    #     comodel_name="hc.res.body.site", 
    #     string="Body Site", 
    #     help="Body Site performed with this Procedure.")                    

class ProcedureDiagnosticReport(models.Model):  
    _name = "hc.procedure.diagnostic.report"    
    _description = "Procedure Diagnostic Report"        
    _inherit = ["hc.basic.association"] 
    
    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this Diagnostic Report.")                   
    # diagnostic_report_id = fields.Many2one(
    #     comodel_name="hc.res.diagnostic.report", 
    #     string="Diagnostic Report", 
    #     help="Diagnostic Report associated with this Procedure.")                   

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
        help="Procedure associated with this Medication.")                  
    # medication_id = fields.Many2one(
    #     comodel_name="hc.res.medication", 
    #     string="Medication", 
    #     help="Medication associated with this Procedure.")                   

class ProcedureSubstance(models.Model): 
    _name = "hc.procedure.substance"    
    _description = "Procedure Substance"        
    _inherit = ["hc.basic.association"] 

    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this Substance.")                   
    # substance_id = fields.Many2one(
    #     comodel_name="hc.res.substance", 
    #     string="Substance", 
    #     help="Substance associated with this Procedure.")                   

# class ProcedureComplication(models.Model):  
#     _name = "hc.procedure.complication" 
#     _description = "Procedure Complication"     
#     inherit = ["hc.basic.association"]

#     procedure_id = fields.Many2one(
#         comodel_name="hc.res.procedure", 
#         string="Procedure", 
#         help="Procedure associated with this Complication.")                    
#     complication_id = fields.Many2one(
#         comodel_name="hc.res.", 
#         string="Complication", 
#         help="Complication associated with this Procedure.")                   

class ProcedureReasonReference(models.Model):   
    _name = "hc.procedure.reason.reference" 
    _description = "Procedure Reason Reference"     
    _inherit = ["hc.basic.association"] 
    
    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this Condition.")                   
    # condition_id = fields.Many2one(
    #     comodel_name="hc.res.condition", 
    #     string="Condition", 
    #     help="Condition associated with this Procedure.")                   

class ProcedureNote(models.Model): 
    _name = "hc.procedure.note"    
    _description = "Procedure Note"        
    _inherit = ["hc.basic.association", "hc.annotation"]    

    procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Procedure", 
        help="Procedure associated with this annotation.")                  

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

class ProcedureReasonCode(models.Model):    
    _name = "hc.vs.procedure.reason.code"   
    _description = "Procedure Reason Code"      
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
