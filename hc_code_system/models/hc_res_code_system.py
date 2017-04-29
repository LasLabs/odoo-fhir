# -*- coding: utf-8 -*-

from openerp import models, fields, api

class CodeSystem(models.Model):    
    _name = "hc.res.code.system"    
    _description = "Code System"    
    _rec_name = "title"            

    url = fields.Char(
        string="URI", 
        help="Globally unique logical identifier for code system (Coding.system).")                        
    identifier_id = fields.Many2one(
        comodel_name="hc.code.system.identifier", 
        string="Identifier", 
        help="Additional identifier for the code system (e.g. HL7 v2 / CDA).")                        
    version = fields.Char(
        string="Version", 
        help="Logical identifier for this version (Coding.version).")                        
    name = fields.Char(
        string="Name", 
        help="Informal name for this code system.")                        
    title = fields.Char(
        string="Title", 
        help="Name for this code system (Human friendly).")                        
    status = fields.Selection(
        string="Status", 
        required="True", 
        selection=[
            ("draft", "Draft"), 
            ("active", "Active"), 
            ("retired", "Retired")], 
        help="The status of this code system. Enables tracking the life-cycle of the content.")                        
    is_experimental = fields.Boolean(
        string="Experimental", 
        help="If for testing purposes, not real usage.")                        
    publisher = fields.Char(
        string="Publisher", 
        help="Name of the publisher (organization or individual).")                        
    contact_ids = fields.One2many(
        comodel_name="hc.code.system.contact", 
        inverse_name="code_system_id", 
        string="Contacts", 
        help="Contact details for the publisher.")                        
    date = fields.Datetime(
        string="Date", 
        help="Date for given status.")                        
    description = fields.Text(
        string="Description", 
        help="Human language description of the code system.")                        
    use_context_ids = fields.One2many(
        comodel_name="hc.code.system.use.context", 
        inverse_name="code_system_id", 
        string="Use Contexts", 
        help="Content intends to support these contexts.")                        
    jurisdiction_ids = fields.Many2many(
        comodel_name="hc.vs.jurisdiction", 
        relation="code_system_jurisdiction_rel", 
        string="Jurisdictions", 
        help="Intended jurisdiction for code system (if applicable).")                        
    purpose = fields.Text(
        tring="Purpose", 
        help="Why this code system is defined.")                        
    copyright = fields.Text(
        string="Copyright", 
        help="Use and/or publishing restrictions.")                        
    is_case_sensitive = fields.Boolean(
        string="Case Sensitive", 
        help="If code comparison is case sensitive.")                        
    value_set = fields.Char(
        string="Value Set URI", 
        help="Canonical URL for value set with entire code system.")                        
    hierarchy_meaning = fields.Selection(
        string="Hierarchy Meaning", 
        selection=[
            ("grouped-by", "Grouped By"), 
            ("is-a", "Is A"), 
            ("part-of", "Part Of"), 
            ("classified with", "Classified With")], 
        help="The meaning of the heirarchy of concepts.")                        
    is_compositional = fields.Boolean(
        string="Compositional", 
        help="If code system defines a post-composition grammar.")                        
    is_version_needed = fields.Boolean(
        string="Version Needed", 
        help="If definitions are not stable.")                        
    content = fields.Selection(
        string="Content", 
        required="True", 
        selection=[
            ("not-present", "Not Present"), 
            ("examplar", "Examplar"), 
            ("fragment", "Fragment"), 
            ("complete", "Complete")], 
        help="How much of the content of the code system - the concepts and codes it defines - are represented in this resource.")                        
    count = fields.Integer(
        string="Count", 
        help="Total concepts in the code system.")                        
    filter_ids = fields.One2many(
        comodel_name="hc.code.system.filter", 
        inverse_name="code_system_id", 
        string="Filter", 
        help="Filter that can be used in a value set.")                        
    property_ids = fields.One2many(
        comodel_name="hc.code.system.property", 
        inverse_name="code_system_id", 
        string="Property", 
        help="Additional information supplied about each concept.")                        
    concept_ids = fields.One2many(
        comodel_name="hc.code.system.concept", 
        inverse_name="code_system_id", 
        string="Concept", 
        help="Concepts in the code system.")                        

