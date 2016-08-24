# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Substance(models.Model):    
    _name = "hc.res.substance"    
    _description = "Substance"        

    identifier_ids = fields.One2many(
        comodel_name="hc.substance.identifier", 
        inverse_name="substance_id", 
        string="Identifier", 
        help="Unique identifier.")                
    category_ids = fields.Many2many(
        comodel_name="hc.vs.substance.category", 
        string="Category", 
        help="What class/type of substance this is.")                
    code_id = fields.Many2one(
        comodel_name="hc.vs.substance.code", 
        string="Code", 
        required="True", 
        help="What substance this is.")                
    description = fields.Text(
        string="Description", 
        help="Textual description of the substance, comments.")                

class SubstanceInstance(models.Model):    
    _name = "hc.substance.instance"    
    _description = "Substance Instance"        

    substance_id = fields.Many2one(
        comodel_name="hc.res.substance", 
        string="Substance", 
        help="Substance associated with this Instance.")                
    identifier_id = fields.Many2one(
        comodel_name="hc.substance.package.identifier", 
        string="Identifier", 
        help="Identifier of the package/container.")
    expiry = fields.Datetime(
        string="Expiry Date", 
        help="When no longer valid to use.")                
    quantity = fields.Float(
        string="Quantity", 
        help="Amount of substance in the package.")                

class SubstanceIngredient(models.Model):    
    _name = "hc.substance.ingredient"   
    _description = "Substance Ingredient"       

    substance_id = fields.Many2one(
        comodel_name="hc.res.substance", 
        string="Substance", 
        help="Substance associated with this Ingredient.")              
    quantity_ratio = fields.Float(
        string="Quantity Ratio", 
        compute="compute_quantity_ratio", 
        help="Ratio of optional amount (concentration) .")             
    quantity_numerator = fields.Float(
        string="Quantity Numerator", 
        help="Numerator value of optional amount (concentration).")              
    quantity_denominator = fields.Float(
        string="Quantity Denominator", 
        help="Denominator value of optional amount (concentration).")                
    substance_type = fields.Selection(
        string="Substance Type", 
        required="True", 
        selection=[
            ("Codeable Concept", "Codeable Concept"), 
            ("Substance", "Substance")], 
        help="Type of component of the substance.")               
    substance_name = fields.Char(
        string="Substance", 
        compute="compute_substance_name", 
        required="True", 
        help="A component of the substance.")              
    substance_code_id = fields.Many2one(
        comodel_name="hc.vs.substance.code", 
        string="Substance Code", 
        required="True", 
        help="Code of the component of the substance.")              
    substance_component_id = fields.Many2one(
        comodel_name="hc.res.substance", 
        string="Substance Component", 
        required="True", 
        help="Substance component of the substance.")              

class SubstanceIdentifier(models.Model):    
    _name = "hc.substance.identifier"    
    _description = "Substance Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    substance_id = fields.Many2one(
        comodel_name="hc.res.substance", 
        string="Substance", 
        help="Substance associated with this identifier.")                

class SubstancePackageIdentifier(models.Model):    
    _name = "hc.substance.package.identifier"    
    _description = "Substance Package Identifier"        
    _inherit = ["hc.identifier"]

class SubstanceCode(models.Model):    
    _name = "hc.vs.substance.code"    
    _description = "Substance Code"        

class SubstanceCategory(models.Model):    
    _name = "hc.vs.substance.category"    
    _description = "Substance Category"        
    _inherit = ["hc.value.set.contains"]
