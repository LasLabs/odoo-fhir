# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ConceptMap(models.Model):    
    _name = "hc.res.concept.map"    
    _description = "Concept Map"    
    _rec_name = "title"            

    url = fields.Char(
        string="URI", 
        help="Globally unique logical id for concept map.")                        
    identifier_id = fields.Many2one(
        comodel_name="hc.concept.map.identifier", 
        string="Identifier", 
        help="Additional identifier for the concept map.")                        
    version = fields.Char(
        string="Version", 
        help="Logical id for this version of the concept map.")                        
    name = fields.Char(
        string="Name", 
        help="Informal name for this concept map.")                        
    title = fields.Char(
        string="Title", 
        help="Name for this concept map (Human friendly).")                        
    status = fields.Selection(
        string="Status", 
        required="True", 
        selection=[
            ("draft", "Draft"), 
            ("active", "Active"), 
            ("retired", "Retired")], 
        help="The status of this concept map. Enables tracking the life-cycle of the content.")                        
    is_experimental = fields.Boolean(
        string="Experimental", 
        help="If for testing purposes, not real usage.")                        
    publisher = fields.Char(
        string="Publisher", 
        help="Name of the publisher (Organization or individual).")                        
    contact_ids = fields.One2many(
        comodel_name="hc.concept.map.contact", 
        inverse_name="concept_map_id", 
        string="Contacts", 
        help="Contact details for the publisher.")                        
    concept_map_date = fields.Datetime(
        string="Concept Map Date", 
        help="Date for given status.")                        
    description = fields.Text(
        string="Description", 
        help="Human language description of the concept map.")                        
    use_context_ids = fields.One2many(
        comodel_name="hc.concept.map.use.context", 
        inverse_name="concept_map_id", 
        string="Use Contexts", 
        help="Content intends to support these contexts.")                        
    jurisdiction_ids = fields.Many2many(
        comodel_name="hc.vs.jurisdiction", 
        relation="concept_map_jurisdiction_rel", 
        string="Jurisdictions", 
        help="Intended jurisdiction for concept map (if applicable).")                        
    purpose = fields.Text(
        string="Purpose", 
        help="Why this concept map is defined.")                        
    copyright = fields.Text(
        string="Copyright", 
        help="Use and/or Publishing restrictions.")                        
    source_type = fields.Selection(
        string="Source Type", 
        required="True", 
        selection=[
            ("uri", "URI"), 
            ("Value Set", "Value Set"), 
            ("Structure Definition", "Structure Definition")], 
        help="Type of source of the concepts which are being mapped.")                        
    source_name = fields.Char(
        string="Source", 
        compute="_compute_source_name", 
        store="True", 
        help="Identifies the source of the concepts which are being mapped.")                        
    source_uri = fields.Char(
        string="Source URI", 
        help="URI that identifies the source of the concepts which are being mapped.")                        
    # source_value_set_id = fields.Many2one(
    #     comodel_name="hc.res.value.set", 
    #     string="Source Value Set", 
    #     help="Value Set that identifies the source of the concepts which are being mapped.")                        
    source_structure_definition_id = fields.Many2one(
        comodel_name="hc.res.structure.definition", 
        string="Source Structure Definition", 
        help="Structure Definition that identifies the source of the concepts which are being mapped.")                        
    target_type = fields.Selection(
        string="Target Type", 
        required="True", 
        selection=[
            ("uri", "URI"), ("Value Set", "Value Set"), ("Structure Definition", "Structure Definition")], help="Type of context to the mappings.")                        
    target_name = fields.Char(
        string="Target", 
        compute="_compute_target_name", store="True", help="Provides context to the mappings.")                        
    target_uri = fields.Char(
        string="Target URI", 
        help="URI that provides context to the mappings.")                        
    # target_value_set_id = fields.Many2one(
    #     comodel_name="hc.res.value.set", 
    #     string="Target Value Set", 
    #     help="Value Set that provides context to the mappings.")                        
    target_structure_definition_id = fields.Many2one(
        comodel_name="hc.res.structure.definition", 
        string="Target Structure Definition", 
        help="Structure Definition that provides context to the mappings.")                        
    group_ids = fields.One2many(
        comodel_name="hc.concept.map.group", 
        inverse_name="concept_map_id", 
        string="Group", 
        help="Same source and target systems.")                        

