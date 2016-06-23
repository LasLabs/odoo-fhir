# -*- coding: utf-8 -*-

from openerp import models, fields, api

class IdentifierType(models.Model): 
    _name = "hc.vs.identifier.type" 
    _description = "Identifier Type"
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Identifier Type Name", 
        help="Name of this identifier type (e.g., Driver's License Number).")
    code = fields.Char(
        string="Identifier Type Code", 
        help="Code of this identifier type (e.g., DL).")

class Identifier(models.Model):
    _name = "hc.identifier"
    _description = "Identifier"

    name = fields.Char(
        string="Name", 
        help="Name of this identifier (e.g., CA Driver's License Number).")
    code = fields.Char(
        string="Code", 
        help="Code of this identifier (e.g., CA DL).")
    use = fields.Selection(
        string="Identifier Use", 
        selection=[
            ("usual", "Usual"), 
            ("official", "Official"), 
            ("temp", "Temporary"), 
            ("secondary", "Secondary")], 
        help="The purpose of this identifier record.")
    definition = fields.Char(
        string="Definition", 
        help="An explanation of the meaning of the identifier.")
    type_id = fields.Many2one(
        comodel_name="hc.vs.identifier.type", 
        string="Type", 
        help="Description of identifier.")
    system = fields.Char(
        string="Source URL", 
        help="Web address of the source of the code.")
    value = fields.Char(
        string="Value", 
        help="Value of this identifier record.")
    # assigner_organization_id = fields.Many2one(
    #     comodel_name="hc.res.organization", 
    #     string="Identifier Assigner Organization", 
    #     help="Organization that issued id (may be just text).")
    country_id = fields.Many2one(
        comodel_name="res.country", 
        string="Country", 
        help="Country associated with the identifier.")


