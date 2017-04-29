# -*- coding: utf-8 -*-

from openerp import models, fields, api

class MedicationOrder(models.Model):    
    _name = "hc.res.medication.order"    
    _description = "Medication Order"        

    identifier_ids = fields.One2many(
        comodel_name="hc.medication.order.identifier", 
        inverse_name="medication_order_id", 
        string="Identifiers", 
        help="External identifier.")                
    status = fields.Selection(
        string="Medication Order Status", 
        selection=[
            ("active", "Active"), 
            ("on-hold", "On-Hold"), 
            ("completed", "Completed"), 
            ("entered-in-error", "Entered-In-Error"), 
            ("stopped", "Stopped"), 
            ("superceded", "Superceded"), 
            ("draft", "Draft")], 
        help="A code specifying the state of the order. Generally this will be active or completed state.")                
    medication_type = fields.Selection(
        string="Medication Type", 
        selection=[
            ("Code", "Code"), 
            ("Medication", "Medication")], 
        help="Type of product to be supplied.")                
    medication_name = fields.Char(
        string="Medication", 
        compute="_compute_medication_name", 
        store="True", 
        help="Product to be supplied.")                
    medication_code_id = fields.Many2one(
        comodel_name="hc.vs.medication.code", 
        string="Medication Code", 
        help="Code of product to be supplied.")                
    medication_id = fields.Many2one(
        comodel_name="hc.res.medication", 
        string="Medication", 
        help="Medication product to be supplied.")                
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", help="Who prescription is for.")                
    encounter_id = fields.Many2one(
        comodel_name="hc.res.encounter", 
        string="Encounter", 
        help="Created during encounter / admission / stay.")                
    date_written = fields.Datetime(
        string="Date Written", 
        help="When prescription was authorized.")                
    prescriber_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Prescriber", 
        help="Who ordered the medication(s).")                
    reason_code_ids = fields.Many2many(
        comodel_name="hc.vs.condition.code", 
        string="Reason Codes", 
        help="Reason or indication for writing the prescription.")                
    reason_reference_ids = fields.One2many(
        comodel_name="hc.medication.order.reason.reference", 
        inverse_name="medication_order_id", 
        string="Reason References", 
        help="Condition that supports why the prescription is being written.")                
    note_ids = fields.One2many(
        comodel_name="hc.medication.order.note", 
        inverse_name="medication_order_id", 
        string="Notes", 
        help="Information about the prescription.")                
    category_id = fields.Many2one(
        comodel_name="hc.vs.medication.order.category", 
        string="Medication Order Category", 
        help="Type of medication usage.")                
    prior_prescription_id = fields.Many2one(
        comodel_name="hc.res.medication.order", 
        string="Prior Prescription", 
        help="An order/prescription that this supersedes.")                
    dosage_instruction_ids = fields.One2many(
        comodel_name="hc.medication.order.dosage.instruction", 
        inverse_name="medication_order_id", 
        string="Dosage Instructions", 
        help="How medication should be taken.")                
    dispense_request_ids = fields.One2many(
        comodel_name="hc.medication.order.dispense.request", 
        inverse_name="medication_order_id", 
        string="Dispense Requests", 
        help="Medication supply authorization.")                
    substitution_ids = fields.One2many(
        comodel_name="hc.medication.order.substitution", 
        inverse_name="medication_order_id", 
        string="Substitutions", 
        help="Any restrictions on medication substitution?.")                
    event_history_ids = fields.One2many(
        comodel_name="hc.medication.order.event.history", 
        inverse_name="medication_order_id", 
        string="Event Histories", 
        help="A list of events of interest in the lifecycle.")                

