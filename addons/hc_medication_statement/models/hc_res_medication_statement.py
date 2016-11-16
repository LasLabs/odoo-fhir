# -*- coding: utf-8 -*-

from openerp import models, fields, api

class MedicationStatement(models.Model):    
    _name = "hc.res.medication.statement"   
    _description = "Medication Statement"       

    identifier_ids = fields.One2many(
        comodel_name="hc.medication.statement.identifier", 
        inverse_name="medication_statement_id", 
        string="Identifiers", 
        help="External Identifier.")              
    status = fields.Selection(
        string="Medication Statement Status", 
        required="True", 
        selection=[
            ("active", "Active"), 
            ("completed", "Completed"), 
            ("entered-in-error", "Entered-In-Error"), 
            ("intended", "Intended")], 
        help="A coded concept indicating the current status of a Medication Statement.")             
    medication_code_id = fields.Many2one(
        comodel_name="hc.vs.medication.code", 
        string="Medication Code", 
        help="Code of what medication was taken.")             
    medication_id = fields.Many2one(
        comodel_name="hc.res.medication", 
        string="Medication", 
        help="What medication was taken.")               
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Who was/is taking medication.")             
    effective_type = fields.Selection(
        string="Effective Type", 
        selection=[
            ("dateTime", "Datetime"), 
            ("Period", "Period")], 
        help="Type of over what period was medication consumed.")                
    effective_name = fields.Char(
        string="Effective", 
        compute="_compute_effective_name", 
        store="True", 
        help="Over what period was medication consumed?")             
    effective_date = fields.Datetime(
        string="Effective Date", 
        help="Over what period was medication consumed?")             
    effective_start_date = fields.Datetime(
        string="Effective Start Date", 
        help="Start of the period when medication was consumed.")             
    effective_end_date = fields.Datetime(
        string="Effective End Date", 
        help="End of the period when medication was consumed.")               
    information_source_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Information Source Patient", 
        help="Patient who provided the information about the taking of this medication.")               
    information_source_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Information Source Practitioner", 
        help="Practitioner who provided the information about the taking of this medication.")               
    information_source_related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Information Source Related Person", 
        help="Related Person who provided the information about the taking of this medication.")               
    derived_from_ids = fields.One2many(
        comodel_name="hc.medication.statement.derived.from", 
        inverse_name="medication_statement_id", 
        string="Derived From", 
        help="Additional supporting information.")               
    date_asserted = fields.Datetime(
        string="Date Asserted", 
        help="When the statement was asserted?")                
    is_not_taken = fields.Boolean(
        string="Not Taken", 
        help="True if medication is/was not being taken.")                
    reason_not_taken_ids = fields.Many2many(
        comodel_name="hc.vs.medication.reason.not.taken", 
        relation="medication_statement_reason_not_taken_rel", 
        string="Reasons Not Taken", 
        help="True if asserting medication was not given.")             
    reason_for_use_ids = fields.Many2many(
        comodel_name="hc.vs.condition.code", 
        relation="medication_statement_reason_for_use_rel", 
        string="Reasons For Use", 
        help="Reason for why the medication is being/was taken.")              
    reason_for_use_reference_ids = fields.One2many(
        comodel_name="hc.medication.statement.reason.for.use.reference", 
        inverse_name="medication_statement_id", 
        string="Reasons For Use Reference", 
        help="Condition that supports why the medication is being/was taken.")              
    note_ids = fields.One2many(
        comodel_name="hc.medication.statement.note", 
        inverse_name="medication_statement_id", 
        string="Notes", 
        help="Further information about the statement.")                
    category_id = fields.Many2one(
        comodel_name="hc.vs.medication.statement.category", 
        string="Medication Statement Category", 
        help="Type of medication usage.")             
    dosage_ids = fields.One2many(
        comodel_name="hc.medication.statement.dosage", 
        inverse_name="medication_statement_id", 
        string="Dosages", 
        help="Details of how medication was taken.")              

class MedicationStatementIdentifier(models.Model):  
    _name = "hc.medication.statement.identifier"    
    _description = "Medication Statement Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    medication_statement_id = fields.Many2one(
        comodel_name="hc.res.medication.statement", 
        string="Medication Statement", 
        help="Medication Statement associated with this Medication Statement Identifier.")             

class MedicationStatementReasonForUseReference(models.Model):   
    _name = "hc.medication.statement.reason.for.use.reference"  
    _description = "Medication Statement Reason For Use Reference"      
    _inherit = ["hc.basic.association"]

    medication_statement_id = fields.Many2one(
        comodel_name="hc.res.medication.statement", 
        string="Medication Statement", 
        help="Medication Statement associated with this Medication Statement Reason For Use Reference.")               
    reason_for_use_reference_id = fields.Many2one(
        comodel_name="hc.res.condition", 
        string="Reason For Use Reference", 
        help="Reason For Use Reference associated with this Medication Statement Reason For Use Reference.")              


class MedicationStatementNote(models.Model):    
    _name = "hc.medication.statement.note"  
    _description = "Medication Statement Note"      
    _inherit = ["hc.basic.association", "hc.annotation"]

    medication_statement_id = fields.Many2one(
        comodel_name="hc.res.medication.statement", 
        string="Medication Statement", 
        help="Medication Statement associated with this Medication Statement Note.")               

class MedicationStatementDerivedFrom(models.Model): 
    _name = "hc.medication.statement.derived.from"  
    _description = "Medication Statement Supporting Information"        
    _inherit = ["hc.basic.association"]

    medication_statement_id = fields.Many2one(
        comodel_name="hc.res.medication.statement", 
        string="Medication Statement", 
        help="Medication Statement associated with this Medication Statement Supporting Information.")             
    derived_from_type = fields.Selection(
        string="Derived From Type", 
        selection=[
            ("string", "String"), 
            ("code", "Code")], 
        help="Type of additional supporting information.")             
    derived_from_name = fields.Char(
        string="Derived From", 
        compute="_compute_derived_from_name", 
        store="True", 
        help="Additional supporting information.")               
    derived_from_string = fields.Char(
        string="Derived From String", 
        help="String of additional supporting information.")
    derived_from_code_id = fields.Many2one(
        comodel_name="hc.vs.resource.type", 
        string="Derived From Code", 
        help="Resource type of additional supporting information.")

class MedicationStatementDosage(models.Model):  
    _name = "hc.medication.statement.dosage"    
    _description = "Medication Statement Supporting Information"        
    _inherit = ["hc.basic.association", "hc.dosage.instruction"]

    medication_statement_id = fields.Many2one(
        comodel_name="hc.res.medication.statement", 
        string="Medication Statement", 
        help="Medication Statement associated with this Medication Statement Supporting Information.")             

class MedicationStatementCategory(models.Model):    
    _name = "hc.vs.medication.statement.category"   
    _description = "Medication Statement Category"      
    _inherit = ["hc.value.set.contains"]

class MedicationReasonNotTaken(models.Model):   
    _name = "hc.vs.medication.reason.not.taken" 
    _description = "Medication Reason Not Taken"        
    _inherit = ["hc.value.set.contains"]
