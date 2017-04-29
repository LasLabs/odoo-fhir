# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ValueSet(models.Model):    
    _name = "hc.res.value.set"    
    _description = "Value Set"                

    url = fields.Char(
        string="URI", 
        help="Globally unique logical id for value set.")
    identifier_id = fields.Many2one(
        comodel_name="hc.value.set.identifier", 
        string="Identifier", 
        help="Additional identifier for the value set (v2 / CDA).")
    version = fields.Char(
        string="Version", 
        help="Logical id for this version of the value set.")
    name = fields.Char(
        string="Name", 
        help="Informal name for this value set.")
    title = fields.Char(
        string="Title", 
        help="Name for this value set (Human friendly).")
    status = fields.Selection(
        string="Status", 
        required="True", 
        selection=[
            ("draft", "Draft"), 
            ("active", "Active"), 
            ("retired", "Retired")], 
        help="The status of this value set. Enables tracking the life-cycle of the content.")
    is_experimental = fields.Boolean(
        string="Experimental", 
        help="If for testing purposes, not real usage.")
    publisher = fields.Char(
        string="Publisher", 
        help="Name of the publisher (Organization or individual).")
    contact_ids = fields.One2many(
        comodel_name="hc.value.set.contact", 
        inverse_name="value_set_id", 
        string="Contacts", 
        help="Contact details for the publisher.")
    date = fields.Datetime(
        string="Date", 
        help="Date for given status.")
    description = fields.Text(
        string="Description", 
        help="Human language description of the value set.")
    use_context_ids = fields.One2many(
        comodel_name="hc.value.set.use.context", 
        inverse_name="value_set_id", 
        string="Use Contexts", 
        help="Content intends to support these contexts.")
    jurisdiction_ids = fields.Many2many(
        comodel_name="hc.vs.jurisdiction", 
        relation="value_set_jurisdiction_rel", 
        string="Jurisdictions", 
        help="Intended jurisdiction for value set (if applicable).")
    is_immutable = fields.Boolean(
        string="Immutable", 
        help="Indicates whether or not any change to the content logical definition may occur.")
    purpose = fields.Text(
        string="Purpose", 
        help="Why this value set is defined.")
    copyright = fields.Text(
        string="Copyright", 
        help="Use and/or Publishing restrictions.")
    is_extensible = fields.Boolean(
        string="Extensible", 
        help="Whether this is intended to be used with an extensible binding.")
    compose_ids = fields.One2many(
        comodel_name="hc.value.set.compose", 
        inverse_name="value_set_id", 
        string="Compose", 
        help="Definition of the content of the value set (CLD).")
    expansion_ids = fields.One2many(
        comodel_name="hc.value.set.expansion", 
        inverse_name="value_set_id", 
        string="Expansion", 
        help='Used when the value set is "expanded".')

class ValueSetCompose(models.Model):    
    _name = "hc.value.set.compose"    
    _description = "Value Set Compose"                

    value_set_id = fields.Many2one(
        comodel_name="hc.res.value.set", 
        string="Value Set", 
        help="Value Set associated with this Value Set Compose.")
    locked_date = fields.Date(
        string="Locked Date", 
        help="Fixed date for all referenced code systems and value sets.")
    is_inactive = fields.Boolean(
        string="Inactive", 
        help="Whether inactive codes are in the value set.")
    exclude_id = fields.Many2one(
        comodel_name="hc.value.set.compose", 
        string="Exclude", 
        help="Explicitly exclude codes from a code system or other value sets.")
    include_ids = fields.One2many(
        comodel_name="hc.value.set.compose.include", 
        inverse_name="compose_id", 
        string="Include", 
        required="True", 
        help="Include one or more codes from a code system or other value set(s).")

class ValueSetComposeInclude(models.Model):    
    _name = "hc.value.set.compose.include"    
    _description = "Value Set Compose Include"                

    compose_id = fields.Many2one(
        comodel_name="hc.value.set.compose", 
        string="Compose", 
        help="Definition of the content of the value set (CLD).")
    system = fields.Char(
        string="System URI", 
        help="The system the codes come from.")
    version = fields.Char(
        string="Version", 
        help="Specific version of the code system referred to.")
    value_set_ids = fields.One2many(
        comodel_name="hc.value.set.compose.include.value.set", 
        inverse_name="include_id", 
        string="Value Set URIs", 
        help="Select only contents included in this value set.")
    concept_reference_ids = fields.One2many(
        comodel_name="hc.value.set.compose.include.concept.reference", 
        inverse_name="include_id", 
        string="Concept Reference", 
        help="A concept defined in the system.")
    filter_ids = fields.One2many(
        comodel_name="hc.value.set.compose.include.filter", 
        inverse_name="include_id", 
        string="Filter", 
        help="Select codes/concepts by their properties (including relationships).")