class MedicationOrderDosageInstruction(models.Model):    
    _name = "hc.medication.order.dosage.instruction"    
    _description = "Medication Order Dosage Instruction"        

    medication_order_id = fields.Many2one(
        comodel_name="hc.res.medication.order", 
        string="Medication Order", 
        help="Medication Order associated with this Medication Order Dosage Instruction.")                
    text = fields.Text(
        string="Text", 
        help="Dosage instructions expressed as text.")                
    additional_instruction_ids = fields.One2many(
        comodel_name="hc.med.order.dosage.instr.addl.instr", 
        inverse_name="dosage_instruction_id", 
        string="Additional Instructions", 
        help='Supplemental instructions - e.g. "with meals".')                
    timing_ids = fields.One2many(
        comodel_name="hc.med.order.dosage.instr.timing", 
        inverse_name="dosage_instruction_id", 
        string="Timings", 
        help="When medication should be administered.")                
    as_needed_type = fields.Selection(
        string="As Needed Type", 
        selection=[
            ("boolean", "Boolean"), 
            ("Code", "Code")], 
        help="Type of take as needed.")                
    as_needed_name = fields.Char(
        string="As Needed", 
        compute="_compute_as_needed_name", 
        store="True", 
        help="Take as needed.")                
    is_as_needed = fields.Boolean(
        string="As Needed", 
        help="Take as needed.")                
    as_needed_code_id = fields.Many2one(
        comodel_name="hc.vs.medication.as.needed.reason", 
        string="As Needed Code", 
        help="SNOMED CT Medication As Needed Reason Codes.")                
    site_type = fields.Selection(
        string="Site Type", 
        selection=[
            ("Code", "Code"), 
            ("Body Site", "Body Site")], 
        help="Type of body site to administer to.")
    site_name = fields.Char(
        string="Site", 
        compute="_compute_site_name", 
        store="True", 
        help="Body site to administer to.")
    site_code_id = fields.Many2one(
        comodel_name="hc.vs.approach.site.code", 
        string="Site Code", 
        help="Code of body site to administer to.")
    body_site_id = fields.Many2one(
        comodel_name="hc.res.body.site", 
        string="Body Site", 
        help="Body site to administer to.")
    route_id = fields.Many2one(
        comodel_name="hc.vs.route.code", 
        string="Route", 
        help="How drug should enter body.")                
    method_id = fields.Many2one(
        comodel_name="hc.vs.administration.method.code", 
        string="Method", 
        help="Technique for administering medication.")                
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
        help="Amount of medication per dose.")                
    dose_range_low = fields.Float(
        string="Dose Range Low", 
        help="Low limit of amount of medication per dose.")                
    dose_range_high = fields.Float(
        string="Dose Range High", 
        help="High limit of amount of medication per dose.")                
    dose = fields.Float(
        string="Dose", 
        help="Amount of medication per dose.")                
    dose_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Dose UOM", 
        help="Dose unit of measure.")                
    max_dose_quantity = fields.Float(
        string="Maximum Dose Quantity", 
        help="Numerator value of upper limit on medication per unit of time.")                
    max_dose_period = fields.Float(
        string="Maximum Dose Period", 
        help="Denominator value of upper limit on medication per unit of time.")                    
    max_dose_per_period = fields.Float(
        string="Maximum Dose per Period", 
        compute="_compute_max_dose_per_period", 
        store="True", 
        help="Upper limit on medication per unit of time.")                
    max_dose_per_period_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Maximum Dose per Period UOM", 
        help="Upper limit on medication per unit of time unit of measure.")                
    max_dose_per_administration = fields.Float(
        string="Maximum Dose per Administration", 
        help="Upper limit on medication per unit of time.")                
    max_dose_per_administration_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Max Dose Per Administration UOM", 
        help="Maximum dose per administration unit of measure.")                
    max_dose_per_lifetime = fields.Float(
        string="Maximum Dose per Lifetime", 
        help="Upper limit on medication per unit of time.")                
    max_dose_per_lifetime_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Max Dose Per Lifetime UOM", 
        help="Maximum dose per lifetime unit of measure.")                
    rate_type = fields.Selection(
        string="Rate Type", 
        selection=[
            ("Ratio", "Ratio"), 
            ("Range", "Range"), 
            ("Quantity", "Quantity")],
        help="Type of amount of medication per unit of time.")                
    rate_name = fields.Char(
        string="Rate", 
        compute="_compute_rate_name", 
        store="True", 
        help="Amount of medication per unit of time.")                
    dose_quantity = fields.Float(
        string="Dose Quantity", 
        help="Numerator value of amount of medication per unit of time.")                
    dose_period = fields.Float(
        string="Dose Period", 
        help="Denominator value of amount of medication per unit of time.")
    dose_period_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Dose Period UOM", 
        help="Dose period unit of measure.")                
    dose_rate = fields.Float(
        string="Dose Rate", 
        compute="_compute_dose_rate", 
        store="True", 
        help="Amount of medication per unit of time.")                
    dose_rate_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Dose Rate UOM", 
        help="Dose rate unit of measure.")                
    rate_range_low = fields.Float(
        string="Rate Range Low", 
        help="Low limit of amount of medication per unit of time.")                
    rate_range_high = fields.Float(
        string="Rate Range High", 
        help="High limit of amount of medication per unit of time.")                
    rate = fields.Float(
        string="Rate",
        help="Amount of medication per unit of time.")
    rate_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Rate UOM", 
        help="Rate unit of measure.")               

