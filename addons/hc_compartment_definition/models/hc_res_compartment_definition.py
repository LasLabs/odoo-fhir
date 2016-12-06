# -*- coding: utf-8 -*-

from openerp import models, fields, api

class CompartmentDefinition(models.Model):    
    _name = "hc.res.compartment.definition"    
    _description = "Compartment Definition"
    _rec_name = "title"                

    url = fields.Char(
        string="URI", 
        required="True", 
        help="Absolute URL used to reference this compartment definition.")
    name = fields.Char(
        string="Name", 
        required="True", 
        help="Informal name for this compartment definition.")                       
    title = fields.Char(
        string="Title", 
        help="Name for this compartment definition (Human friendly).")                        
    status = fields.Selection(
        string="Status", 
        selection=[
            ("draft", "Draft"), 
            ("active", "Active"), 
            ("retired", "Retired")], 
        help="The status of this message definition. Enables tracking the life-cycle of the content.")                        
    is_experimental = fields.Boolean(
        string="Experimental", 
        help="If for testing purposes, not real usage.")
    publisher = fields.Char(
        string="Publisher", 
        help="Name of the publisher (Organization or individual).")                  
    contact_ids = fields.One2many(
        comodel_name="hc.compartment.definition.contact", 
        inverse_name="compartment_definition_id", 
        string="Contacts", 
        help="Contact details for the publisher.")                        
    date = fields.Datetime(
        string="Date", 
        help="Publication Date(/time).")                        
    description = fields.Text(
        string="Description", 
        help="Natural language description of the CompartmentDefinition.")   
    purpose = fields.Text(
        string="Purpose", 
        help="Why this compartment definition is defined.")                  
    use_context_ids = fields.One2many(
        comodel_name="hc.compartment.definition.use.context", 
        inverse_name="compartment_definition_id", 
        string="Use Contexts", 
        help="Content intends to support these contexts.")                        
    jurisdiction_ids = fields.Many2many(
        comodel_name="hc.vs.jurisdiction", 
        relation="compartment_definition_jurisdiction_rel", 
        string="Jurisdictions", 
        help="Intended jurisdiction for compartment definition (if applicable).")                        
    code = fields.Selection(
        string="Code", 
        required="True", 
        selection=[
            ("patient", "Patient"), 
            ("encounter", "Encounter"), 
            ("related person", "Related Person"), 
            ("practitioner", "Practitioner"), 
            ("Device", "Device")], 
        help="Which compartment this definition describes.")                        
    search = fields.Boolean(
        string="Search", 
        required="True", 
        help="Whether the search syntax is supported.")                        
    resource_ids = fields.One2many(
        comodel_name="hc.compartment.definition.resource", 
        inverse_name="compartment_definition_id", 
        string="Software", 
        help="How resource is related to the compartment.")                        

class CompartmentDefinitionResource(models.Model):    
    _name = "hc.compartment.definition.resource"    
    _description = "Compartment Definition Resource"                

    compartment_definition_id = fields.Many2one(
        comodel_name="hc.res.compartment.definition", 
        string="Compartment Definition", 
        help="Compartment Definition associated with this Compartment Definition Resource.")                        
    code_id = fields.Many2one(
        comodel_name="hc.vs.resource.type", 
        string="Code", 
        required="True", 
        help="Name of resource type.")                        
    param_ids = fields.One2many(
        comodel_name="hc.compartment.definition.resource.param", 
        inverse_name="resource_id", 
        string="Params", 
        help="Search Parameter Name, or chained params.")                        
    documentation = fields.Text(
        string="Documentation", 
        help="Additional documentation about the resource and compartment.")

class CompartmentDefinitionContact(models.Model):    
    _name = "hc.compartment.definition.contact"    
    _description = "Compartment Definition Contact"            
    _inherit = ["hc.basic.association"]    
    _inherits = {"hc.contact.detail": "contact_id"}

    contact_id = fields.Many2one(
        comodel_name="hc.contact.detail", 
        string="Contact", 
        ondelete="restrict", 
        required="True", help="Contact Detail associated with this Compartment Definition Contact.")                        
    compartment_definition_id = fields.Many2one(
        comodel_name="hc.res.compartment.definition", 
        string="Compartment Definition", 
        help="Compartment Definition associated with this Compartment Definition Contact.")                        

class CompartmentDefinitionUseContext(models.Model):    
    _name = "hc.compartment.definition.use.context"    
    _description = "Compartment Definition Use Context"            
    _inherit = ["hc.basic.association", "hc.usage.context"]    

    compartment_definition_id = fields.Many2one(
        comodel_name="hc.res.compartment.definition", 
        string="Compartment Definition", 
        help="Compartment Definition associated with this Compartment Definition Use Context.")                        

class CompartmentDefinitionResourceParam(models.Model):    
    _name = "hc.compartment.definition.resource.param"    
    _description = "Compartment Definition Resource Param"            
    _inherit = ["hc.basic.association"]    

    resource_id = fields.Many2one(
        comodel_name="hc.compartment.definition.resource", 
        string="Resource", 
        help="Resource associated with this Compartment Definition Resource Param.")                        
    param = fields.Char(
        string="Param", 
        help="Param associated with this Compartment Definition Resource Param.")                        
