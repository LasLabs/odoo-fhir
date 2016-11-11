# -*- coding: utf-8 -*-

from openerp import models, fields, api

class MedicationRequest(models.Model):  
    _name = "hc.res.medication.request" 
    _description = "Medication Request"         

    identifier_ids = fields.One2many(comodel_name="hc.medication.request.identifier", inverse_name="medication_request_id", string="Identifiers", help="External identifier.")                  
    definition_ids = fields.One2many(comodel_name="hc.medication.request.definition", inverse_name="medication_request_id", string="Libraries", help="Protocol or definition.")                 
    based_on_ids = fields.One2many(comodel_name="hc.medication.request.based.on", inverse_name="medication_request_id", string="Libraries", help="What request fulfills.")                  
    requisition_id = fields.Many2one(comodel_name="hc.medication.request.requisition", string="Requisition", help="Identifier of composite.")                   
    status = fields.Selection(string="Status", selection=[("active", "Active"), ("on-hold", "On-Hold"), ("cancelled", "Cancelled"), ("completed", "Completed"), ("entered-in-error", "Entered-In-Error"), ("stopped", "Stopped"), ("draft", "Draft")], help="A code specifying the state of the order. Generally this will be active or completed state.")                  
    stage = fields.Selection(string="Stage", required="True", selection=[("proposal", "Proposal"), ("plan", "Plan"), ("original-order", "Original-Order")], help="Whether the request is a proposal, plan, or an original order.")                  
    medication_type = fields.Selection(string="Medication Type", required="True", selection=[("code", "Code"), ("Timing", "Timing")], help="Type of medication to be taken.")                   
    medication_name = fields.Char(string="Medication", compute="_compute_medication_name", store="True", help="Medication to be taken.")                    
    medication_code_id = fields.Many2one(comodel_name="hc.vs.medication.code", string="Medication Code", help="Code of medication to be taken.")                    
    medication_id = fields.Many2one(comodel_name="hc.res.medication", string="Medication", required="True", help="Medication to be taken.")                 
    patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Patient", required="True", help="Who prescription is for.")                 
    context_type = fields.Selection(string="Context Type", selection=[("Encounter", "Encounter"), ("Episode Of Care", "Episode Of Care")], help="Type created during encounter/admission/stay.")                    
    context_name = fields.Char(string="Context", compute="_compute_context_name", store="True", help="Created during encounter/admission/sta.")                 
    context_encounter_id = fields.Many2one(comodel_name="hc.res.encounter", string="Context Encounter", help="Encounter created during encounter/admission/stay.")                  
    context_episode_of_care_id = fields.Many2one(comodel_name="hc.res.episode.of.care", string="Context Episode Of Care", help="Episode Of Care during encounter/admission/stay.")                  
    supporting_information_type = fields.Selection(string="Supporting Information Type", selection=[("string", "String"), ("code", "Code")], help="Type of what is account tied to.")                   
    supporting_information_name = fields.Char(string="Supporting Information", compute="_compute_supporting_information_name", store="True", help="Information to support ordering of the medication.")                 
    supporting_information_string = fields.Char(string="Supporting Information String", help="Information to support ordering of the medication.")                  
    supporting_information_code_id = fields.Many2one(comodel_name="hc.vs.resource.type", string="Supporting Information Code", help="Type of resource of information to support ordering of the medication.")                   
    date_written = fields.Datetime(string="Date Written", help="When prescription was initially authorized.")                   
    prescriber_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Prescriber", help="Who ordered the initial medication(s).")                 
    reason_code_ids = fields.Many2many(comodel_name="hc.vs.activity.definition.topic", string="Reason Codes", help="Reason or indication for writing the prescription.")                    
    reason_reference_ids = fields.One2many(comodel_name="hc.medication.request.reason.reference", inverse_name="medication_request_id", string="Libraries", help="Condition or Observation that supports why the prescription is being written.")                   
    note_ids = fields.One2many(comodel_name="hc.medication.request.note", inverse_name="medication_request_id", string="Notes", help="Information about the prescription.")                 
    category_id = fields.Many2one(comodel_name="hc.vs.medication.request.category", string="Category", help="Type of medication usage.")                    
    dosage_instruction_ids = fields.One2many(comodel_name="hc.medication.request.dosage.instruction", inverse_name="medication_request_id", string="Dosage Instructions", help="How the medication should be taken.")                   
    prior_prescription_id = fields.Many2one(comodel_name="hc.res.medication.request", string="Prior Prescription", help="An order/prescription that this supersedes.")                  
    event_history_ids = fields.One2many(comodel_name="hc.medication.request.event.history", inverse_name="medication_request_id", string="Libraries", help="A list of events of interest in the lifecycle.")                    
    dispense_request_ids = fields.One2many(comodel_name="hc.medication.request.dispense.request", inverse_name="medication_request_id", string="Dispense Requests", help="Medication supply authorization.")                    
    substitution_ids = fields.One2many(comodel_name="hc.medication.request.substitution", inverse_name="medication_request_id", string="Substitutions", help="Any restrictions on medication substitution.")                    

