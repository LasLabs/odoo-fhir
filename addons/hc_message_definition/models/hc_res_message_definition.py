# -*- coding: utf-8 -*-

from openerp import models, fields, api

class MessageDefinition(models.Model):    
    _name = "hc.res.message.definition"    
    _description = "Message Definition"
    _rec_name = "title"

    url = fields.Char(
        string="URL", 
        help="Logical URI to reference this message definition (globally unique).")                        
    version = fields.Char(
        string="Version", 
        help="Business version of the message definition.")                        
    name = fields.Char(
        string="Name", 
        help="Name for this message definition (Computer friendly).")                        
    title = fields.Char(
        string="Title", 
        help="Name for this message definition (Human friendly).")                        
    status = fields.Selection(
        string="Status", 
        required="True", 
        selection=[
            ("draft", "Draft"), 
            ("active", "Active"), 
            ("retired", "Retired")], 
        help="The status of this message definition. Enables tracking the life-cycle of the content.")                        
    is_experimental = fields.Boolean(
        string="Experimental", 
        help="If for testing purposes, not real usage.")                        
    date = fields.Datetime(
        string="Date", 
        required="True", 
        help="Date this was last changed.")                        
    publisher = fields.Char(
        string="Publisher", 
        help="Name of the publisher (Organization or individual).")                        
    contact_ids = fields.One2many(
        comodel_name="hc.message.definition.contact", 
        inverse_name="message_definition_id", 
        string="Contacts", 
        help="Contact details for the publisher.")                        
    description = fields.Text(
        string="Description", 
        help="Natural language description of the message definition.")                        
    use_context_ids = fields.One2many(
        comodel_name="hc.message.definition.use.context", 
        inverse_name="message_definition_id", 
        string="Use Contexts", 
        help="Content intends to support these contexts.")                        
    jurisdiction_ids = fields.Many2many(
        comodel_name="hc.vs.jurisdiction", 
        relation="message_definition_jurisdiction_rel", 
        string="Jurisdictions", 
        help="Intended jurisdiction for message definition (if applicable).")                        
    purpose = fields.Text(
        string="Purpose", 
        help="Why this message definition is defined.")                        
    copyright = fields.Text(
        string="Copyright", 
        help="Use and/or publishing restrictions.")                        
    base_id = fields.Many2one(
        comodel_name="hc.res.message.definition", 
        string="Base", 
        help="Definition this one is based on.")                        
    parent_ids = fields.One2many(
        comodel_name="hc.message.definition.parent", 
        inverse_name="message_definition_id", 
        string="Parents", 
        help="Protocol/workflow this is part of.")                        
    replaces_ids = fields.One2many(
        comodel_name="hc.message.definition.replaces", 
        inverse_name="message_definition_id", 
        string="Replaces", 
        help="Takes the place of.")                        
    event_id = fields.Many2one(
        comodel_name="hc.vs.message.event", 
        string="Event", 
        required="True", 
        help="Event type.")                        
    category = fields.Selection(
        string="Category", 
        selection=[
            ("consequence", "Consequence"), 
            ("currency", "Currency"), 
            ("notification", "Notification")], 
        help="The impact of the content of the message.")                        
    is_response_required = fields.Boolean(
        string="Response Required", 
        help="Is a response required?")                        
    focus_ids = fields.One2many(
        comodel_name="hc.message.definition.focus", 
        inverse_name="message_definition_id", 
        string="Focus", 
        help="Resource(s) that are the subject of the event.")                        
    allowed_message_ids = fields.One2many(
        comodel_name="hc.message.definition.allowed.response", 
        inverse_name="message_definition_id", 
        string="Allowed Message", 
        help="Responses to this message.")                        