class MedicationOrderDispenseRequest(models.Model):    
    _name = "hc.medication.order.dispense.request"    
    _description = "Medication Order Dispense Request"        

    medication_order_id = fields.Many2one(
        comodel_name="hc.res.medication.order", 
        string="Medication Order", 
        help="Medication Order associated with this Medication Order Dispense Request.")                
    start_date = fields.Datetime(
        string="Start Date", 
        help="Start of the time period supply is authorized for.")                
    end_date = fields.Datetime(
        string="End Date", 
        help="End of the time period supply is authorized for.")                
    number_repeats_allowed = fields.Integer(
        string="Number Repeats Allowed", 
        help="# of refills authorized.")                
    quantity = fields.Float(
        string="Quantity", 
        help="Amount of medication to supply per dispense.")                
    quantity_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Quantity UOM", 
        help="Quantity unit of measure.")                
    expected_supply_duration = fields.Float(
        string="Expected Supply Duration", 
        help="Days supply per dispense.")                
    expected_supply_duration_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Expected Supply Duration UOM", 
        help="Days supply per dispense unit of measure." )                

class MedicationOrderSubstitution(models.Model):    
    _name = "hc.medication.order.substitution"    
    _description = "Medication Order Substitution"        

    medication_order_id = fields.Many2one(
        comodel_name="hc.res.medication.order", 
        string="Medication Order", 
        help="Medication Order associated with this Medication Order Substitution.")                
    allowed = fields.Boolean(
        string="Substitution Allowed", 
        required="True", 
        help="Whether substitution is allowed or not.")                
    reason_id = fields.Many2one(
        comodel_name="hc.vs.substance.admin.substitution.reason", 
        string="Reason", 
        help="Why should substitution (not) be made.")                

class MedicationOrderEventHistory(models.Model):    
    _name = "hc.medication.order.event.history"    
    _description = "Medication Order Event History"        

    medication_order_id = fields.Many2one(
        comodel_name="hc.res.medication.order", 
        string="Medication Order",  
        help="Medication Order associated with this Medication Order Event History.")                
    status = fields.Selection(
        string="Event History Status", 
        required="True", 
        selection=[
            ("active", "Active"), 
            ("on-hold", "On-Hold"), 
            ("completed", "Completed"), 
            ("entered-in-error", "Entered-In-Error"), 
            ("stopped", "Stopped"), 
            ("draft", "Draft")], 
        help="The status for the event.")
    action_id = fields.Many2one(
        comodel_name="hc.vs.medication.event.history.action", 
        string="Action", 
        help="Action taken (e.g. verify, discontinue).")                
    occurrence_date = fields.Datetime(
        string="Occurrence Date", 
        required="True", 
        help="The date at which the event happened.")                
    actor_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Actor", 
        help="Who took the action.")                
    reason_id = fields.Many2one(
        comodel_name="hc.vs.medication.event.history.reason", 
        string="Reason", 
        help="Reason the action was taken.")                

