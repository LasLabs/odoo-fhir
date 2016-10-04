# -*- coding: utf-8 -*-

from openerp import models, fields, api

class MedicationAdministration(models.Model):    
    _name = "hc.res.medication.administration"    
    _description = "Medication Administration"        

    identifier_ids = fields.One2many(
        comodel_name="hc.medication.administration.identifier", 
        inverse_name="medication_administration_id", 
        string="Identifiers", 
        help="External identifier.")                
    status = fields.Selection(
        string="Medication Administration Status", 
        required="True", 
        selection=[
            ("in-progress", "In-Progress"), 
            ("on-hold", "On-Hold"), 
            ("completed", "Completed"), 
            ("entered-in-error", "Entered-In-Error"), 
            ("stopped", "Stopped")], 
        help="The status for the event.")                
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        required="True", 
        help="Who received medication?")                
    practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Practitioner", 
        help="Who administered substance?")                
    encounter_id = fields.Many2one(
        comodel_name="hc.res.encounter", 
        string="Encounter", 
        help="Encounter administered as part of.")                
    medication_order_id = fields.Many2one(
        comodel_name="hc.res.medication.order", 
        string="Medication Order", 
        help="Order administration performed against.")                
    is_was_not_given = fields.Boolean(
        string="Was Not Given", 
        help="True if medication not administered.")                
    reason_not_given_ids = fields.One2many(
        comodel_name="hc.medication.administration.reason.not.given", 
        inverse_name="medication_administration_id", 
        string="Reasons Not Given", 
        help="Reason administration not performed.")                
    reason_given_ids = fields.One2many(
        comodel_name="hc.medication.administration.reason.given", 
        inverse_name="medication_administration_id", 
        string="Reasons Given", 
        help="Reason administration performed.")                
    effective_time_type = fields.Selection(
        string="Effective Time Type", 
        required="True", 
        selection=[
            ("dateTime", "Datetime"), 
            ("Period", "Period")], 
        help="Type of start and end time of administration.")                
    effective_time_name = fields.Char(
        string="Effective Time", 
        compute="_compute_effective_time_name", 
        store="True", 
        help="Start and end time of administration.")                
    effective_time = fields.Datetime(
        string="Effective Time", 
        help="Time of admistration.")                
    start_effective_time = fields.Datetime(
        string="Start Effective Time", 
        help="Start time of administration.")                
    end_effective_time = fields.Datetime(
        string="End Effective Time", 
        help="End time of administration.")                
    medication_type = fields.Selection(
        string="Medication Type", 
        required="True", 
        selection=[
            ("Code", "Code"), 
            ("Medication", "Medication")], 
        help="Type of what was administered.")                
    medication_name = fields.Char(
        string="Medication", 
        compute="_compute_medication_name", 
        store="True", 
        help="What was administered?.")                
    medication_code_id = fields.Many2one(
        comodel_name="hc.vs.medication.code", 
        string="Medication Code", 
        help="Code of medication administered")                
    medication_id = fields.Many2one(
        comodel_name="hc.res.medication", 
        string="Medication", 
        help="Medication administered.")                
    device_ids = fields.One2many(
        comodel_name="hc.medication.administration.device", 
        inverse_name="medication_administration_id", 
        string="Devices", 
        help="Device used to administer.")                
    note_ids = fields.One2many(
        comodel_name="hc.medication.administration.note", 
        inverse_name="medication_administration_id", 
        string="Note", 
        help="Information about the administration.")                
    dosage_ids = fields.One2many(
        comodel_name="hc.medication.administration.dosage", 
        inverse_name="medication_administration_id", 
        string="Dosages", 
        help="Details of how medication was taken.")                
    event_history_ids = fields.One2many(
        comodel_name="hc.medication.administration.event.history", 
        inverse_name="medication_administration_id", 
        string="Event Histories", 
        help="A list of events of interest in the lifecycle.")                

class MedicationAdministrationDosage(models.Model):    
    _name = "hc.medication.administration.dosage"    
    _description = "Medication Administration Dosage"        

    medication_administration_id = fields.Many2one(
        comodel_name="hc.res.medication.administration", 
        string="Medication Administration", 
        help="Medication Administration associated with this Medication Administration Dosage.")                
    text = fields.Text(
        string="Text", 
        help="Dosage Instructions.")                
    site_id = fields.Many2one(
        comodel_name="hc.vs.approach.site.code", 
        string="Site", 
        help="Body site administered to.")                
    route_id = fields.Many2one(
        comodel_name="hc.vs.route.code", 
        string="Route", 
        help="Path of substance into body.")                
    method_id = fields.Many2one(
        comodel_name="hc.vs.administration.method.code", 
        string="Method", 
        help="How drug was administered.")                
    quantity = fields.Float(
        string="Quantity", 
        help="Amount administered in one dose.")                
    quantity_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Quantity UOM", 
        help="Quantity unit of measure.")                
    dose_quantity_numerator = fields.Float(
        string="Dose Quantity Numerator", 
        help="Numerator value of dose quantity per unit of time.")                
    dose_period_denominator = fields.Float(
        string="Dose Period Denominator", 
        help="Denominator value of dose quantity per unit of time.")                
    dose_rate = fields.Float(
        string="Dose Rate", 
        compute="_compute_dose_rate", 
        store="True", 
        help="Dose quantity per unit of time.")                
    dose_rate_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Dose Rate UOM", 
        help="Dose quantity per unit of time unit of measure.")                