class ValueSetComposeIncludeConceptReference(models.Model): 
    _name = "hc.value.set.compose.include.concept.reference"    
    _description = "Value Set Compose Include Concept Reference"
               
    include_id = fields.Many2one(
        comodel_name="hc.value.set.compose.include", 
        string="Include", 
        help="Include one or more codes from a code system or other value set(s).")
    code_id = fields.Many2one(
        comodel_name="hc.vs.value.set.concept.reference.code", 
        string="Code", 
        required="True", 
        help="Code or expression from system.")
    display = fields.Char(
        string="Display", 
        help="Test to display for this code for this value set.")
    designation_ids = fields.One2many(
        comodel_name="hc.value.set.compose.include.concept.reference.designation", 
        inverse_name="concept_reference_id", 
        string="Designation", 
        help="Additional representations for the concept.")

class ValueSetComposeIncludeConceptReferenceDesignation(models.Model):  
    _name = "hc.value.set.compose.include.concept.reference.designation"    
    _description = "Value Set Compose Include Concept Reference Designation"

    concept_reference_id = fields.Many2one(
        comodel_name="hc.value.set.compose.include.concept.reference", 
        string="Concept", 
        help="A concept defined in the system.")
    contains_id = fields.Many2one(
        comodel_name="hc.value.set.expansion.contains", 
        string="Contains", 
        help="Codes in the value set.")
    language_id = fields.Many2one(
        comodel_name="hc.vs.language", 
        string="Language", 
        help="Language of the designation.")
    use_id = fields.Many2one(
        comodel_name="hc.vs.designation.use", 
        string="Use", 
        help="Details how this designation would be used.")
    value = fields.Char(
        string="Value", 
        required="True", 
        help="The text value for this designation.")                   

class ValueSetComposeIncludeFilter(models.Model):    
    _name = "hc.value.set.compose.include.filter"    
    _description = "Value Set Compose Include Filter"                

    include_id = fields.Many2one(
        comodel_name="hc.value.set.compose.include", 
        string="Include", 
        help="Include one or more codes from a code system or other value set(s).")
    property_id = fields.Many2one(
        comodel_name="hc.vs.value.set.filter.property", 
        string="Property", 
        required="True", 
        help="A property defined by the code system.")
    op = fields.Selection(
        string="Op", 
        required="True", 
        selection=[
            ("=", "="), 
            ("is-a", "Is-A"), 
            ("is-not-a", "Is-Not-A"), 
            ("regex", "Regex"), 
            ("in", "In"), 
            ("not-in", "Not-In")], 
        help="Kind of operation to perform as a part of the filter criteria.")
    value_id = fields.Many2one(
        comodel_name="hc.vs.value.set.filter.value", 
        string="Value", 
        required="True", 
        help="Code from the system, or regex criteria.")

class ValueSetExpansion(models.Model):    
    _name = "hc.value.set.expansion"    
    _description = "Value Set Expansion"                

    value_set_id = fields.Many2one(
        comodel_name="hc.res.value.set", 
        string="Value Set", 
        help="Value Set associated with this Value Set Expansion.")
    identifier = fields.Char(
        string="Identifier URI", 
        required="True", 
        help="URL that uniquely identifies this expansion.")
    timestamp = fields.Datetime(
        string="Timestamp", 
        required="True", 
        help="Time valueset expansion happened.")
    total = fields.Integer(
        string="Total", 
        help="Total number of codes in the expansion.")
    offset = fields.Integer(
        string="Offset", 
        help="Offset at which this resource starts.")
    parameter_ids = fields.One2many(
        comodel_name="hc.value.set.expansion.parameter", 
        inverse_name="expansion_id", 
        string="Parameter", 
        help="Parameter that controlled the expansion process.")
    contains_ids = fields.One2many(
        comodel_name="hc.value.set.expansion.contains", 
        inverse_name="expansion_id", 
        string="Contains", 
        help="Codes in the value set.")

class ValueSetExpansionParameter(models.Model):    
    _name = "hc.value.set.expansion.parameter"    
    _description = "Value Set Expansion Parameter" 

    expansion_id = fields.Many2one(
        comodel_name="hc.value.set.expansion", 
        string="Expansion", 
        help='Used when the value set is "expanded".')
    name = fields.Char(
        string="Name", 
        required="True", 
        help="Name as assigned by server.")
    value_type = fields.Selection(
        string="Value Type", 
        selection=[
            ("string", "String"), 
            ("boolean", "Boolean"), 
            ("integer", "Integer"), 
            ("decimal", "Decimal"), 
            ("uri", "URI"), 
            ("code", "Code")], 
        help="Type of source of the concepts which are being mapped.")
    value_name = fields.Char(
        string="Value", 
        compute="_compute_value_name", 
        store="True", 
        help="Value of the parameter.")
    value_string = fields.Char(
        string="Value", 
        help="String of value of the parameter.")
    is_value_boolean = fields.Boolean(
        string="Value Boolean", 
        help="Value of the parameter.")
    value_integer = fields.Integer(
        string="Value Integer", 
        help="Integer of value of the parameter.")
    value_decimal = fields.Float(
        string="Value Decimal", 
        help="Decimal of value of the parameter.")
    value_uri = fields.Char(
        string="Value URI", 
        help="URI of value of the parameter.")
    value_code_id = fields.Many2one(
        comodel_name="hc.vs.value.set.parameter.value", 
        string="Value Code", 
        help="Code of value of the parameter.")

