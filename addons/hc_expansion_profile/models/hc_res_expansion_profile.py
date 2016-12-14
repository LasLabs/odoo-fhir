# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ExpansionProfile(models.Model):    
    _name = "hc.res.expansion.profile"    
    _description = "Expansion Profile"                

    url = fields.Char(
        string="URI", 
        help="Globally unique logical identifier for expansion profile.")                        
    identifier_id = fields.Many2one(
        comodel_name="hc.expansion.profile.identifier", 
        string="Identifier", 
        help="Additional identifier for the expansion profile (e.g. an Object Identifier).")                        
    version = fields.Char(
        string="Version", 
        help="Logical identifier for this version of the expansion profile.")                        
    name = fields.Char(
        string="Name", 
        help="Informal name for this expansion profile.")                        
    status = fields.Selection(
        string="Status", 
        required="True", 
        selection=[
            ("draft", "Draft"), 
            ("active", "Active"), 
            ("retired", "Retired")], 
        help="The status of this expansion profile. Enables tracking the life-cycle of the content.")                        
    is_experimental = fields.Boolean(
        string="Experimental", 
        help="If for testing purposes, not real usage.")                        
    publisher = fields.Char(
        string="Publisher", 
        help="Name of the publisher (organization or individual).")                        
    contact_ids = fields.One2many(
        comodel_name="hc.expansion.profile.contact", 
        inverse_name="expansion_profile_id", 
        string="Contacts", 
        help="Contact details for the publisher.")                        
    date = fields.Datetime(
        string="Date", 
        help="Date for given status.")                        
    description = fields.Char(
        string="Description", 
        help="Human language description of the expansion profile.")                        
    use_context_ids = fields.One2many(
        comodel_name="hc.expansion.profile.use.context", 
        inverse_name="expansion_profile_id", 
        string="Use Contexts", 
        help="Content intends to support these contexts.")                        
    jurisdiction_ids = fields.Many2many(
        comodel_name="hc.vs.jurisdiction", 
        relation="expansion_profile_jurisdiction_rel", 
        string="Jurisdictions", 
        help="Intended jurisdiction for expansion profile (if applicable).")                        
    is_include_designations = fields.Boolean(
        string="Include Designations", 
        help="Whether the expansion should include concept designations.")                        
    is_include_definition = fields.Boolean(
        string="Include Definition", 
        help="Include or exclude the value set definition in the expansion.")                        
    is_active_only = fields.Boolean(
        string="Active Only", 
        help="Include or exclude inactive concepts in the expansion.")
    is_exclude_nested = fields.Boolean(
        string="Exclude Nested", 
        help="Include or exclude nested codes in the value set expansion.")                        
    is_exclude_not_for_ui = fields.Boolean(
        string="Exclude Not For UI", 
        help="Include or exclude codes which cannot be rendered in user interfaces in the value set expansion.")                        
    is_exclude_post_coordinated = fields.Boolean(
        string="Exclude Post Coordinated", 
        help="Include or exclude codes which are post coordinated expressions in the value set expansion.")                        
    display_language_id = fields.Many2one(
        comodel_name="hc.vs.language", 
        string="Display Language", 
        help="Specify the language for the display element of codes in the value set expansion.")                        
    is_limited_expansion = fields.Boolean(
        string="Limited Expansion", 
        help="Controls behaviour of the value set expand operation when value sets are too large to be completely expanded.")                        
    fixed_version_ids = fields.One2many(
        comodel_name="hc.expansion.profile.fixed.version", 
        inverse_name="expansion_profile_id", 
        string="Fixed Version", 
        help="Fix use of a code system to a particular version.")                        
    excluded_system_ids = fields.One2many(
        comodel_name="hc.expansion.profile.excluded.system", 
        inverse_name="expansion_profile_id", 
        string="Excluded System", 
        help="Systems/Versions to be exclude.")                        
    designation_ids = fields.One2many(
        comodel_name="hc.expansion.profile.designation", 
        inverse_name="expansion_profile_id", 
        string="Designation", 
        help="When the expansion profile imposes designation contraints.")                        

class ExpansionProfileFixedVersion(models.Model):    
    _name = "hc.expansion.profile.fixed.version"    
    _description = "Expansion Profile Fixed Version"                

    expansion_profile_id = fields.Many2one(
        comodel_name="hc.res.expansion.profile", 
        string="Expansion Profile", 
        help="Expansion Profile associated with this Expansion Profile Fixed Version.")                        
    system = fields.Char(
        string="System URI", 
        required="True", 
        help="System to have it's version fixed.")                        
    version = fields.Char(
        string="Version", 
        required="True", 
        help="Specific version of the code system referred to.")                        
    mode = fields.Selection(
        string="Mode", 
        required="True", 
        selection=[
            ("default", "Default"), 
            ("check", "Check"), 
            ("override", "Override")], 
        help="How to manage the intersection between a fixed version in a value set, and this fixed version of the system in the expansion profile.")                        

