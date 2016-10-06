# -*- coding: utf-8 -*-

from openerp import models, fields, api

class MedicationDispense(models.Model):    
    _name = "hc.res.medication.dispense"    
    _description = "Medication Dispense"        

    identifier_id = fields.Many2one(
        comodel_name="hc.med.disp.identifier", 
        string="Identifier", 
        help="External identifier.")             
    status = fields.Selection(string="Medication Dispense Status", 
        selection=[
            ("in-progress", "In-Progress"), 
            ("on-hold", "On-Hold"), 
            ("completed", "Completed"), 
            ("entered-in-error", "Entered-In-Error"), 
            ("stopped", "Stopped")], 
        help="A code specifying the state of the set of dispense events.")                
    medication_type = fields.Selection(
        string="Medication Type", 
        required="True", 
        selection=[
            ("Code", "Code"), 
            ("Medication", "Medication")], 
        help="Type of what medication was supplied.")                
    medication_name = fields.Char(
        string="Medication", 
        compute="_compute_medication_name", 
        store="True", 
        help="What medication was supplied.")                
    medication_code_id = fields.Many2one(
        comodel_name="hc.vs.medication.code", 
        string="Medication Code", 
        help="Code of what medication was supplied.")                
    medication_id = fields.Many2one(
        comodel_name="hc.res.medication", 
        string="Medication", 
        help="What medication was supplied.")                
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Who the dispense is for.")                
    dispenser_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Dispenser", 
        help="Practitioner responsible for dispensing medication.")                
    dispensing_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Dispensing Organization", 
        help="Organization responsible for the dispense of the medication.")                
    authorizing_prescription_ids = fields.One2many(
        comodel_name="hc.med.disp.authorizing.prescription", 
        inverse_name="medication_dispense_id", 
        string="Authorizing Prescriptions", 
        help="Medication order that authorizes the dispense.")                
    type_id = fields.Many2one(
        comodel_name="hc.vs.medication.dispense.type", 
        string="Type", 
        help="Trial fill, partial fill, emergency fill, etc.")                
    quantity = fields.Float(
        string="Quantity", 
        help="Amount dispensed.")                
    quantity_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Quantity UOM", 
        help="Quantity unit of measure.")                
    days_supply = fields.Integer(
        string="Days Supply", 
        help="Amount of medication expressed as a timing amount.")                
    when_prepared = fields.Datetime(
        string="When Prepared Date", 
        help="Dispense processing time.")                
    when_handed_over = fields.Datetime(
        string="When Handed Over Date", 
        help="Handover time.")                
    destination_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Destination", 
        help="Where the medication was sent.")                
    receiver_ids = fields.One2many(
        comodel_name="hc.med.disp.receiver", 
        inverse_name="medication_dispense_id", 
        string="Receivers", 
        help="Patient who collected the medication.")                
    note_ids = fields.One2many(
        comodel_name="hc.med.disp.note", 
        inverse_name="medication_dispense_id", 
        string="Notes", 
        help="Information about the dispense.")                
    dosage_instruction_ids = fields.One2many(
        comodel_name="hc.med.disp.dosage.instr", 
        inverse_name="medication_dispense_id", 
        string="Dosage Instructions", 
        help="Medicine administration instructions to the patient/carer.")                
    substitution_ids = fields.One2many(
        comodel_name="hc.med.disp.substitution", 
        inverse_name="medication_dispense_id", 
        string="Substitutions", 
        help="Deals with substitution of one medicine for another.")                
    event_history_ids = fields.One2many(
        comodel_name="hc.med.disp.event.history", 
        inverse_name="medication_dispense_id", 
        string="Event Histories", 
        help="A list of events of interest in the lifecycle.")                

