# -*- coding: utf-8 -*-

from openerp import models, fields, api

class RelatedResource(models.Model):	
    _name = "hc.related.resource"	
    _description = "Related Resource"		
    
    type = fields.Selection(string="Related Resource Type", 
        required="True", 
        selection=[
            ("documentation", "Documentation"), 
            ("justification", "Justification"), 
            ("citation", "Citation"), 
            ("predecessor", "Predecessor"), 
            ("successor", "Successor"), 
            ("derived-from", "Derived From"), 
            ("depends-on", "Depends On"), 
            ("composed-of", "Composed Of")], 
        help="The type of related resource.")				
    name = fields.Char(
        string="Display", 
        help="Brief description of the related resource.")				
    citation = fields.Char(
        string="Citation", 
        help="Bibliographic citation for the resource.")				
    url = fields.Char(
        string="URL", 
        help="URL for the related resource.")				
    document_id = fields.Many2one(
        comodel_name="hc.related.resource.document", 
        string="Document", 
        help="The related document.")
    resource_id = fields.Many2one(
        comodel_name="hc.vs.resource.list", 
        string="Resource", 
        help="The related resource.")		

class RelatedResourceDocument(models.Model):	
    _name = "hc.related.resource.document"	
    _description = "Related Resource Document"		
    _inherit = ["hc.basic.association", "hc.attachment"]

class ResourceList(models.Model):	
    _name = "hc.vs.resource.list"	
    _description = "Resource List"		
    _inherit = ["hc.value.set.contains"]