class MedicationRequestDispenseRequest(models.Model):   
    _name = "hc.medication.request.dispense.request"    
    _description = "Medication Request Dispense Request"            

    medication_request_id = fields.Many2one(comodel_name="hc.res.medication.request", string="Medication Request", help="Medication Request associated with this Medication Request Dispense Request.")                 
    validity_period_start_date = fields.Datetime(string="Validity Period Start Date", help="Start of the time period supply is authorized for.")                    
    validity_period_end_date = fields.Datetime(string="Validity Period End Date", help="End of the time period supply is authorized for.")                  
    number_of_repeats_allowed = fields.Integer(string="Number Of Repeats Allowed", help="Number of refills authorized.")                    
    quantity = fields.Float(string="Quantity", help="Amount of medication to supply per dispense.")                 
    expected_supply_duration = fields.Float(string="Expected Supply Duration", help="Number of days supply per dispense.")                  
    performer_id = fields.Many2one(comodel_name="hc.res.organization", string="Performer", help="Intended dispenser.")                  

class MedicationRequestSubstitution(models.Model):  
    _name = "hc.medication.request.substitution"    
    _description = "Medication Request Substitution"            

    medication_request_id = fields.Many2one(
        comodel_name="hc.res.medication.request", 
        string="Medication Request", 
        help="Medication Request associated with this Medication Request Substitution.")                 
    is_allowed = fields.Boolean(
        string="Allowed", 
        required="True", 
        help="Whether substitution is allowed or not.")                  
    reason_id = fields.Many2one(
        comodel_name="hc.vs.substance.admin.substitution.reason", 
        string="Reason", 
        help="Why should (not) substitution be made.")                   

class MedicationRequestIdentifier(models.Model):    
    _name = "hc.medication.request.identifier"  
    _description = "Medication Request Identifier"      
    _inherit = ["hc.basic.association", "hc.identifier"]    

    medication_request_id = fields.Many2one(comodel_name="hc.res.medication.request", string="Medication Request", help="Medication Request associated with this Medication Request Identifier.")                   

class MedicationRequestDefinition(models.Model):    
    _name = "hc.medication.request.definition"  
    _description = "Medication Request Definition"      
    _inherit = ["hc.basic.association"] 

    medication_request_id = fields.Many2one(comodel_name="hc.res.medication.request", string="Medication Request", help="Medication Request associated with this Medication Request Definition.")                   
    definition_type = fields.Selection(string="Definition Type", selection=[("Activity Definition", "Activity Definition"), ("Plan Definition", "Plan Definition")], help="Protocol or definition.")                    
    definition_name = fields.Char(string="Definition", compute="_compute_definition_name", store="True", help="Protocol or definitio.")                 
    definition_activity_definition_id = fields.Many2one(comodel_name="hc.res.activity.definition", string="Definition Activity Definition", help="Activity Definition protocol or definition.")                 
    # definition_plan_definition_id = fields.Many2one(
    #     comodel_name="hc.res.plan.definition", 
    #     string="Definition Plan Definition", 
    #     help="Plan Definition or definition.")                  

class MedicationRequestBasedOn(models.Model):   
    _name = "hc.medication.request.based.on"    
    _description = "Medication Request Based On"        
    _inherit = ["hc.basic.association"] 

    medication_request_id = fields.Many2one(
        comodel_name="hc.res.medication.request", 
        string="Medication Request", 
        help="Medication Request associated with this Medication Request Based On.")                 
    based_on_type = fields.Selection(
        string="Based On Type", 
        selection=[
            # ("Care Plan", "Care Plan"), 
            ("Diagnostic Request", "Diagnostic Request"), 
            ("Medication Request", "Medication Request"), 
            ("Procedure Request", "Procedure Request"), 
            ("Referral Request", "Referral Request")], 
        help="Type of what request fulfills.")
    based_on_name = fields.Char(
        string="Based On", 
        compute="_compute_based_on_name", 
        store="True", help="What request fulfill.")                    
    # based_on_care_plan_id = fields.Many2one(comodel_name="hc.res.care.plan", string="Based On Care Plan", help="Care Plan request fulfills.")                   
    based_on_diagnostic_request_id = fields.Many2one(comodel_name="hc.res.diagnostic.request", string="Based On Diagnostic Request", help="Diagnostic Request fulfills.")                   
    based_on_medication_request_id = fields.Many2one(comodel_name="hc.res.medication.request", string="Based On Medication Request", help="Medication Request fulfills.")                   
    based_on_procedure_request_id = fields.Many2one(comodel_name="hc.res.procedure.request", string="Based On Procedure Request", help="Procedure Request fulfills.")                   
    based_on_referral_request_id = fields.Many2one(comodel_name="hc.res.referral.request", string="Based On Referral Request", help="Referral Request fulfills.")                   

class MedicationRequestRequisition(models.Model):   
    _name = "hc.medication.request.requisition" 
    _description = "Medication Request Requisition"     
    _inherit = ["hc.basic.association", "hc.identifier"]    

