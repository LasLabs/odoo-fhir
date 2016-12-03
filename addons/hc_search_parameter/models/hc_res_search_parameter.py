# -*- coding: utf-8 -*-

from openerp import models, fields, api

class SearchParameter(models.Model):    
    _name = "hc.res.search.parameter"    
    _description = "Search Parameter"                

    url = fields.Char(
        string="URL", 
        required="True", 
        help="Literal URL used to reference this search parameter.")                        
    version = fields.Char(
        string="Version", 
        help="Business version of the search parameter.")                        
    name = fields.Char(
        string="Name", 
        required="True", 
        help="Name of search parameter.")                        
    status = fields.Selection(
        string="Status", 
        selection=[
            ("draft", "Draft"), 
            ("active", "Active"), 
            ("retired", "Retired")], 
        help="The status of this search parameter. Enables tracking the life-cycle of the content.")                        
    is_experimental = fields.Boolean(
        string="Experimental", 
        help="If for testing purposes, not real usage.")                        
    date = fields.Datetime(
        string="Date", 
        help="Publication Date(/time).")                        
    publisher = fields.Char(
        string="Publisher", 
        help="Name of the publisher (Organization or individual).")                        
    contact_ids = fields.One2many(
        comodel_name="hc.search.parameter.contact", 
        inverse_name="search_parameter_id", 
        string="Contacts", 
        help="Contact details for the publisher.")                        
    use_context_ids = fields.One2many(
        comodel_name="hc.search.parameter.use.context", 
        inverse_name="search_parameter_id", 
        string="Use Contexts", 
        help="Content intends to support these contexts.")                        
    jurisdiction_ids = fields.Many2many(
        comodel_name="hc.vs.jurisdiction", 
        relation="search_parameter_jurisdiction_rel", 
        string="Jurisdictions", 
        help="Intended jurisdiction for search parameter (if applicable).")                        
    purpose = fields.Text(
        string="Purpose", 
        help="Why this search parameter is defined.")                        
    code_id = fields.Many2one(
        comodel_name="hc.vs.search.parameter.code", 
        string="Code", 
        required="True", 
        help="Code used in URL.")                        
    base_id = fields.Many2one(
        comodel_name="hc.vs.resource.type", 
        string="Base", 
        required="True", 
        help="The resource type this search parameter applies to.")                        
    type = fields.Selection(
        string="Type", 
        required="True", 
        selection=[
            ("number", "Number"), 
            ("date", "Date"), 
            ("string", "String"), 
            ("token", "Token"), 
            ("reference", "Reference"), 
            ("composite", "Composite"), 
            ("quantity", "Quantity"), 
            ("uri", "URI")], 
        help="The type of value a search parameter refers to, and how the content is interpreted.")                        
    derived_from = fields.Char(
        string="URI Derived From", 
        help="Original Definition for the search parameter.")                        
    description = fields.Text(
        string="Description", 
        required="True", 
        help="Natural language description of the search parameter.")                        
    expression = fields.Char(
        string="Expression", 
        help="FluentPath expression that extracts the values.")                        
    xpath = fields.Char(
        string="Xpath", 
        help="XPath that extracts the values.")                        
    xpath_usage = fields.Selection(
        string="Xpath Usage", 
        selection=[
            ("normal", "Normal"), 
            ("phonetic", "Phonetic"), 
            ("nearby", "Nearby"), 
            ("distance", "Distance"), 
            ("other", "Other")], 
        help="How the search parameter relates to the set of elements returned by evaluating the xpath query.")                        
    target_ids = fields.Many2many(
        comodel_name="hc.vs.resource.type", 
        relation="search_parameter_target_rel", 
        string="Targets", 
        help="Types of resource (if a resource reference).")                        
    comparator_ids = fields.One2many(
        comodel_name="hc.search.parameter.comparator", 
        inverse_name="search_parameter_id", 
        string="Comparators", 
        help="Comparators supported for the search parameter.")                        
    modifier_ids = fields.One2many(
        comodel_name="hc.search.parameter.modifier", 
        inverse_name="search_parameter_id", 
        string="Modifiers", 
        help="A modifier supported for the search parameter.")                        
    chain = fields.One2many(
        comodel_name="hc.search.parameter.chain", 
        inverse_name="search_parameter_id", 
        string="Chains", 
        help="Chained names supported.")                        
    component_ids = fields.One2many(
        comodel_name="hc.search.parameter.component", 
        inverse_name="search_parameter_id", 
        string="Software", 
        help="For Composite resources to define the parts.")                        

