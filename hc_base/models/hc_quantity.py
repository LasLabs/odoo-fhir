# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Quantity(models.AbstractModel):
    _name = "hc.quantity"    
    _description = "Quantity"

    value = fields.Float(
        string="Value", 
        help="Numerical value (with implicit precision).")
    comparator = fields.Selection(
        string="Quantity Comparator", 
        default="=", 
        selection=[
            ("=", "="), 
            ("<", "<"), 
            ("<=", "<="), 
            (">=", ">="), 
            (">", ">")], 
        help="How to understand the value.")
    unit_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Unit of Measure", 
        help="Unit representation.")
    system_uri = fields.Char(
        string="System URL", 
        help="System that defines coded unit form.")
    code = fields.Char(
        string="Code", 
        help="Coded form of the unit.")

# Constraints

# If a code for the unit is present, the system_uri SHALL also be present

class Age(models.Model):
    _name = "hc.age"    
    _description = "Age"
    _inherit = "hc.quantity"


# Rules

# There SHALL be a code if there is a value and it SHALL be an expression of time. 
# If system is present, it SHALL be UCUM. 
# If value is present, it SHALL be positive.

class Count(models.Model):
    _name = "hc.count"    
    _description = "Count"
    _inherit = "hc.quantity"

    value = fields.Integer(
        string="Count", 
        help="Count.")

# Rules

# There SHALL be a code with a value of "1" if there is a value and it SHALL be an expression of length. 
# If system is present, it SHALL be UCUM. 
# If present, the value SHALL a whole number.

class Distance(models.Model):
    _name = "hc.distance"    
    _description = "Distance"
    _inherit = "hc.quantity"

# Rules

# There SHALL be a code if there is a value and it SHALL be an expression of length. 
# If system is present, it SHALL be UCUM.

class Duration(models.Model):
    _name = "hc.duration"    
    _description = "Duration"
    _inherit = "hc.quantity"

# Rules

# There SHALL be a code if there is a value and it SHALL be an expression of time. 
# If system is present, it SHALL be UCUM.

class Money(models.Model):
    _name = "hc.money"    
    _description = "Money"
    _inherit = "hc.quantity"

# Rules

# There SHALL be a code if there is a value and it SHALL be an expression of currency. 
# If system is present, it SHALL be ISO 4217 (system = "urn:iso:std:iso:4217" - currency).

class SimpleQuantity(models.Model):
    _name = "hc.simple.quantity"    
    _description = "Simple Quantity"
    _inherit = "hc.quantity"

# Rules

# The comparator is not used on a SimpleQuantity.