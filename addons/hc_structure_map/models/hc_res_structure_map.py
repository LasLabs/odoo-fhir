# -*- coding: utf-8 -*-

from openerp import models, fields, api

class StructureMap(models.Model):    
    _name = "hc.res.structure.map"    
    _description = "Structure Map"
    _rec_name = "title"            

    url = fields.Char(
        string="URL", 
        required="True", 
        help="Absolute URL used to reference this StructureMap.")
    identifier_ids = fields.One2many(
        comodel_name="hc.structure.map.identifier", 
        inverse_name="structure_map_id", 
        string="Identifiers", 
        help="Other identifiers for the StructureMap.")
    version = fields.Char(
        string="Version", 
        help="Logical id for this version of the StructureMap.")
    name = fields.Char(
        string="Name", 
        required="True", 
        help="Name for this structure map (Computer friendly).")
    title = fields.Char(
        string="Title", 
        help="Name for this structure map (Human friendly).")
    status = fields.Selection(
        string="Status", 
        required="True", 
        selection=[
            ("draft", "Draft"), 
            ("active", "Active"), 
            ("retired", "Retired")], 
        help="The status of the StructureMap.")
    is_experimental = fields.Boolean(
        string="Experimental", 
        help="If for testing purposes, not real usage.")
    publisher = fields.Char(
        string="Publisher", 
        help="Name of the publisher (Organization or individual).")
    contact_ids = fields.One2many(
        comodel_name="hc.structure.map.contact", 
        inverse_name="structure_map_id", 
        string="Contacts", 
        help="Contact details for the publisher.")
    date = fields.Datetime(
        string="Date", 
        help="Date for this version of the StructureMap.")
    description = fields.Text(
        string="Description", 
        help="Natural language description of the Structure Map.")
    use_context_ids = fields.One2many(
        comodel_name="hc.structure.map.use.context", 
        inverse_name="structure_map_id", 
        string="Use Contexts", 
        help="Content intends to support these contexts.")
    jurisdiction_ids = fields.Many2many(
        comodel_name="hc.vs.jurisdiction", 
        relation="structure_map_jurisdiction_rel", 
        string="Jurisdictions", 
        help="Intended jurisdiction for structure map (if applicable).")
    purpose = fields.Text(
        string="Purpose", 
        help="Why this structure map is defined.")
    copyright = fields.Text(
        string="Copyright", 
        help="Use and/or publishing restrictions.")
    import_ids = fields.One2many(
        comodel_name="hc.structure.map.import", 
        inverse_name="structure_map_id", 
        string="Import URIs", 
        help="URI of other maps used by this map (canonical urls).")
    group_ids = fields.One2many(
        comodel_name="hc.structure.map.group", 
        inverse_name="structure_map_id", 
        string="Groups", 
        required="True", 
        help="Named sections for reader convenience.")
    structure_ids = fields.One2many(
        comodel_name="hc.structure.map.structure", 
        inverse_name="structure_map_id", 
        string="Structures", 
        help="Structure Definition used by this map.")

class StructureMapStructure(models.Model):    
    _name = "hc.structure.map.structure"    
    _description = "Structure Map Structure"            

    structure_map_id = fields.Many2one(
        comodel_name="hc.res.structure.map", 
        string="Structure Map", 
        help="Structure Map associated with this Structure Map Structure.")                    
    url = fields.Char(
        string="URL", 
        required="True", 
        help="Canonical URL for structure definition.")                    
    mode = fields.Selection(
        string="Mode", 
        required="True", 
        selection=[
            ("source", "Source"), 
            ("queried", "Queried"), 
            ("target", "Target"), 
            ("produced", "Produced")], 
        help="How the referenced structure is used in this mapping.")                    
    documentation = fields.Text(
        string="Documentation", 
        help="Documentation on use of structure.")
                 
class StructureMapGroup(models.Model):    
    _name = "hc.structure.map.group"    
    _description = "Structure Map Group"            

    structure_map_id = fields.Many2one(
        comodel_name="hc.res.structure.map", 
        string="Structure Map", 
        help="Structure Map associated with this Structure Map Group.")
    name = fields.Char(
        string="Name", 
        required="True", 
        help="Descriptive name for a user.")
    extends = fields.Char(
        string="Extends", 
        help="Another group that this group adds rules to.")
    documentation = fields.Text(
        string="Documentation", 
        help="Documentation for this group.")
    input_ids = fields.One2many(
        comodel_name="hc.structure.map.group.input", 
        inverse_name="group_id", 
        string="Inputs", 
        required="True", 
        help="Named instance provided when invoking the map.")
    rule_ids = fields.One2many(
        comodel_name="hc.structure.map.group.rule", 
        inverse_name="group_id", 
        string="Rules", 
        required="True", 
        help="Transform Rule from source to target.")
    parameter_ids = fields.One2many(
        comodel_name="hc.structure.map.group.parameter", 
        inverse_name="group_id", 
        string="Parameters", 
        help="Parameters to the transform.")

