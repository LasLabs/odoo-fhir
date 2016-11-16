# -*- coding: utf-8 -*-

from openerp import models, fields, api

class MedicationDispense(models.Model): 
    _name = "hc.res.medication.dispense"    
    _description = "Medication Dispense"        

    identifier_id = fields.Many2one(
        comodel_name="hc.medication.dispense.identifier", 
        string="Identifier", 
        help="External identifier.")             
    status = fields.Selection(
        string="Medication Dispense Status", 
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
            ("code", "Code"), 
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
    medication_medication_id = fields.Many2one(
        comodel_name="hc.res.medication", 
        string="Medication", 
        help="What medication was supplied.")              
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Who the dispense is for.")              
    supporting_information_ids = fields.One2many(
        comodel_name="hc.medication.dispense.supporting.information", 
        inverse_name="medication_dispense_id", 
        string="Supporting Informations", 
        help="Information that supports the dispensing of the medication.")             
    dispenser_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Dispenser", 
        help="Practitioner responsible for dispensing medication.")              
    dispensing_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Dispensing Organization", 
        help="Organization responsible for the dispense of the medication.")             
    authorizing_prescription_ids = fields.One2many(
        comodel_name="hc.medication.dispense.authorizing.prescription", 
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
    days_supply = fields.Float(
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
        comodel_name="hc.medication.dispense.receiver", 
        inverse_name="medication_dispense_id", 
        string="Receivers", 
        help="Who collected the medication.")             
    note_ids = fields.One2many(
        comodel_name="hc.medication.dispense.note", 
        inverse_name="medication_dispense_id", 
        string="Notes", 
        help="Information about the dispense.")               
    dosage_instruction_ids = fields.One2many(
        comodel_name="hc.medication.dispense.dosage.instruction", 
        inverse_name="medication_dispense_id", 
        string="Dosage Instructions", 
        help="Medicine administration instructions to the patient/caregiver.")              
    event_history_ids = fields.One2many(
        comodel_name="hc.medication.dispense.event.history", 
        inverse_name="medication_dispense_id", 
        string="Event Histories", 
        help="A list of events of interest in the lifecycle.")                
    substitution_ids = fields.One2many(
        comodel_name="hc.medication.dispense.substitution", 
        inverse_name="medication_dispense_id", 
        string="Substitutions", 
        help="Deals with substitution of one medicine for another.")              

class MedicationDispenseSubstitution(models.Model): 
    _name = "hc.medication.dispense.substitution"   
    _description = "Medication Dispense Substitution"       

    medication_dispense_id = fields.Many2one(
        comodel_name="hc.res.medication.dispense", 
        string="Medication Dispense", 
        help="Medication Dispense associated with this Medication Dispense Substitution.")                
    type_id = fields.Many2one(
        comodel_name="hc.vs.substance.admin.substitution.code", 
        string="Type", 
        required="True", 
        help="Code signifying whether a different drug was dispensed from what was prescribed.")              
    reason_ids = fields.Many2many(
        comodel_name="hc.vs.substance.admin.substitution.reason", 
        relation="medication_dispense_substitution_reason_rel", 
        string="Reasons", help="Why was substitution made.")                
    responsible_party_ids = fields.One2many(
        comodel_name="hc.medication.dispense.substitution.responsible.party", 
        inverse_name="substitution_id", 
        string="Responsible Parties", 
        help="Who is responsible for the substitution.")                

class MedicationDispenseIdentifier(models.Model):   
    _name = "hc.medication.dispense.identifier" 
    _description = "Medication Dispense Identifier"     
    _inherit = ["hc.basic.association", "hc.identifier"]

class MedicationDispenseSupportingInformation(models.Model):    
    _name = "hc.medication.dispense.supporting.information" 
    _description = "Medication Dispense Supporting Information"     
    _inherit = ["hc.basic.association"]

    medication_dispense_id = fields.Many2one(
        comodel_name="hc.res.medication.dispense", 
        string="Medication Dispense", 
        help="Medication Dispense associated with this Medication Dispense Note.")                
    supporting_information_type = fields.Selection(
        string="Supporting Information Type", 
        selection=[
            ("string", "String"), 
            ("code", "Code")], 
        help="Type of information that supports the dispensing of the medication.")                
    supporting_information_name = fields.Char(
        string="Supporting Information", 
        compute="_compute_supporting_information_name", 
        store="True", 
        help="Information that supports the dispensing of the medication.")                
    supporting_info_string = fields.Char(
        string="Supporting Info String", 
        help="String of information that supports the dispensing of the medication.")             
    supporting_information_code_id = fields.Many2one(
        comodel_name="hc.vs.resource.type", 
        string="Supporting Information Code", 
        help="Type of resource of information that supports the dispensing of the medication.")              

class MedicationDispenseAuthorizingPrescription(models.Model):  
    _name = "hc.medication.dispense.authorizing.prescription"   
    _description = "Medication Dispense Authorizing Prescription"       
    _inherit = ["hc.basic.association"]

    medication_dispense_id = fields.Many2one(
        comodel_name="hc.res.medication.dispense", 
        string="Medication Dispense", 
        help="Medication Dispense associated with this Medication Dispense Authorizing Prescription.")                
    authorizing_prescription_id = fields.Many2one(
        comodel_name="hc.res.medication.request", 
        string="Authorizing Prescription", 
        help="Authorizing Prescription associated with this Medication Dispense Authorizing Prescription.")              

class MedicationDispenseReceiver(models.Model): 
    _name = "hc.medication.dispense.receiver"   
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

class MedicationDispenseNote(models.Model): 
    _name = "hc.medication.dispense.note"   
    _description = "Medication Dispense Note"       
    _inherit = ["hc.basic.association", "hc.annotation"]

    medication_dispense_id = fields.Many2one(
        comodel_name="hc.res.medication.dispense", 
        string="Medication Dispense", 
        help="Medication Dispense associated with this Medication Dispense Note.")                

class MedicationDispenseDosageInstruction(models.Model):    
    _name = "hc.medication.dispense.dosage.instruction" 
    _description = "Medication Dispense Dosage Instruction"     
    _inherit = ["hc.basic.association", "hc.dosage.instruction"]

    medication_dispense_id = fields.Many2one(
        comodel_name="hc.res.medication.dispense", 
        string="Medication Dispense", 
        help="Medication Dispense associated with this Medication Dispense Dosage Instruction.")             

class MedicationDispenseEventHistory(models.Model): 
    _name = "hc.medication.dispense.event.history"  
    _description = "Medication Dispense Event History"      
    _inherit = ["hc.basic.association"]

    medication_dispense_id = fields.Many2one(
        comodel_name="hc.res.medication.dispense", 
        string="Medication Dispense", 
        help="Medication Dispense associated with this Medication Dispense Event History.")               
    event_history_id = fields.Many2one(
        comodel_name="hc.res.provenance", 
        string="Event History", 
        help="Event History associated with this Medication Dispense Event History.")              

class MedicationDispenseSubstitutionResponsibleParty(models.Model): 
    _name = "hc.medication.dispense.substitution.responsible.party" 
    _description = "Medication Dispense Substitution Responsible Party"     
    _inherit = ["hc.basic.association"]

    substitution_id = fields.Many2one(
        comodel_name="hc.medication.dispense.substitution", 
        string="Substitution", 
        help="Substitution associated with this Medication Dispense Substitution Responsible Party.")              
    responsible_party_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Responsible Party", 
        help="Responsible Party associated with this Medication Dispense Substitution Responsible Party.")               

class MedicationDispenseType(models.Model): 
    _name = "hc.vs.medication.dispense.type"    
    _description = "Medication Dispense Type"       
    _inherit = ["hc.value.set.contains"]

class SubstanceAdminSubstitutionCode(models.Model): 
    _name = "hc.vs.substance.admin.substitution.code"   
    _description = "Substance Admin Substitution Code"      
    _inherit = ["hc.value.set.contains"]
