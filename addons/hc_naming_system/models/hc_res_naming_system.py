# -*- coding: utf-8 -*-

from openerp import models, fields, api

class NamingSystem(models.Model):    
    _name = "hc.res.naming.system"    
    _description = "Naming System"                

    name = fields.Char(
        string="Name", 
        required="True", help="Human-readable label.")                        
    status = fields.Selection(
        string="Status", 
        required="True", 
        selection=[
            ("draft", "Draft"), 
            ("active", "Active"), 
            ("retired", "Retired")], 
        help="The status of this naming system. Enables tracking the life-cycle of the content.")                        
    kind = fields.Selection(
        string="Kind", 
        required="True", 
        selection=[
            ("codesystem", "Code System"), 
            ("identifier", "Identifier"), 
            ("root", "Root")], 
        help="Indicates the purpose for the naming system - what kinds of things does it make unique?")                        
    date = fields.Datetime(
        string="Date", 
        required="True", 
        help="Publication Date(/time).")                        
    publisher = fields.Char(
        string="Publisher", 
        help="Name of the publisher (Organization or individual).")                        
    contact_ids = fields.One2many(
        comodel_name="hc.naming.system.contact", 
        inverse_name="naming_system_id", 
        string="Contacts", 
        help="Contact details for the publisher.")                        
    responsible = fields.Char(
        string="Responsible", 
        help="Who maintains system namespace?")                        
    type = fields.Many2one(
        comodel_name="hc.vs.identifier.type", 
        string="Type", 
        help="e.g. driver, provider, patient, bank etc.")                        
    description = fields.Text(
        string="Description", 
        help="What does namingsystem identify?")                        
    use_context_ids = fields.One2many(
        comodel_name="hc.naming.system.use.context", 
        inverse_name="naming_system_id", 
        string="Use Contexts", 
        help="Content intends to support these contexts.")                        
    jurisdiction_ids = fields.Many2many(
        comodel_name="hc.vs.jurisdiction", 
        relation="naming_system_jurisdiction_rel", 
        string="Jurisdictions", 
        help="Intended jurisdiction for naming system (if applicable).")                        
    usage = fields.Text(
        string="Usage", 
        help="How/where is it used.")                        
    replaced_by_id = fields.Many2one(
        comodel_name="hc.res.naming.system", 
        string="Replaced By", 
        help="Use this instead.")                        
    unique_id_ids = fields.One2many(
        comodel_name="hc.naming.system.unique.id", 
        inverse_name="naming_system_id", 
        string="Unique Id", 
        required="True", 
        help="Unique identifiers used for system.")                        

class NamingSystemUniqueId(models.Model):    
    _name = "hc.naming.system.unique.id"    
    _description = "Naming System Unique Id"                

    naming_system_id = fields.Many2one(
        comodel_name="hc.res.naming.system", 
        string="Naming System", 
        help="Naming System associated with this Naming System Unique Id.")                        
    type = fields.Selection(
        string="Type", 
        required="True", 
        selection=[
            ("oid", "OID"), 
            ("uuid", "UUID"), 
            ("uri", "URI"), 
            ("other", "Other")], 
        help="Categorizes a naming system for easier search by grouping related naming systems.")                        
    value = fields.Char(
        string="Value", 
        required="True", 
        help="The unique identifier.")                        
    is_preferred = fields.Boolean(
        string="Preferred", 
        help="Is this the id that should be used for this type.")
    comment = fields.Text(
        string="Comment", 
        help="Notes about identifier usage.")                        
    start_date = fields.Datetime(
        string="Start Date", 
        help="Start of the period when the identifier was/is valid.")                        
    end_date = fields.Datetime(
        string="End Date", 
        help="End of the period when the identifier was/is valid.")                       

class NamingSystemContact(models.Model):    
    _name = "hc.naming.system.contact"    
    _description = "Naming System Contact"            
    _inherit = ["hc.basic.association"]    
    _inherits = {"hc.contact.detail": "contact_id"}

    contact_id = fields.Many2one(
        comodel_name="hc.contact.detail", 
        string="Contact", 
        ondelete="restrict", 
        required="True", 
        help="Contact Detail associated with this Naming System Contact.")                        
    naming_system_id = fields.Many2one(
        comodel_name="hc.res.naming.system", 
        string="Naming System", 
        help="Naming System associated with this Naming System Contact.")                        

class NamingSystemUseContext(models.Model):    
    _name = "hc.naming.system.use.context"    
    _description = "Naming System Use Context"            
    _inherit = ["hc.basic.association", "hc.usage.context"]    

    naming_system_id = fields.Many2one(
        comodel_name="hc.res.naming.system", 
        string="Naming System", 
        help="Naming System associated with this Naming System Use Context.")                        

class NamingSystemUniqueIdCategory(models.Model):    
    _name = "hc.vs.naming.system.unique.id.category"    
    _description = "Naming System Unique Id Category"            
    _inherit = ["hc.value.set.contains"]    