class StructureMapGroupInput(models.Model):    
    _name = "hc.structure.map.group.input"    
    _description = "Structure Map Group Input"            

    group_id = fields.Many2one(
        comodel_name="hc.structure.map.group", 
        string="Group", 
        help="Named sections for reader convenience.")
    name = fields.Char(
        string="Name", 
        required="True", 
        help="Name for this instance of data.")
    type = fields.Char(
        string="Type", 
        help="Type for this instance of data.")
    mode = fields.Selection(
        string="Mode", 
        required="True", 
        selection=[
            ("source", "Source"), 
            ("target", "Target")], 
        help="Mode for this instance of data.")
    documentation = fields.Text(
        string="Documentation", 
        help="Documentation for this instance of data.")

class StructureMapGroupParameter(models.Model):    
    _name = "hc.structure.map.group.parameter"    
    _description = "Structure Map Group Parameter"            

    group_id = fields.Many2one(
        comodel_name="hc.structure.map.group", 
        string="Group", 
        help="Named sections for reader convenience.")                    
    value_type = fields.Selection(
        string="Value Type", 
        required="True", 
        selection=[
            ("id", "Id"), 
            ("string", "String"), 
            ("boolean", "Boolean"), 
            ("integer", "Integer"), 
            ("decimal", "Decimal")], 
            help="Type of parameter value.")
    value_name = fields.Char(
        string="Value", 
        compute="_compute_value_name", 
        store="True", 
        help="Parameter value - variable or literal.")
    value_id = fields.Char(
        string="Value Id", 
        help="Id parameter value.")                    
    value_string = fields.Char(
        string="Value String", 
        help="String parameter value.")                    
    value_boolean = fields.Boolean(
        string="Value Boolean", 
        help="Boolean parameter value.")                    
    value_integer = fields.Integer(
        string="Value Integer", 
        help="Integer parameter value.")                    
    value_decimal = fields.Float(
        string="Value Decimal",  
        help="Decimal parameter value.")                    

class StructureMapGroupRule(models.Model):    
    _name = "hc.structure.map.group.rule"    
    _description = "Structure Map Group Rule"            

    group_id = fields.Many2one(
        comodel_name="hc.structure.map.group", 
        string="Group", 
        help="Named sections for reader convenience.")
    name = fields.Char(
        string="Name", 
        required="True", 
        help="Name of the rule for internal references.")
    documentation = fields.Text(
        string="Documentation", 
        help="Documentation for this instance of data.")
    rule_id = fields.Many2one(
        comodel_name="hc.structure.map.group.rule", 
        string="Rule", 
        help="Rules contained in this rule.")
    target_ids = fields.One2many(
        comodel_name="hc.structure.map.group.rule.target", 
        inverse_name="rule_id", 
        string="Targets", 
        help="Content to create because of this mapping rule.")
    source_ids = fields.One2many(
        comodel_name="hc.structure.map.group.rule.source", 
        inverse_name="rule_id", 
        string="Sources", 
        required="True", 
        help="Source inputs to the mapping.")
    dependent_ids = fields.One2many(
        comodel_name="hc.structure.map.group.rule.dependent", 
        inverse_name="rule_id", 
        string="Dependents", 
        help="Which other rules to apply in the context of this rule.")

class StructureMapGroupRuleSource(models.Model):    
    _name = "hc.structure.map.group.rule.source"    
    _description = "Structure Map Group Rule Source"            

    rule_id = fields.Many2one(
        comodel_name="hc.structure.map.group.rule", 
        string="Rule", 
        help="Transform Rule from source to target.")
    is_required = fields.Boolean(
        string="Required", 
        required="True", 
        help="Whether this rule applies if the source isn't found.")
    context = fields.Char(
        string="Context", 
        required="True", 
        help="Type or variable this rule applies to.")
    context_type = fields.Selection(
        string="Context Type", 
        required="True", 
        selection=[
            ("type", "Type"), 
            ("variable", "Variable")], 
        help="How to interpret the context.")
    element = fields.Char(
        string="Element", 
        help="Optional field for this source.")
    list_mode = fields.Selection(
        string="List Mode", 
        selection=[
            ("first", "First"), 
            ("share", "Share"), 
            ("last", "Last")], 
        help="If field is a list, how to manage the list.")
    variable = fields.Char(
        string="Variable", 
        help="Named context for field, if a field is specified.")
    condition = fields.Char(
        string="Condition", 
        help="FluentPath expression - must be true or the rule does not apply.")
    check = fields.Char(
        string="Check", 
        help="FluentPath expression - must be true or the mapping engine throws an error instead of completing.")
               