class ValueSetExpansionContains(models.Model):    
    _name = "hc.value.set.expansion.contains"    
    _description = "Value Set Expansion Contains"                

    expansion_id = fields.Many2one(
        comodel_name="hc.value.set.expansion", 
        string="Expansion", 
        help='Used when the value set is "expanded".')
    system = fields.Char(
        string="System URI", 
        help="URL of system value for the code.")
    is_abstract = fields.Boolean(
        string="Abstract", 
        help="If user cannot select this entry.")
    is_inactive = fields.Boolean(
        string="Inactive", 
        help="If concept is inactive in the code system.")
    version = fields.Char(
        string="Version", 
        help="Version in which this code / display is defined.")
    code_id = fields.Many2one(
        comodel_name="hc.vs.value.set.contains.code", 
        string="Code", 
        help="Code - if blank, this is not a choosable code.")
    display = fields.Char(
        string="Display", 
        help="User display for the concept.")
    designation_ids = fields.One2many(
        comodel_name="hc.value.set.compose.include.concept.reference.designation", 
        inverse_name="contains_id", 
        string="Designation", 
        help="Additional representations for this item.")
    contains_id = fields.Many2one(
        comodel_name="hc.value.set.expansion.contains", 
        string="Contains", 
        help="Codes contained under this entry.")
                        
class ValueSetIdentifier(models.Model):    
    _name = "hc.value.set.identifier"    
    _description = "Value Set Identifier"            
    _inherit = ["hc.basic.association", "hc.identifier"]    

class ValueSetContact(models.Model):    
    _name = "hc.value.set.contact"    
    _description = "Value Set Contact"            
    _inherit = ["hc.basic.association"]    
    _inherits = {"hc.contact.detail": "contact_id"}

    contact_id = fields.Many2one(
        comodel_name="hc.contact.detail", 
        string="Contact", 
        ondelete="restrict", 
        required="True", 
        help="Contact Detail associated with this Value Set Contact.")                        
    value_set_id = fields.Many2one(
        comodel_name="hc.res.value.set", 
        string="Value Set", 
        help="Value Set associated with this Value Set Contact.")                        

class ValueSetUseContext(models.Model):    
    _name = "hc.value.set.use.context"    
    _description = "Value Set Use Context"            
    _inherit = ["hc.basic.association", "hc.usage.context"]    

    value_set_id = fields.Many2one(
        comodel_name="hc.res.value.set", 
        string="Value Set", 
        help="Value Set associated with this Value Set Use Context.")                        

class ValueSetComposeIncludeValueSet(models.Model): 
    _name = "hc.value.set.compose.include.value.set"    
    _description = "Value Set Compose Include Value Set"            
    _inherit = ["hc.basic.association"]

    include_id = fields.Many2one(
        comodel_name="hc.value.set.compose.include", 
        string="Include", 
        help="Include associated with this Value Set Compose Include Value Set.")                 
    value_set = fields.Char(
        string="Value Set URI", 
        help="URI of Value Set associated with this Value Set Compose Include Value Set.")                  

class ValueSetConceptReferenceCode(models.Model):   
    _name = "hc.vs.value.set.concept.reference.code"    
    _description = "Value Set Concept Reference Code"           
    _inherit = ["hc.value.set.contains"]

class ValueSetFilterProperty(models.Model):    
    _name = "hc.vs.value.set.filter.property"    
    _description = "Value Set Filter Property"            
    _inherit = ["hc.value.set.contains"]    

class ValueSetFilterValue(models.Model):    
    _name = "hc.vs.value.set.filter.value"    
    _description = "Value Set Filter Value"            
    _inherit = ["hc.value.set.contains"]    

class ValueSetParameterValue(models.Model): 
    _name = "hc.vs.value.set.parameter.value"   
    _description = "Value Set Parameter Value"          
    _inherit = ["hc.value.set.contains"]

class ValueSetContainsCode(models.Model):    
    _name = "hc.vs.value.set.contains.code"    
    _description = "Value Set Contains Code"            
    _inherit = ["hc.value.set.contains"]    

# External Reference

class ElementDefinitionBinding(models.Model):    
    _inherit = "hc.element.definition.binding"

    value_set_id = fields.Many2one(
        comodel_name="hc.res.value.set", 
        string="Value Set", 
        help="Value Set the reference to the value set.")