class MedicationRequestReasonReference(models.Model):   
    _name = "hc.medication.request.reason.reference"    
    _description = "Medication Request Reason Reference"        
    _inherit = ["hc.basic.association"] 

    medication_request_id = fields.Many2one(comodel_name="hc.res.medication.request", string="Medication Request", help="Medication Request associated with this Medication Request Reason Reference.")                 
    reason_reference_type = fields.Selection(string="Reason Reference Type", selection=[("Condition", "Condition"), ("Observation", "Observation")], help="Condition or Observation that supports why the prescription is being written.")                  
    reason_reference_name = fields.Char(string="Reason Reference", compute="_compute_reason_reference_name", store="True", help="Condition or Observation that supports why the prescription is being writte.")                 
    reason_reference_condition_id = fields.Many2one(comodel_name="hc.res.condition", string="Reason Reference Condition", help="Condition that supports why the prescription is being written.")                    
    reason_reference_observation_id = fields.Many2one(comodel_name="hc.res.observation", string="Reason Reference Observation", help="Observation that supports why the prescription is being written.")                    

class MedicationRequestNote(models.Model):  
    _name = "hc.medication.request.note" 
    _description = "Medication Request Note"        
    _inherit = ["hc.basic.association", "hc.annotation"]    

    medication_request_id = fields.Many2one(comodel_name="hc.res.medication.request", string="Medication Request", help="Medication Request associated with this Medication Request Note.")                 

class MedicationRequestDosageInstruction(models.Model): 
    _name = "hc.medication.request.dosage.instruction"  
    _description = "Medication Request Dosage Instruction"      
    _inherit = ["hc.basic.association", "hc.dosage.instruction"]    

    medication_request_id = fields.Many2one(
        comodel_name="hc.res.medication.request", 
        string="Medication Request", 
        help="Medication Request associated with this Medication Request Dosage Instruction.")                   

class MedicationRequestEventHistory(models.Model):  
    _name = "hc.medication.request.event.history"   
    _description = "Medication Request Event History"       
    _inherit = ["hc.basic.association"] 

    medication_request_id = fields.Many2one(comodel_name="hc.res.medication.request", string="Medication Request", help="Medication Request associated with this Medication Request Event History.")                    
    event_history_id = fields.Many2one(comodel_name="hc.res.provenance", string="Event History", help="Event History associated with this Medication Request Event History.")                   

class MedicationRequestCategory(models.Model):  
    _name = "hc.vs.medication.request.category" 
    _description = "Medication Request Category"        
    _inherit = ["hc.value.set.contains"]    

class SubstanceAdminSubstitutionReason(models.Model):   
    _name = "hc.vs.substance.admin.substitution.reason" 
    _description = "Substance Admin Substitution Reason"        
    _inherit = ["hc.value.set.contains"]


# External Reference


# class CarePlanActivity(models.Model):    
#     _inherit = "hc.care.plan.activity"    
    
#     reference_type = fields.Selection(
#         string="Reference Type", 
#         selection=[
#             ("Appointment", "Appointment"), 
#             ("Communication Request", "Communication Request"), 
#             ("Device Use Request", "Device Use Request"), 
#             ("Diagnostic Request", "Diagnostic Request"), 
#             ("Medication Request", "Medication Request"), 
#             ("Nutrition Request", "Nutrition Request"), 
#             ("Procedure Request", "Procedure Request"), 
#             ("Process Request", "Process Request"),
#             ("Referral Request", "Referral Request"),
#             ("Supply Request", "Supply Request"),
#             ("Vision Prescription", "Vision Prescription")], 
#         help="Type of entity assessed.")

#     reference_medication_request_id = fields.Many2one(
#         comodel_name="hc.res.medication.request", 
#         string="Reference Medication Request", 
#         help="Medication Request activity details defined in specific resource.")

# class CarePlanActivityActionResulting(models.Model):    
#     _inherit = "hc.care.plan.activity.action.resulting"    

#     action_resulting_type = fields.Selection(
#         string="Action Resulting Type", 
#         selection=[
#             ("Appointment", "Appointment"), 
#             ("Communication Request", "Communication Request"), 
#             ("Device Use Request", "Device Use Request"), 
#             ("Diagnostic Request", "Diagnostic Request"), 
#             ("Medication Request", "Medication Request"), 
#             ("Nutrition Request", "Nutrition Request"), 
#             ("Procedure Request", "Procedure Request"), 
#             ("Process Request", "Process Request"),
#             ("Referral Request", "Referral Request"),
#             ("Supply Request", "Supply Request"),
#             ("Vision Prescription", "Vision Prescription")], 
#         help="Type of resource that describes follow-on actions resulting from the plan.")

#     action_resulting_medication_request_id = fields.Many2one(
#         comodel_name="hc.res.medication.request", 
#         string="Action Resulting Medication Request", 
#         help="Medication Request resource that describes follow-on actions resulting from the plan.")