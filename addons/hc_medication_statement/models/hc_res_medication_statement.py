# -*- coding: utf-8 -*-

from openerp import models, fields, api

class MedicationStatement(models.Model):    
    _name = "hc.res.medication.statement"    
    _description = "Medication Statement"        

    identifier_ids = fields.One2many(
        comodel_name="hc.med.stmt.identifier", 
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
        help="On what date was medication consumed?")                
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
    supporting_information_ids = fields.One2many(
        comodel_name="hc.med.stmt.supporting.information", 
        inverse_name="medication_statement_id", 
        string="Supporting Information", 
        help="Additional supporting information.")                
    date_asserted = fields.Datetime(
        string="Date Asserted", 
        help="When the statement was asserted?")                
    is_was_not_taken = fields.Boolean(
        string="Was Not Taken", 
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
        comodel_name="hc.med.stmt.reason.for.use.reference", 
        inverse_name="medication_statement_id", 
        string="Reasons For Use Reference", 
        help="Condition that supports why the medication is being/was taken.")                
    note_ids = fields.One2many(
        comodel_name="hc.med.stmt.note", 
        inverse_name="medication_statement_id", 
        string="Notes", 
        help="Further information about the statement.")                
    category_id = fields.Many2one(
        comodel_name="hc.vs.medication.statement.category", 
        string="Medication Statement Category", 
        help="Type of medication usage.")                
    dosage_ids = fields.One2many(
        comodel_name="hc.med.stmt.dosage", 
        inverse_name="medication_statement_id", 
        string="Dosages", 
        help="Details of how medication was taken.")                

class MedStmtDosage(models.Model):    
    _name = "hc.med.stmt.dosage"    
    _description = "Medication Statement Dosage"        

    medication_statement_id = fields.Many2one(
        comodel_name="hc.res.medication.statement", 
        string="Medication Statement", 
        help="Medication Statement associated with this Medication Statement Dosage.")                
    text = fields.Text(
        string="Text", 
        help="Dosage Instructions.")                
    additional_instructions_ids = fields.Many2many(
        comodel_name="hc.vs.additional.instructions.code",
        relation="med_stmt_dosage_additional_instructions_rel",  
        string="Additional Instructions", 
        help='Supplemental instructions - e.g. "with meals".')                
    timing_ids = fields.One2many(
        comodel_name="hc.med.stmt.dosage.timing", 
        inverse_name="med_stmt_dosage_id", 
        string="Timings", 
        help="When/how often was medication taken.")                
    medication_type = fields.Selection(
        string="Medication Type", 
        selection=[
            ("boolean", "Boolean"), 
            ("code", "Code")], 
        help="Type of product to be supplied.")                
    as_needed_name = fields.Char(
        string="As Needed", 
        compute="_compute_as_needed_name", 
        store="True", 
        help='Take "as needed".')                
    is_as_needed = fields.Boolean(
        string="As Needed", 
        help='Boolean take "as needed" f(or x).')                
    as_needed_code_id = fields.Many2one(
        comodel_name="hc.vs.medication.as.needed.reason", 
        string="As Needed Code", 
        help='Code of take "as needed" f(or x).')                
    medication_type = fields.Selection(
        string="Medication Type", 
        selection=[
            ("code", "Code"), 
            ("Body Site", "Body Site")], 
        help="Type of product to be supplied.")                
    site_name = fields.Char(
        string="Site", 
        compute="_compute_site_name", 
        store="True", 
        help="Where (on body) medication is/was administered.")                
    site_code_id = fields.Many2one(
        comodel_name="hc.vs.approach.site.code", 
        string="Site Code", 
        help="Code of where (on body) medication is/was administered.")                
    site_id = fields.Many2one(
        comodel_name="hc.res.body.site", 
        string="Site", 
        help="Body Site where (on body) medication is/was administered.")                
    route_id = fields.Many2one(
        comodel_name="hc.vs.route.code", 
        string="Route", 
        help="How did the medication enter the body?")                
    method_id = fields.Many2one(
        comodel_name="hc.vs.administration.method.code", 
        string="Method", 
        help="Technique used to administer medication.")                
    dose_type = fields.Selection(
        string="Dose Type", 
        selection=[
            ("Range", "Range"), 
            ("Quantity", "Quantity")], 
        help="Type of amount of medication per dose.")                
    dose_name = fields.Char(
        string="Dose", 
        compute="_compute_dose_name", 
        store="True", 
        help="Take as needed.")                
    dose_quantity = fields.Float(
        string="Dose Quantity", 
        help="Amount of medication per dose.")           
    dose_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Dose UOM", 
        help="Amount of medication per dose unit of measure.")                
    dose_range_low = fields.Float(
        string="Dose Range Low", 
        help="Low limit of amount of medication per dose.")                
    dose_range_high = fields.Float(
        string="Dose Range High", 
        help="High limit of amount of medication per dose.")                
    rate_type = fields.Selection(
        string="Rate Type", 
        selection=[
            ("Ratio", "Ratio"), 
            ("Range", "Range"), 
            ("Quantity", "Quantity")], 
        help="Type of dose quantity per unit of time.")                
    rate_name = fields.Char(
        string="Rate", 
        compute="_compute_rate_name", 
        store="True", 
        help="Dose quantity per unit of time.")                
    dose_quantity_numerator = fields.Float(
        string="Dose Quantity Numerator", 
        help="Numerator value of dose quantity per unit of time.")                
    dose_quantity_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Dose Quantity UOM", 
        help="Dose Quantity unit of measure.")
    dose_period_denominator = fields.Float(
        string="Dose Period Denominator", 
        help="Denominator value of dose quantity per unit of time.")
    dose_period_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Dose Period UOM", 
        help="Dose Period unit of measure.")
    rate_ratio = fields.Float(
        string="Rate Ratio", 
        compute="_compute_rate_ratio", 
        store="True", 
        help="Dose quantity per unit of time.")                
    rate_ratio_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Rate Ratio UOM", 
        help="Dose quantity per unit of time unit of measure.")                
    rate_range_low = fields.Float(
        string="Rate Range Low", 
        help="Low limit of dose quantity per unit of time.")                
    rate_range_high = fields.Float(
        string="Rate Range High", 
        help="High limit of dose quantity per unit of time.")                
    rate_quantity = fields.Float(
        string="Rate Quantity", 
        help="Dose quantity per unit of time.")                
    rate_quantity_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Rate Quantity UOM", 
        help="Rate unit of measure.")                               
    max_dose_quantity = fields.Float(
        string="Maximum Dose Quantity", 
        help="Maximum dose that was consumed.")
    max_dose_period = fields.Integer(
        string="Maximum Dose Period", 
        help="Unit of time when maximum dose was consumed.")
    max_dose_period_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Maximum Dose Period UOM", 
        help="Period unit of measure.")
    max_dose_per_period = fields.Integer(
        string="Maximum Dose per Period", 
        compute="_compute_max_dose_per_period", 
        store="True", 
        help="Maximum dose that was consumed per unit of time.")
    max_dose_per_period_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Maximum Dose per Period UOM", 
        help="Period unit of measure.")

