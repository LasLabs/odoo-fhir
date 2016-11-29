# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ElementDefinition(models.Model): 
    _name = "hc.element.definition"    
    _description = "Element Definition"

    name = fields.Char(
        string="Name", 
        help="Name for this element definition.")