class CodeSystemFilter(models.Model):    
    _name = "hc.code.system.filter"    
    _description = "Code System Filter"                

    code_system_id = fields.Many2one(
        comodel_name="hc.res.code.system", 
        string="Code System", 
        help="Code System associated with this Code System Filter.")                        
    code_id = fields.Many2one(
        comodel_name="hc.vs.code.system.filter.code", 
        string="Code", 
        required="True", 
        help="Code that identifies the filter.")                        
    description = fields.Text(
        string="Description", 
        help="How or why the filter is used.")                        
    operator_ids = fields.Many2many(
        comodel_name="hc.vs.filter.operator", 
        relation="code_system_filter_operator_rel", 
        string="Operators", 
        required="True", 
        help="Operators that can be used with filter.")                        
    value = fields.Char(
        string="Value", 
        required="True", 
        help="What to use for the value.")                        

class CodeSystemProperty(models.Model):    
    _name = "hc.code.system.property"    
    _description = "Code System Property"                

    code_system_id = fields.Many2one(
        comodel_name="hc.res.code.system", 
        string="Code System", 
        help="Code System associated with this Code System Property.")                        
    code_id = fields.Many2one(
        comodel_name="hc.vs.code.system.property.code", 
        string="Code", 
        required="True", 
        help="Identifies the property on the concepts, and when referred to in operations.")                        
    uri = fields.Char(
        string="URI", 
        help="Formal identifier for the property.")                        
    description = fields.Text(
        string="Description", 
        help="Why the property is defined, and/or what it conveys.")                        
    type = fields.Selection(
        string="Type", 
        required="True", 
        selection=[
            ("code", "Code"), 
            ("coding", "Coding"), 
            ("string", "String"), 
            ("integer", "Integer"), 
            ("boolean", "Boolean"), 
            ("datetime", "Datetime")], 
        help="The type of the property value.")                        

class CodeSystemConcept(models.Model):    
    _name = "hc.code.system.concept"    
    _description = "Code System Concept"                

    code_system_id = fields.Many2one(
        comodel_name="hc.res.code.system", 
        string="Code System", 
        help="Code System associated with this Code System Concept.")                        
    code_id = fields.Many2one(
        comodel_name="hc.vs.code.system.concept.code", 
        string="Code", 
        required="True", 
        help="Code that identifies concept.")                        
    display = fields.Char(
        string="Display", 
        help="Text to display to the user.")                        
    definition = fields.Text(
        string="Definition", 
        help="Formal definition.")                        
    concept_id = fields.Many2one(
        comodel_name="hc.code.system.concept", 
        string="Concept", 
        help="Child Concepts (is-a/contains/categorizes).")                        
    designation_ids = fields.One2many(
        comodel_name="hc.code.system.concept.designation", 
        inverse_name="concept_id", 
        string="Designation", 
        help="Additional representations for the concept.")                        
    property_ids = fields.One2many(
        comodel_name="hc.code.system.concept.property", 
        inverse_name="concept_id", 
        string="Property", 
        help="Property value for the concept.")                        

class CodeSystemConceptDesignation(models.Model):    
    _name = "hc.code.system.concept.designation"    
    _description = "Code System Concept Designation"                

    concept_id = fields.Many2one(
        comodel_name="hc.code.system.concept", 
        string="Concept", 
        help="Concepts in the code system.")                        
    language_id = fields.Many2one(
        comodel_name="hc.vs.language", 
        string="Language", 
        help="Human language of the designation.")                        
    use_id = fields.Many2one(
        comodel_name="hc.vs.designation.use", 
        string="Use", 
        help="Coding Details how this designation would be used.")                        
    value = fields.Char(
        string="Value", 
        required="True", 
        help="The text value for this designation.")                        

