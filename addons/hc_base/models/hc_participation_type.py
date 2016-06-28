# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ParticipationType(models.Model): 
    _name = "hc.vs.participation.type" 
    _description = "Participation Type"
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this participation type (e.g., admitter).")
    code = fields.Char(
        string="Code", 
        help="Code of this participation type (e.g., ADM).")
    parent_id = fields.Many2one(
    	comodel_name="hc.vs.participation.type", 
    	string="Parent",
    	help="Parent concept.")
