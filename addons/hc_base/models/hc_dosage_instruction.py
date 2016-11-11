# -*- coding: utf-8 -*-

from openerp import models, fields, api

class DosageInstruction(models.Model):    
    _name = "hc.dosage.instruction"    
    _description = "Dosage Instruction"        

    sequence = fields.Integer(
        string="Sequence", 
        help="The order of the dosage instructions.")                
    text = fields.Text(
        string="Text", 
        help="Free text dosage instructions e.g. SIG.")                
    additional_instructions_ids = fields.Many2many(
        comodel_name="hc.vs.additional.instructions.code", 
        relation="dosage_instruction_additional_instructions_rel", 
        string="Additional Instructionss", 
        help='Supplemental instructions - e.g. "with meals".')             
    # timing_id = fields.Many2one(
    #     comodel_name="hc.dosage.instruction.timing", 
    #     string="Timing", help="When medication should be administered.")                
    action_type = fields.Selection(
        string="Action Type", 
        selection=[
            ("boolean", "Boolean"), 
            ("code", "Code")], 
        help="Type of actions taken during assessment.")                
    as_needed_name = fields.Char(
        string="As Needed", 
        compute="_compute_as_needed_name", 
        store="True", 
        help='Take "as needed" (for x).')                
    as_needed = fields.Boolean(
        string="As Needed", 
        help='Numerator value of take "as needed" (for x).')                
    as_needed_code_id = fields.Many2one(
        comodel_name="hc.vs.medication.as.needed.reason", 
        string="As Needed Code", 
        help='Code of take "as needed" (for x).')                
    action_type = fields.Selection(
        string="Action Type", 
        selection=[
            ("code", "Code"), 
            ("Body Site", "Body Site")], 
        help="Type of actions taken during assessment.")                
    site_name = fields.Char(
        string="Site", 
        compute="_compute_site_name", 
        store="True", 
        help="Body site to administer to.")                
    site_code_id = fields.Many2one(
        comodel_name="hc.vs.approach.site.code", 
        string="Site Code", 
        help="Body site to administer to.")                
    # site_body_site_id = fields.Many2one(
    #     comodel_name="hc.res.body.site", 
    #     string="Site Body Site", 
    #     help="Body Site content of this set of documents.")                
    route_id = fields.Many2one(
        comodel_name="hc.vs.route.code", 
        string="Route", 
        help="How drug should enter body.")                
    method_id = fields.Many2one(
        comodel_name="hc.vs.administration.method.code", 
        string="Method", 
        help="Technique for administering medication.")                
    action_type = fields.Selection(
        string="Action Type", 
        selection=[
            ("Range", "Range"), 
            ("Quantity", "Quantity")], 
        help="Type of actions taken during assessment.")                
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
    dose_quantity = fields.Float(
        string="Dose Quantity", 
        help="Amount of medication per dose.")                
    dose_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Dose UOM", 
        help="Dose unit of measure.")                
    max_dose_per_period_numerator = fields.Float(
        string="Max Dose Per Period Numerator", 
        help="Numerator value of upper limit on medication per unit of time.")                
    max_dose_per_period_numerator_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Max Dose Per Period Numerator UOM", 
        help="Max Dose Per Period Numerator unit of measure.")                
    max_dose_per_period_denominator = fields.Float(
        string="Max Dose Per Period Denominator", 
        help="Denominator value of upper limit on medication per unit of time.")                
    max_dose_per_period_denominator_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Max Dose Per Period Denominator UOM", 
        help="Max Dose Per Period Denominator unit of measure.")                
    max_dose_per_period_ratio = fields.Float(
        string="Max Dose Per Period Ratio", 
        compute="_compute_max_dose_per_period_ratio", 
        store="True", 
        help="Ratio of upper limit on medication per unit of time.")                
    max_dose_per_period_ratio_uom = fields.Char(
        string="Max Dose Per Period Ratio UOM", 
        compute="_compute_max_dose_per_period_ratio_uom", 
        store="True", 
        help="Max Dose Per Period Ratio unit of measure.")                
    max_dose_per_administration = fields.Float(
        string="Max Dose Per Administration", 
        help="Upper limit on medication per administration")                
    max_dose_per_administration_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Max Dose Per Administration UOM", 
        help="Max Dose Per Administration unit of measure.")                
    max_dose_per_lifetime = fields.Float(
        string="Max Dose Per Lifetime", 
        help="Upper limit on medication per lifetime of the patient")                
    max_dose_per_lifetime_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Max Dose Per Lifetime UOM", 
        help="Max Dose Per Lifetime unit of measure.")                
    action_type = fields.Selection(
        string="Action Type", 
        selection=[
            ("Ratio", "Ratio"), 
            ("Range", "Range"), 
            ("Quantity", "Quantity")], 
        help="Type of actions taken during assessment.")                
    rate_name = fields.Char(
        string="Rate", 
        compute="_compute_rate_name", 
        store="True", 
        help="Amount of medication per unit of time.")                
    rate_numerator = fields.Float(
        string="Rate Numerator", 
        help="Numerator value of amount of medication per unit of time.")                
    rate_numerator_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Rate Numerator UOM", 
        help="Rate Numerator unit of measure.")                
    rate_denominator = fields.Float(
        string="Rate Denominator", 
        help="Denominator value of amount of medication per unit of time.")                
    rate_denominator_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Rate Denominator UOM", 
        help="Rate Denominator unit of measure.")                
    rate_ratio = fields.Float(
        string="Rate Ratio", 
        compute="_compute_rate_ratio", 
        store="True", 
        help="Ratio of amount of medication per unit of time.")                
    rate_ratio_uom = fields.Char(
        string="Rate Ratio UOM", 
        compute="_compute_rate_ratio_uom", 
        store="True", help="Rate Ratio unit of measure.")                
    rate_range_low = fields.Float(
        string="Rate Range Low", 
        help="Low limit of amount of medication per unit of time.")                
    rate_range_high = fields.Float(
        string="Rate Range High", 
        help="High limit of amount of medication per unit of time.")                
    rate_quantity = fields.Float(
        string="Rate Quantity", 
        help="Amount of medication per unit of time.")                
    rate_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Rate UOM", 
        help="Rate unit of measure.")                

class AdditionalInstructionsCode(models.Model):    
    _name = "hc.vs.additional.instructions.code"    
    _description = "Additional Instructions Code"        
    _inherit = ["hc.value.set.contains"]

# class DosageInstructionTiming(models.Model):    
#     _name = "hc.dosage.instruction.timing"    
#     _description = "Dosage Instruction Timing"        
#     _inherit = ["hc.basic.association", "hc.timing"]