class StructureMapGroupRuleTarget(models.Model):    
    _name = "hc.structure.map.group.rule.target"    
    _description = "Structure Map Group Rule Target"            

    rule_id = fields.Many2one(
        comodel_name="hc.structure.map.group.rule", 
        string="Rule", 
        help="Transform Rule from source to target.")
    context = fields.Char(
        string="Context", 
        required="True", 
        help="Type or variable this rule applies to.")
    context_type = fields.Selection(
        string="Context Type", 
        required="True", 
        selection=[
            ("type", "Type"), 
            ("variable", "Variable")], 
        help="How to interpret the context.")
    element = fields.Char(
        string="Element", 
        help="Field to create in the context.")
    variable = fields.Char(
        string="Variable", 
        help="Named context for field, if desired, and a field is specified.")
    list_mode_ids = fields.One2many(
        comodel_name="hc.structure.map.group.rule.target.list.mode", 
        inverse_name="target_id", 
        string="List Modes", 
        help="If field is a list, how to manage the list.")
    list_rule_id = fields.Char(
        string="List Rule Id", 
        help="Internal rule reference for shared list items.")
    transform = fields.Selection(
        string="Transform", 
        selection=[
            ("create", "Create"), 
            ("copy +", "Copy +")], 
        help="How the data is copied / created.")

class StructureMapGroupRuleDependent(models.Model):    
    _name = "hc.structure.map.group.rule.dependent"    
    _description = "Structure Map Group Rule Dependent"            

    rule_id = fields.Many2one(
        comodel_name="hc.structure.map.group.rule", 
        string="Rule", 
        help="Transform Rule from source to target.")
    name = fields.Char(
        string="Name", 
        required="True", 
        help="Name of a rule or group to apply.")
    variable = fields.Char(
        string="Variable", 
        required="True", 
        help="Names of variables to pass to the rule or group.")
                   
class StructureMapIdentifier(models.Model):    
    _name = "hc.structure.map.identifier"    
    _description = "Structure Map Identifier"            
    _inherit = ["hc.basic.association", "hc.identifier"]

    structure_map_id = fields.Many2one(
        comodel_name="hc.res.structure.map", 
        string="Structure Map", 
        help="Structure Map associated with this Structure Map Identifier.")                    

class StructureMapContact(models.Model):    
    _name = "hc.structure.map.contact"  
    _description = "Structure Map Contact"          
    _inherit = ["hc.basic.association"] 
    _inherits = {"hc.contact.detail": "contact_id"}

    contact_id = fields.Many2one(
        comodel_name="hc.contact.detail", 
        string="Contact", 
        ondelete="restrict", 
        required="True", 
        help="Contact Detail associated with this Structure Map Contact.")                       
    structure_map_id = fields.Many2one(
        comodel_name="hc.res.structure.map", 
        string="Structure Map", 
        help="Structure Map associated with this Structure Map Contact.")                       

class StructureMapImport(models.Model): 
    _name = "hc.structure.map.import"   
    _description = "Structure Map Import"           
    _inherit = ["hc.basic.association"]

    structure_map_id = fields.Many2one(
        comodel_name="hc.res.structure.map", 
        string="Structure Map", 
        help="Structure Map associated with this Structure Map Import.")                
    import_uri = fields.Char(
        string="Import URI", 
        help="URI of other maps used by this map (canonical URLs).")                  

class StructureMapUseContext(models.Model):    
    _name = "hc.structure.map.use.context"    
    _description = "Structure Map Use Context"            
    _inherit = ["hc.basic.association", "hc.usage.context"]

    structure_map_id = fields.Many2one(
        comodel_name="hc.res.structure.map", 
        string="Structure Map", 
        help="Structure Map associated with this Structure Map Use Context.")                    

class StructureMapGroupRuleTargetListMode(models.Model):    
    _name = "hc.structure.map.group.rule.target.list.mode"    
    _description = "Structure Map Group Rule Target List Mode"            
    _inherit = ["hc.basic.association"]

    target_id = fields.Many2one(
        comodel_name="hc.structure.map.group.rule.target", 
        string="Target", 
        help="Target associated with this Structure Map Group Rule Target List Mode.")                    
    list_mode = fields.Selection(
        string="List Mode", 
        selection=[
            ("first", "First"), 
            ("share", "Share"), 
            ("last", "Last")], 
        help="If field is a list, how to manage the list.")                    