class MedStmtReasonForUseReference(models.Model):    
    _name = "hc.med.stmt.reason.for.use.reference"    
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

class MedStmtDosageTiming(models.Model):    
    _name = "hc.med.stmt.dosage.timing"    
    _description = "Medication Statement Dosage Timing"        
    _inherit = ["hc.basic.association", "hc.timing"]

    med_stmt_dosage_id = fields.Many2one(
        comodel_name="hc.med.stmt.dosage", 
        string="Dosage", 
        help="Dosage associated with this Medication Statement Dosage Timing.")                

class MedStmtIdentifier(models.Model):    
    _name = "hc.med.stmt.identifier"    
    _description = "Medication Statement Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    medication_statement_id = fields.Many2one(
        comodel_name="hc.res.medication.statement", 
        string="Medication Statement", 
        help="Medication Statement associated with this Medication Statement Identifier.")                

class MedStmtNote(models.Model):    
    _name = "hc.med.stmt.note"    
    _description = "Medication Statement Note"        
    _inherit = ["hc.basic.association", "hc.annotation"]

    medication_statement_id = fields.Many2one(
        comodel_name="hc.res.medication.statement", 
        string="Medication Statement", 
        help="Medication Statement associated with this Medication Statement Note.")                

class MedStmtSupportingInformation(models.Model):    
    _name = "hc.med.stmt.supporting.information"    
    _description = "Medication Statement Supporting Information"        
    _inherit = ["hc.basic.association"]

    medication_statement_id = fields.Many2one(
        comodel_name="hc.res.medication.statement", 
        string="Medication Statement", 
        help="Medication Statement associated with this Medication Statement Supporting Information.")                
    supporting_information_type = fields.Selection(
        string="Supporting Information Type", 
        selection=[
            ("string", "String"), 
            ("Medication Request", "Medication Request")], 
        help="Type of amount of medication per dose.")                
    supporting_information_name = fields.Char(
        string="Supporting Information", 
        compute="_compute_supporting_information_name", 
        store="True", 
        help="Additional supporting information.")                
    supporting_information_string = fields.Char(
        string="Supporting Information String", 
        help="Supporting Information String associated with this Medication Statement Supporting Information.")                
    supporting_information_medication_Request_id = fields.Many2one(
        comodel_name="hc.res.medication.request", 
        string="Supporting Information Medication Request", 
        help="Supporting Information Medication Request associated with this Medication Statement Supporting Information.")                                           

class MedicationStatementCategory(models.Model):    
    _name = "hc.vs.medication.statement.category"    
    _description = "Medication Statement Category"        
    _inherit = ["hc.value.set.contains"]

class MedicationReasonNotTaken(models.Model):    
    _name = "hc.vs.medication.reason.not.taken"    
    _description = "Medication Reason Not Taken"        
    _inherit = ["hc.value.set.contains"]