class MedDispDosageInstr(models.Model):    
    _name = "hc.med.disp.dosage.instr"    
    _description = "Medication Dispense Dosage Instruction"        

    medication_dispense_id = fields.Many2one(
        comodel_name="hc.res.medication.dispense", 
        string="Medication Dispense", 
        help="Medication Dispense associated with this Medication Dispense Dosage Instruction.")                
    text = fields.Text(
        string="Text", 
        help="Dosage Instructions.")                
    additional_instruction_ids = fields.One2many(
        comodel_name="hc.med.disp.dosage.instr.addl.instr",
        inverse_name="dosage_instruction_id", 
        string="Additional Instructions", 
        help='Supplemental instructions - e.g. "with meals".')                
    timing_ids = fields.One2many(
        comodel_name="hc.med.disp.dosage.instr.timing", 
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
        help="Boolean take as needed.")                
    as_needed_code_id = fields.Many2one(
        comodel_name="hc.vs.medication.as.needed.reason", 
        string="As Needed Code", 
        help="SNOMED CT Medication As Needed Reason Codes.")                
    site_type = fields.Selection(
        string="Site Type", 
        selection=[
            ("Code", "Code"), 
            ("Body Site", "Body Site")], 
        help="Type of body Site to administer to.")                
    site_name = fields.Char(
        string="Site", 
        compute="_compute_site_name", 
        store="True", 
        help="Body Site to administer to.")                
    site_code_id = fields.Many2one(
        comodel_name="hc.vs.approach.site.code", 
        string="Site Code", 
        help="Code of body site to administer to.")                
    body_site_id = fields.Many2one(
        comodel_name="hc.res.body.site", 
        string="Body Site", 
        help="Body Site to administer to.")                
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
        help="Amount of medication per dose unit of measure.")                 
    rate_type = fields.Selection(
        string="Rate Type", 
        selection=[
            ("Ratio", "Ratio"),
            ("Range", "Range"), 
            ("Quantity", "Quantity")], 
        help="Type of amount of medication per dose.")                
    rate_name = fields.Char(
        string="Rate", 
        compute="_compute_rate_name", 
        store="True", 
        help="Amount of medication per unit of time.")                
    medication_quantity = fields.Float(
        string="Medication Quantity", 
        help="Numerator value of amount of medication per unit of time.")                
    medication_period = fields.Float(
        string="Medication Period", 
        help="Denominator value of amount of medication per unit of time.")
    medication_period_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Medication Period UOM", 
        help="Medication Period unit of measure.")                
    medication_rate = fields.Float(
        string="Medication Rate", 
        compute="_compute_medication_rate", 
        store="True", 
        help="Amount of medication per unit of time.")                
    medication_rate_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Medication Rate UOM", 
        help="Medication Rate unit of measure.")                
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
    max_dose_quantity_numerator = fields.Float(
        string="Maximum Dose Quantity", 
        help="Numerator value of upper limit on medication per unit of time.")                
    max_dose_period_numerator = fields.Float(
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

class MedDispSubstitution(models.Model):    
    _name = "hc.med.disp.substitution"    
    _description = "Medication Dispense Substitution"        

    medication_dispense_id = fields.Many2one(
        comodel_name="hc.res.medication.dispense", 
        string="Medication Dispense", 
        help="Medication Dispense associated with this Medication Dispense Substitution.")                
    type_id = fields.Many2one(
        comodel_name="hc.vs.medication.dispense.substitution.type", 
        string="Type", 
        required="True", 
        help="Code signifying whether a different drug was dispensed from what was prescribed.")                
    reason_ids = fields.One2many(
        comodel_name="hc.med.disp.subs.reason", 
        inverse_name="substitution_id", 
        string="Reasons", 
        help="Why was substitution made.")                
    responsible_party_ids = fields.One2many(
        comodel_name="hc.med.disp.subs.responsible.party", 
        inverse_name="substitution_id", 
        string="Responsible Parties", 
        help="Who is responsible for the substitution.")                

class MedDispEventHistory(models.Model):    
    _name = "hc.med.disp.event.history"    
    _description = "Medication Dispense Event History"        

    medication_dispense_id = fields.Many2one(
        comodel_name="hc.res.medication.dispense", 
        string="Medication Dispense", 
        help="Medication Dispense associated with this Medication Dispense Event History.")                
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

class MedDispDosageInstrAddlInstr(models.Model):    
    _name = "hc.med.disp.dosage.instr.addl.instr"   
    _description = "Medication Dispense Dosage Instruction Additional Instructions"
    _inherit = ["hc.basic.association"]

    dosage_instruction_id = fields.Many2one(
        comodel_name="hc.med.disp.dosage.instr", 
        string="Dosage Instruction", 
        help="Dosage Instruction associated with this Medication Dispense Dosage Instruction Additional Instructions.")           
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

class MedDispDosageInstrTiming(models.Model):    
    _name = "hc.med.disp.dosage.instr.timing"    
    _description = "Medication Dispense Dosage Instruction Timing"        
    _inherit = ["hc.basic.association", "hc.timing"]

    dosage_instruction_id = fields.Many2one(
        comodel_name="hc.med.disp.dosage.instr", 
        string="Dosage Instruction", 
        help="Dosage Instruction associated with this Medication Dispense Dosage Instruction Timing.")                

class MedDispIdentifier(models.Model):    
    _name = "hc.med.disp.identifier"    
    _description = "Medication Dispense Identifier"        
    _inherit = ["hc.identifier"]

class MedDispAuthorizingPrescription(models.Model):    
    _name = "hc.med.disp.authorizing.prescription"    
    _description = "Medication Dispense Authorizing Prescription"        
    _inherit = ["hc.basic.association"]

    medication_dispense_id = fields.Many2one(
        comodel_name="hc.res.medication.dispense", 
        string="Medication Dispense", 
        help="Medication dispense associated with this Medication Dispense Authorizing Prescription.")
    authorizing_prescription_id = fields.Many2one(
        comodel_name="hc.res.medication.order", 
        string="Authorizing Prescription", 
        help="Authorizing Prescription associated with this Medication Dispense Authorizing Prescription.")                

class MedDispNote(models.Model):    
    _name = "hc.med.disp.note"    
    _description = "Medication Dispense Note"        
    _inherit = ["hc.basic.association", "hc.annotation"]

    medication_dispense_id = fields.Many2one(
        comodel_name="hc.res.medication.dispense", 
        string="Medication Dispense", 
        help="Medication Dispense associated with this Medication Dispense Note.")                

class MedDispReceiver(models.Model):    
    _name = "hc.med.disp.receiver"    
    _description = "Medication Dispense Receiver"        
    _inherit = ["hc.basic.association"]

    medication_dispense_id = fields.Many2one(
        comodel_name="hc.res.medication.dispense", 
        string="Medication Dispense", 
        help="Medication Dispense associated with this Medication Dispense Receiver.")                
    receiver_type = fields.Selection(
        string="Receiver Type", 
        selection=[
            ("Patient", "Patient"), 
            ("Practitioner", "Practitioner")], 
        help="Type of who collected the medication.")                
    receiver_name = fields.Char(
        string="Receiver", 
        compute="_compute_receiver_name", 
        store="True", 
        help="Who collected the medication.")                
    receiver_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Receiver Patient", 
        help="Patient who collected the medication.")                
    receiver_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Receiver Practitioner", 
        help="Practitioner who collected the medication.")                