class ConceptMapGroup(models.Model):    
    _name = "hc.concept.map.group"    
    _description = "Concept Map Group"                

    concept_map_id = fields.Many2one(
        comodel_name="hc.res.concept.map", 
        string="Concept Map", 
        help="Concept Map associated with this Concept Map Group.")                        
    source = fields.Char(
        string="Source URI", 
        required="True", 
        help="Code System (if value set crosses code systems).")                        
    source_version = fields.Char(
        string="Source Version", 
        help="Specific version of the code system.")                        
    target = fields.Char(
        string="Target URI", 
        help="System of the target (if necessary).")                        
    target_version = fields.Char(
        string="Target Version", 
        help="Specific version of the code system.")                        
    element_ids = fields.One2many(
        comodel_name="hc.concept.map.group.element", 
        inverse_name="group_id", 
        string="Element", 
        help="Mappings for a concept from the source set.")                        

class ConceptMapGroupElement(models.Model):    
    _name = "hc.concept.map.group.element"    
    _description = "Concept Map Group Element"                

    group_id = fields.Many2one(
        comodel_name="hc.concept.map.group", 
        string="Group", 
        help="Same source and target systems.")                        
    code_id = fields.Many2one(
        comodel_name="hc.vs.concept.map.element.code", 
        string="Code", 
        help="Identifies element being mapped.")                        
    target_ids = fields.One2many(
        comodel_name="hc.concept.map.group.element.target", 
        inverse_name="element_id", 
        string="Target", 
        help="Concept in target system for element.")                        

class ConceptMapGroupElementTarget(models.Model):    
    _name = "hc.concept.map.group.element.target"    
    _description = "Concept Map Group Element Target"                

    element_id = fields.Many2one(
        comodel_name="hc.concept.map.group.element", 
        string="Element", 
        help="Mappings for a concept from the source set.")                        
    code_id = fields.Many2one(
        comodel_name="hc.vs.concept.map.element.code", 
        string="Code", 
        help="Code that identifies the target element.")                        
    equivalence = fields.Selection(
        string="Equivalence",
        selection=[
            ("relatedto", "Related to"), 
            ("equivalent", "Equivalent"), 
            ("equal", "Equal"), 
            ("wider", "Wider"), 
            ("subsumes", "Subsumes"), 
            ("narrower", "Narrower"), 
            ("specializes", "Specializes"), 
            ("inexact", "Inexact"), 
            ("unmatched", "Unmatched") ],       
        help="The status of this structure definition. Enables tracking the life-cycle of the content.")                        
    comments = fields.Text(
        string="Comments", 
        help="Description of status/issues in mapping.")
    product_ids = fields.One2many(
        comodel_name="hc.concept.map.group.element.target.depends.on", 
        inverse_name="target_id", 
        string="Product", 
        help="Content as for ConceptMap.group.element.target.dependsOn Other concepts that this mapping also produces.")
    depends_on_ids = fields.One2many(
        comodel_name="hc.concept.map.group.element.target.depends.on", 
        inverse_name="target_id", 
        string="Depends On", 
        help="Other elements required for this mapping (from context).")

class ConceptMapGroupElementTargetDependsOn(models.Model):    
    _name = "hc.concept.map.group.element.target.depends.on"    
    _description = "Concept Map Group Element Target Depends On"                

    
    target_id = fields.Many2one(
        comodel_name="hc.concept.map.group.element.target", 
        string="Target", 
        help="Concept in target system for element.")
    property = fields.Char(
        string="Property URI", 
        required="True", 
        help="Reference to property mapping depends on.")
    system = fields.Char(
        string="System URI", 
        help="Code System (if necessary).")
    code = fields.Char(
        string="Code", 
        required="True", 
        help="Value of the referenced element.")
                       
class ConceptMapIdentifier(models.Model):    
    _name = "hc.concept.map.identifier"    
    _description = "Concept Map Identifier"            
    _inherit = ["hc.basic.association", "hc.identifier"]    

class ConceptMapContact(models.Model):    
    _name = "hc.concept.map.contact"    
    _description = "Concept Map Contact"            
    _inherit = ["hc.basic.association"]    
    _inherits = {"hc.contact.detail": "contact_id"}

    contact_id = fields.Many2one(
        comodel_name="hc.contact.detail", 
        string="Contact", 
        ondelete="restrict", 
        required="True", help="Contact Detail associated with this Concept Map Contact.")                        
    concept_map_id = fields.Many2one(
        comodel_name="hc.res.concept.map", 
        string="Concept Map", 
        help="Concept Map associated with this Concept Map Contact.")                        

class ConceptMapUseContext(models.Model):    
    _name = "hc.concept.map.use.context"    
    _description = "Concept Map Use Context"            
    _inherit = ["hc.basic.association", "hc.usage.context"]    

    concept_map_id = fields.Many2one(
        comodel_name="hc.res.concept.map", 
        string="Concept Map", 
        help="Concept Map associated with this Concept Map Use Context.")

class ConceptMapElementCode(models.Model):  
    _name = "hc.vs.concept.map.element.code"    
    _description = "Concept Map Element Code"           
    _inherit = ["hc.value.set.contains"]