class MessageDefinitionFocus(models.Model):    
    _name = "hc.message.definition.focus"
    _description = "Message Definition Focus"                

    message_definition_id = fields.Many2one(
        comodel_name="hc.res.message.definition", 
        string="Message Definition", 
        help="Message Definition associated with this Message Definition Focus.")
    code_id = fields.Many2one(
        comodel_name="hc.vs.resource.type", 
        string="Code", 
        required="True", 
        help="Type of resource.")                        
    profile_id = fields.Many2one(
        comodel_name="hc.res.structure.definition", 
        string="Profile", 
        help="Profile that must be adhered to by focus.")                        
    min = fields.Integer(
        string="Min", 
        help="Minimum number of focuses of this type.")                        
    max = fields.Char(
        string="Max", 
        help="Maximum number of focuses of this type.")                        

class MessageDefinitionAllowedResponse(models.Model):    
    _name = "hc.message.definition.allowed.response"    
    _description = "Message Definition Allowed Response"                

    message_definition_id = fields.Many2one(
        comodel_name="hc.res.message.definition", 
        string="Message Definition", 
        help="Message Definition associated with this Message Definition Allowed Response.")                        
    message_id = fields.Many2one(
        comodel_name="hc.res.message.definition", 
        string="Message", 
        required="True", 
        help="MessageDefinition for response.")                        
    situation = fields.Text(
        string="Situation", 
        help="When should this response be used.")                        

class MessageDefinitionContact(models.Model):    
    _name = "hc.message.definition.contact"    
    _description = "Message Definition Contact"            
    _inherit = ["hc.basic.association"]    
    _inherits = {"hc.contact.detail": "contact_id"}

    contact_id = fields.Many2one(
        comodel_name="hc.contact.detail", 
        string="Contact", 
        ondelete="restrict", 
        required="True", 
        help="Contact Detail associated with this Message Definition Contact.")                        
    message_definition_id = fields.Many2one(
        comodel_name="hc.res.message.definition", 
        string="Message Definition", 
        help="Message Definition associated with this Message Definition Contact.")                        

class MessageDefinitionUseContext(models.Model):    
    _name = "hc.message.definition.use.context"    
    _description = "Message Definition Use Context"            
    _inherit = ["hc.basic.association", "hc.usage.context"]    

    message_definition_id = fields.Many2one(
        comodel_name="hc.res.message.definition", 
        string="Message Definition", 
        help="Message Definition associated with this Message Definition Use Context.")                        

class MessageDefinitionParent(models.Model):    
    _name = "hc.message.definition.parent"    
    _description = "Message Definition Parent"            
    _inherit = ["hc.basic.association"]    

    message_definition_id = fields.Many2one(
        comodel_name="hc.res.message.definition", 
        string="Message Definition", 
        help="Message Definition associated with this Message Definition Parent.")                        
    parent_type = fields.Selection(
        string="Parent Type", 
        selection=[
            ("activity definition", "Activity Definition"), 
            ("plan definition", "Plan Definition")], 
        help="Type of protocol/workflow this is part of.")                        
    parent_name = fields.Char(
        string="Parent", 
        compute="_compute_parent_name", 
        store="True", 
        help="Protocol/workflow this is part of.")                        
    parent_activity_definition_id = fields.Many2one(
        comodel_name="hc.res.activity.definition", 
        string="Parent Activity Definition", 
        help="Activity Definition protocol/workflow this is part of.")                        
    parent_plan_definition_id = fields.Many2one(
        comodel_name="hc.res.plan.definition", 
        string="Parent Plan Definition", 
        help="Plan Definition protocol/workflow this is part of.")                        

class MessageDefinitionReplaces(models.Model):    
    _name = "hc.message.definition.replaces"    
    _description = "Message Definition Replaces"            
    _inherit = ["hc.basic.association"]    

    message_definition_id = fields.Many2one(
        comodel_name="hc.res.message.definition", 
        string="Message Definition", 
        help="Message Definition associated with this Message Definition Replaces.")                        
    replaces_id = fields.Many2one(
        comodel_name="hc.res.message.definition", 
        string="Replaces", 
        help="Message Definition associated with this Message Definition Replaces.")                        
