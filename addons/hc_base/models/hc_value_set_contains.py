# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ValueSetContains(models.AbstractModel):

    _name = "hc.value.set.contains"
    _description = "Value Set Contains"
    _order = "code"

    system = fields.Char(
        string="Source URL",
        help="Web address of the source of the code.")
    is_abstract = fields.Boolean(
        string="Abstract", 
        help="If user cannot select this entry.")
    version = fields.Char(
        string="Version", 
        help="Version in which this code / display is defined.")
    code = fields.Char(
        string="Code", 
        help="Code - if blank, this is not a choosable code.")
    name = fields.Char(
        string="Name", 
        help="User display for the concept.")
    level = fields.Integer(
        string="Level", 
        help="Level in a hierarchy of codes.")
    source_id = fields.Many2one(
        comodel_name="res.partner", 
        string="Source", 
        help="The source of the definition of the code.")
    definition = fields.Text(
        string="Definition", 
        help="An explanation of the meaning of the concept.")
    comments = fields.Text(
        string="Comments", 
        help="Additional notes about how to use the code.")

    # _sql_constraints = [
    #     ('code_unique',
    #     'UNIQUE(code)',
    #     "The concept code must be unique.")
    #     ]


    # @api.one
    # @api.constrains('name', 'description')
    # def _check_description(self):
    #     if self.name == self.description:
    #         raise ValidationError("Concept name and description must be different")


class BasicAssociation(models.AbstractModel):   
    _name = "hc.basic.association"  
    _description = "Basic Association"
    
    is_active = fields.Boolean(
        string="Active", 
        default=True, 
        help="Whether this record is in active use.")      
    is_preferred = fields.Boolean(
        string="Preferred", 
        help="Record preference indicator.")        
    start_date = fields.Datetime(
        string="Start Date", 
        help="Start of the period during which this record is valid.")        
    end_date = fields.Datetime(
        string="End Date", 
        help="End of the period during which this record is valid.")     