class CodeSystemConceptProperty(models.Model):    
    _name = "hc.code.system.concept.property"    
    _description = "Code System Concept Property"                

    concept_id = fields.Many2one(
        comodel_name="hc.code.system.concept", 
        string="Concept", 
        help="Concepts in the code system.")                        
    code_id = fields.Many2one(
        comodel_name="hc.vs.code.system.property.code", 
        string="Code", required="True", 
        help="Reference to CodeSystem.property.code.")                        
    value_type = fields.Selection(
        string="Value Type", 
        required="True", 
        selection=[
            ("code", "Code"), 
            ("Coding", "Coding"), 
            ("string", "String"), 
            ("integer", "Integer"), 
            ("boolean", "Boolean"), 
            ("dateTime", "Datetime")], 
        help="Type of value of the property for this concept.")                        
    value_name = fields.Char(
        string="Value", 
        compute="_compute_value_name", 
        store="True", 
        help="Value of the property for this concept.")                        
    value_code_id = fields.Many2one(
        comodel_name="hc.vs.code.system.concept.property.value.code", 
        string="Value Code", 
        help="Code value of the property for this concept.")                        
    value_coding_id = fields.Many2one(
        comodel_name="hc.vs.code.system.concept.property.value.coding", 
        string="Value Coding", 
        help="Coding value of the property for this concept.")                        
    value_string = fields.Char(
        string="Value", 
        help="String of value of the property for this concept.")                        
    value_integer = fields.Integer(
        string="Value Integer", 
        help="Integer value of the property for this concept.")                        
    value_boolean = fields.Boolean(
        string="Value Boolean", 
        help="Boolean value of the property for this concept.")                        
    value_datetime = fields.Datetime(
        string="Value Datetime", 
        help="Datetime value of the property for this concept.")                        

class CodeSystemIdentifier(models.Model):    
    _name = "hc.code.system.identifier"    
    _description = "Code System Identifier"            
    _inherit = ["hc.basic.association", "hc.identifier"]    

class CodeSystemContact(models.Model):    
    _name = "hc.code.system.contact"    
    _description = "Code System Contact"            
    _inherit = ["hc.basic.association"]    
    _inherits = {"hc.contact.detail": "contact_id"}

    contact_id = fields.Many2one(
        comodel_name="hc.contact.detail", 
        string="Contact", 
        ondelete="restrict", 
        required="True", 
        help="Contact Detail associated with this Code System Contact.")                        
    code_system_id = fields.Many2one(
        comodel_name="hc.res.code.system", 
        string="Code System", 
        help="Code System associated with this Code System Contact.")                        

class CodeSystemUseContext(models.Model):    
    _name = "hc.code.system.use.context"    
    _description = "Code System Use Context"            
    _inherit = ["hc.basic.association", "hc.usage.context"]   

    code_system_id = fields.Many2one(
        comodel_name="hc.res.code.system", 
        string="Code System", 
        help="Code System associated with this Code System Use Context.")                        

class CodeSystemConceptCode(models.Model):    
    _name = "hc.vs.code.system.concept.code"    
    _description = "Code System Concept Code"            
    _inherit = ["hc.value.set.contains"]    

class CodeSystemFilterCode(models.Model):    
    _name = "hc.vs.code.system.filter.code"    
    _description = "Code System Filter Code"            
    _inherit = ["hc.value.set.contains"]    

class CodeSystemPropertyCode(models.Model):    
    _name = "hc.vs.code.system.property.code"    
    _description = "Code System Property Code"            
    _inherit = ["hc.value.set.contains"]       

class FilterOperator(models.Model):    
    _name = "hc.vs.filter.operator"    
    _description = "Filter Operator"            
    _inherit = ["hc.value.set.contains"]    

class CodeSystemConceptPropertyValueCode(models.Model):    
    _name = "hc.vs.code.system.concept.property.value.code"    
    _description = "Code System Concept Property Value Code"            
    _inherit = ["hc.value.set.contains"]    

class CodeSystemConceptPropertyValueCoding(models.Model):    
    _name = "hc.vs.code.system.concept.property.value.coding"    
    _description = "Code System Concept Property Value Coding"            
    _inherit = ["hc.value.set.contains"]    
