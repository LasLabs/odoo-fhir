# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Resource(models.Model):    
    _name = "hc.resource"    
    _description = "Resource"        

    id = fields.Char(
        string="Id", 
        help="How the resource reference is interpreted when testing consent restrictions.")                
    meta_id = fields.Many2one(
        comodel_name="hc.resource.meta", 
        string="Meta", 
        help="Metadata about the resource.")                
    implicit_rules = fields.Char(
        string="Implicit Rules URI", 
        help="URL of a set of rules under which this content was created.")                
    language_id = fields.Many2one(
        comodel_name="hc.vs.language", 
        string="Language", 
        help="Language of the resource content.")                

class ResourceMeta(models.Model):    
    _name = "hc.resource.meta"    
    _description = "Resource Meta"        
    _inherit = ["hc.basic.association", "hc.meta"]
