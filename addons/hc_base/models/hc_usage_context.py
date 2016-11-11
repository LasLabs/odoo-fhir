# -*- coding: utf-8 -*-

from openerp import models, fields, api

class UsageContext(models.Model):    
    _name = "hc.usage.context"    
    _description = "Usage Context"        

    code_id = fields.Many2one(
        comodel_name="hc.vs.usage.context.type", 
        string="Code", 
        required="True", 
        help="Type of context being specified.")                
    action_type = fields.Selection(
        string="Action Type", 
        required="True", 
        selection=[
            ("code", "Code"), 
            ("Quantity", "Quantity"), 
            ("Range", "Range")], 
        help="Type of actions taken during assessment.")                
    value_name = fields.Char(
        string="Value", 
        compute="_compute_value_name", 
        store="True", 
        help="Value that defines the context.")                
    value_code_id = fields.Many2one(
        comodel_name="hc.vs.usage.context.value", 
        string="Value Code", 
        help="Value that defines the context.")                
    value_quantity = fields.Float(
        string="Value Quantity", 
        required="True", 
        help="Value that defines the context.")                
    value_quantity_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Value Quantity UOM", 
        help="Value quantity unit of measure.")                
    value_range_low = fields.Float(
        string="Value Range Low", 
        help="Low limit of value that defines the context.")                
    value_range_high = fields.Float(
        string="Value Range High", 
        help="High limit of value that defines the context.")                
    value_range_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Value Range UOM", 
        help="Value range unit of measure.")                

class UsageContextType(models.Model):    
    _name = "hc.vs.usage.context.type"    
    _description = "Usage Context Type"        
    _inherit = ["hc.value.set.contains"]

class UsageContextValue(models.Model):    
    _name = "hc.vs.usage.context.value"    
    _description = "Usage Context Value"        
    _inherit = ["hc.value.set.contains"]