class ExpansionProfileExcludedSystem(models.Model):    
    _name = "hc.expansion.profile.excluded.system"    
    _description = "Expansion Profile Excluded System"                

    expansion_profile_id = fields.Many2one(
        comodel_name="hc.res.expansion.profile", 
        string="Expansion Profile", 
        help="Expansion Profile associated with this Expansion Profile Excluded System.")                        
    system = fields.Char(
        string="System URI", 
        required="True", 
        help="The specific code system to be excluded.")                        
    version = fields.Char(
        string="Version", 
        help="Specific version of the code system referred to.")                        

class ExpansionProfileDesignation(models.Model):    
    _name = "hc.expansion.profile.designation"    
    _description = "Expansion Profile Designation"                

    expansion_profile_id = fields.Many2one(
        comodel_name="hc.res.expansion.profile", 
        string="Expansion Profile", 
        help="Expansion Profile associated with this Expansion Profile Designation.")                        
    include_ids = fields.One2many(
        comodel_name="hc.expansion.profile.designation.include", 
        inverse_name="designation_id", 
        string="Include", 
        help="Code systems to be included.")                        
    exclude_ids = fields.One2many(
        comodel_name="hc.expansion.profile.designation.exclude", 
        inverse_name="designation_id", 
        string="Exclude", 
        help="Designations to be excluded.")                        

class ExpansionProfileDesignationInclude(models.Model):    
    _name = "hc.expansion.profile.designation.include"    
    _description = "Expansion Profile Designation Include"                

    designation_id = fields.Many2one(
        comodel_name="hc.expansion.profile.designation", 
        string="Designation", 
        help="When the expansion profile imposes designation contraints.")                        
    designation_ids = fields.One2many(
        comodel_name="hc.expansion.profile.designation.include.designation", 
        inverse_name="include_id", 
        string="Designation", 
        help="The designation to be included.")                        

class ExpansionProfileDesignationIncludeDesignation(models.Model):    
    _name = "hc.expansion.profile.designation.include.designation"    
    _description = "Expansion Profile Designation Include Designation"                

    include_id = fields.Many2one(
        comodel_name="hc.expansion.profile.designation.include", 
        string="Include", 
        help="Code systems to be included.")                        
    language_id = fields.Many2one(
        comodel_name="hc.vs.language", 
        string="Language", 
        help="Human language of the designation to be included.")                        
    use_id = fields.Many2one(
        comodel_name="hc.vs.designation.use", 
        string="Use", 
        help="Designation use.")                        

class ExpansionProfileDesignationExclude(models.Model):    
    _name = "hc.expansion.profile.designation.exclude"    
    _description = "Expansion Profile Designation Exclude"                

    designation_id = fields.Many2one(
        comodel_name="hc.expansion.profile.designation", 
        string="Designation", 
        help="When the expansion profile imposes designation contraints.")                        
    designation_ids = fields.One2many(
        comodel_name="hc.expansion.profile.designation.exclude.designation", 
        inverse_name="exclude_id", 
        string="Designation", help="The designation to be excluded.")                        

class ExpansionProfileDesignationExcludeDesignation(models.Model):    
    _name = "hc.expansion.profile.designation.exclude.designation"    
    _description = "Expansion Profile Designation Exclude Designation"                

    exclude_id = fields.Many2one(
        comodel_name="hc.expansion.profile.designation.exclude", 
        string="Exclude", 
        help="Designations to be excluded.")                        
    language_id = fields.Many2one(
        comodel_name="hc.vs.language", 
        string="Language", 
        help="Human language of the designation to be excluded.")                        
    use_id = fields.Many2one(
        comodel_name="hc.vs.designation.use", 
        string="Use", 
        help="Designation use.")                        

class ExpansionProfileIdentifier(models.Model):    
    _name = "hc.expansion.profile.identifier"    
    _description = "Expansion Profile Identifier"            
    _inherit = ["hc.basic.association", "hc.identifier"]    

class ExpansionProfileContact(models.Model):    
    _name = "hc.expansion.profile.contact"    
    _description = "Expansion Profile Contact"            
    _inherit = ["hc.basic.association"]    
    _inherits = {"hc.contact.detail": "contact_id"}

    contact_id = fields.Many2one(
        comodel_name="hc.contact.detail", 
        string="Contact", 
        ondelete="restrict", 
        required="True", 
        help="Contact Detail associated with this Expansion Profile Contact.")                        
    expansion_profile_id = fields.Many2one(
        comodel_name="hc.res.expansion.profile", 
        string="Expansion Profile", 
        help="Expansion Profile associated with this Expansion Profile Contact.")                        

class ExpansionProfileUseContext(models.Model):    
    _name = "hc.expansion.profile.use.context"    
    _description = "Expansion Profile Use Context"            
    _inherit = ["hc.basic.association", "hc.usage.context"]    

    expansion_profile_id = fields.Many2one(
        comodel_name="hc.res.expansion.profile", 
        string="Expansion Profile", 
        help="Expansion Profile associated with this Expansion Profile Use Context.")                        