class MedicationAdministrationEventHistory(models.Model):    
    _name = "hc.medication.administration.event.history"    
    _description = "Medication Administration Event History"        

    medication_administration_id = fields.Many2one(
        comodel_name="hc.res.medication.administration", 
        string="Medication Administration", 
        help="Medication Administration associated with this Medication Administration Event History.")                
    status = fields.Selection(
        string="Event History Status", 
        required="True", 
        selection=[
            ("in-progress", "In-Progress"), 
            ("on-hold", "On-Hold"), 
            ("completed", "Completed"), 
            ("entered-in-error", "Entered-In-Error"), 
            ("stopped", "Stopped")], 
        help="The status for the event.")                
    action_id = fields.Many2one(
        comodel_name="hc.vs.medication.event.history.action", 
        string="Action", 
        help="Action taken (e.g. verify).")                
    recorded_date = fields.Datetime(
        string="Recorded Date", 
        required="True", 
        help="The date at which the event happened.")                
    actor_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Actor", 
        help="Who took the action.")                
    reason_id = fields.Many2one(
        comodel_name="hc.vs.medication.event.history.action", 
        string="Reason", 
        help="Reason the action was taken.")                

class MedicationAdministrationIdentifier(models.Model):    
    _name = "hc.medication.administration.identifier"    
    _description = "Medication Administration Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    medication_administration_id = fields.Many2one(
        comodel_name="hc.res.medication.administration", 
        string="Medication Administration", 
        help="Medication Administration associated with this Medication Administration Identifier.")                

class MedicationAdministrationNote(models.Model):    
    _name = "hc.medication.administration.note"    
    _description = "Medication Administration Note"        
    _inherit = ["hc.basic.association", "hc.annotation"]

    medication_administration_id = fields.Many2one(
        comodel_name="hc.res.medication.administration", 
        string="Medication Administration", 
        help="Medication Administration associated with this Medication Administration Note.")                

class MedicationAdministrationReasonNotGiven(models.Model):    
    _name = "hc.medication.administration.reason.not.given"    
    _description = "Medication Administration Reason Not Given"        
    _inherit = ["hc.basic.association"]

    medication_administration_id = fields.Many2one(
        comodel_name="hc.res.medication.administration", 
        string="Medication Administration", 
        help="Medication Administration associated with this Medication Administration Reason Not Given.")                
    reason_not_given_id = fields.Many2one(
        comodel_name="hc.vs.reason.medication.not.given", 
        string="Reason Not Given", 
        help="Reason Not Given associated with this Medication Administration Reason Not Given.")                

class MedicationAdministrationReasonGiven(models.Model):    
    _name = "hc.medication.administration.reason.given"    
    _description = "Medication Administration Reason Given"        
    _inherit = ["hc.basic.association"]

    medication_administration_id = fields.Many2one(
        comodel_name="hc.res.medication.administration", 
        string="Medication Administration", 
        help="Medication Administration associated with this Medication Administration Reason Given.")                
    reason_given_id = fields.Many2one(
        comodel_name="hc.vs.reason.medication.given", 
        string="Reason Given", 
        help="Reason Given associated with this Medication Administration Reason Given.")                

class MedicationAdministrationDevice(models.Model):    
    _name = "hc.medication.administration.device"    
    _description = "Medication Administration Device"        
    _inherit = ["hc.basic.association"]

    medication_administration_id = fields.Many2one(
        comodel_name="hc.res.medication.administration", 
        string="Medication Administration", 
        help="Medication Administration associated with this Medication Administration Device.")                

class ApproachSiteCode(models.Model):    
    _name = "hc.vs.approach.site.code"    
    _description = "Approach Site Code"        
    _inherit = ["hc.value.set.contains"]

class AdministrationMethodCode(models.Model):    
    _name = "hc.vs.administration.method.code"    
    _description = "Administration Method Code"        
    _inherit = ["hc.value.set.contains"]

class ReasonMedicationNotGiven(models.Model):    
    _name = "hc.vs.reason.medication.not.given"    
    _description = "Reason Medication Not Given"        
    _inherit = ["hc.value.set.contains"]

class ReasonMedicationGiven(models.Model):    
    _name = "hc.vs.reason.medication.given"    
    _description = "Reason Medication Given"        
    _inherit = ["hc.value.set.contains"]