class SearchParameterComponent(models.Model):    
    _name = "hc.search.parameter.component"    
    _description = "Search Parameter Component"                

    search_parameter_id = fields.Many2one(
        comodel_name="hc.res.search.parameter", 
        string="Search Parameter", 
        help="For Composite resources to define the parts.")                        
    definition_id = fields.Many2one(
        comodel_name="hc.res.search.parameter", 
        string="Definition", 
        required="True", 
        help="Defines how the part works.")                        
    expression = fields.Char(
        string="Expression", 
        required="True", 
        help="Subexpression relative to main expression.")                        

class SearchParameterContact(models.Model):    
    _name = "hc.search.parameter.contact"    
    _description = "Search Parameter Contact"            
    _inherit = ["hc.basic.association"]    
    _inherits = {"hc.contact.detail": "contact_id"}

    contact_id = fields.Many2one(
        comodel_name="hc.contact.detail", 
        string="Contact", 
        ondelete="restrict", 
        required="True", 
        help="Contact Detail associated with this Search Parameter Contact.")                        
    search_parameter_id = fields.Many2one(
        comodel_name="hc.res.search.parameter", 
        string="Search Parameter", 
        help="Search Parameter associated with this Search Parameter Contact.")                        

class SearchParameterUseContext(models.Model):    
    _name = "hc.search.parameter.use.context"    
    _description = "Search Parameter Use Context"            
    _inherit = ["hc.basic.association", "hc.usage.context"]    

    search_parameter_id = fields.Many2one(
        comodel_name="hc.res.search.parameter", 
        string="Search Parameter", 
        help="Search Parameter associated with this Search Parameter Use Context.")                        

class SearchParameterChain(models.Model):    
    _name = "hc.search.parameter.chain"    
    _description = "Search Parameter Chain"            
    _inherit = ["hc.basic.association"]    

    search_parameter_id = fields.Many2one(
        comodel_name="hc.res.search.parameter", 
        string="Search Parameter", 
        help="Search Parameter associated with this Search Parameter Chain.")                        
    chain = fields.Char(
        string="Chain", 
        help="Chain associated with this Search Parameter Chain.")                        

class SearchParameterComparator(models.Model):    
    _name = "hc.search.parameter.comparator"    
    _description = "Search Parameter Comparator"            
    _inherit = ["hc.basic.association"]    

    search_parameter_id = fields.Many2one(
        comodel_name="hc.res.search.parameter", 
        string="Search Parameter", 
        help="Search Parameter associated with this Search Parameter Comparator.")                        
    comparator = fields.Selection(
        string="Comparator", 
        selection=[
            ("eq", "EQ"), 
            ("ne", "NE"), 
            ("gt", "GT"), 
            ("lt", "LT"), 
            ("ge", "GE"), 
            ("le", "LE"), 
            ("sa", "SA"), 
            ("eb", "EB"), 
            ("ap", "AP")], 
        help="Comparators supported for the search parameter.")                        

class SearchParameterModifier(models.Model):    
    _name = "hc.search.parameter.modifier"    
    _description = "Search Parameter Modifier"            
    _inherit = ["hc.basic.association"]    

    search_parameter_id = fields.Many2one(
        comodel_name="hc.res.search.parameter", 
        string="Search Parameter", 
        help="Search Parameter associated with this Search Parameter Modifier.")                        
    modifier = fields.Selection(
        string="Modifier", 
        selection=[
            ("missing", "Missing"), 
            ("exact", "Exact"), 
            ("contains", "Contains"), 
            ("not", "Not"), 
            ("text", "Text"), 
            ("in", "In"), 
            ("not-in", "Not In"), 
            ("below", "Below"), 
            ("above", "Above") ], 
        help="A modifier supported for the search parameter.")                        