class MedicationOrderIdentifier(models.Model):    
    _name = "hc.medication.order.identifier"    
    _description = "Medication Order Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    medication_order_id = fields.Many2one(
        comodel_name="hc.res.medication.order", 
        string="Medication Order", 
        help="Medication Order associated with this Medication Order Identifier.")                

class MedicationOrderReasonReference(models.Model):    
    _name = "hc.medication.order.reason.reference"    
    _description = "Medication Order Reason Reference"        
    _inherit = ["hc.basic.association"]

    medication_order_id = fields.Many2one(
        comodel_name="hc.res.medication.order", 
        string="Medication Order", 
        help="Medication Order associated with this Medication Order Reason Reference.")                
    reason_reference_id = fields.Many2one(
        comodel_name="hc.res.condition", 
        string="Reason Reference", 
        help="Reason Reference associated with this Medication Order Reason Reference.")                

class MedicationOrderNote(models.Model):    
    _name = "hc.medication.order.note"    
    _description = "Medication Order Note"        
    _inherit = ["hc.basic.association", "hc.annotation"]

    medication_order_id = fields.Many2one(
        comodel_name="hc.res.medication.order", 
        string="Medication Order", 
        help="Medication Order associated with this Medication Order Note.")                

class MedOrderDosageInstrAddlInstr(models.Model):    
    _name = "hc.med.order.dosage.instr.addl.instr"    
    _description = "Medication Order Dosage Instruction Additional Instruction"        
    _inherit = ["hc.basic.association"]

    dosage_instruction_id = fields.Many2one(
        comodel_name="hc.medication.order.dosage.instruction", 
        string="Dosage Instruction", 
        help="Dosage Instruction associated with this Medication Order Dosage Instruction Additional Instruction.")                
    additional_instruction_type = fields.Selection(
        string="Dose Type", 
        selection=[
            ("string", "String"), 
            ("Code", "Code")], 
        help="Type of supplemental instructions.")          
    additional_instruction_name = fields.Char(
        string="Additional Instructions", 
        compute="_compute_additional_instruction_name", 
        store="True", 
        help='Supplemental instructions - e.g. "with meals".')         
    additional_instruction = fields.Char(
        string="Additional Instructions", 
        help="Text of supplemental instructions.")           
    additional_instruction_code_id = fields.Many2one(
        comodel_name="hc.vs.additional.instruction.code", 
        string="Additional Instructions Code", 
        help="Code of supplemental instructions.")

class MedOrderDosageInstrTiming(models.Model):    
    _name = "hc.med.order.dosage.instr.timing"    
    _description = "Medication Order Dosage Instruction Timing"       
    _inherit = ["hc.basic.association", "hc.timing"]

    dosage_instruction_id = fields.Many2one(
        comodel_name="hc.medication.order.dosage.instruction", 
        string="Dosage Instruction", 
        help="Dosage Instruction associated with this Medication Order Dosage Instruction Timing.")                

class MedicationEventHistoryReason(models.Model):    
    _name = "hc.vs.medication.event.history.reason"    
    _description = "Medication Event History Reason"        
    _inherit = ["hc.value.set.contains"]

class MedicationEventHistoryAction(models.Model):    
    _name = "hc.vs.medication.event.history.action"    
    _description = "Medication Event History Action"        
    _inherit = ["hc.value.set.contains"]

class MedicationOrderCategory(models.Model):    
    _name = "hc.vs.medication.order.category"    
    _description = "Medication Order Category"        
    _inherit = ["hc.value.set.contains"]

class SubstanceAdminSubstitutionReason(models.Model):    
    _name = "hc.vs.substance.admin.substitution.reason"    
    _description = "Substance Administration Substitution Reason"        
    _inherit = ["hc.value.set.contains"]