class MedDispSubsReason(models.Model):    
    _name = "hc.med.disp.subs.reason"    
    _description = "Medication Dispense Substitution Reason"        
    _inherit = ["hc.basic.association"]

    substitution_id = fields.Many2one(
        comodel_name="hc.med.disp.substitution", 
        string="Substitution", 
        help="Substitution associated with this Medication Dispense Substitution Reason.")                
    reason_id = fields.Many2one(
        comodel_name="hc.vs.substance.admin.substitution.reason", 
        string="Reason", 
        help="Reason associated with this Medication Dispense Substitution Reason.")                

class MedDispSubsResponsibleParty(models.Model):    
    _name = "hc.med.disp.subs.responsible.party"    
    _description = "Medication Dispense Substitution Responsible Party"        
    _inherit = ["hc.basic.association"]

    substitution_id = fields.Many2one(
        comodel_name="hc.med.disp.substitution", 
        string="Substitution", 
        help="Substitution associated with this Medication Dispense Substitution Responsible Party.")                
    responsible_party_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Responsible Party", 
        help="Responsible Party associated with this Medication Dispense Substitution Responsible Party.")                

class MedicationDispenseSubstitutionType(models.Model):    
    _name = "hc.vs.medication.dispense.substitution.type"    
    _description = "Medication Dispense Substitution Type"        
    _inherit = ["hc.value.set.contains"]

class MedicationDispenseType(models.Model):    
    _name = "hc.vs.medication.dispense.type"    
    _description = "Medication Dispense Type"        
    _inherit = ["hc.value.set.contains"]
