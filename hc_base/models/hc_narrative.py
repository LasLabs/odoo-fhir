# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Narrative(models.Model):    
    _name = "hc.narrative"    
    _description = "Narrative"

    status = fields.Selection(
    	string="Narrative Status", 
    	required="True", 
    	selection=[
    		("generated", "Generated"), 
    		("extensions", "Extensions"), 
    		("additional", "Additional"), 
    		("empty", "Empty")], 
    	help="Indicates whether the account is presently used/useable or not.")        
    div = fields.Text(
    	string="Div", 
    	help=" Limited xhtml content.")        
