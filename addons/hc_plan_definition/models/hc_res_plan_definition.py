# -*- coding: utf-8 -*-

from openerp import models, fields, api

class PlanDefinition(models.Model):    
    _name = "hc.res.plan.definition"    
    _description = "Plan Definition"            

    url = fields.Char(
        string="URL", 
        help="Logical uri to reference this plan definition (globally unique).")                    
    identifier_ids = fields.One2many(
        comodel_name="hc.plan.definition.identifier", 
        inverse_name="plan_definition_id", 
        string="Identifiers", 
        help="Additional identifier for the plan definition.")                    
    version = fields.Char(
        string="Version", 
        help="Business version of the plan definition.")                    
    name = fields.Char(
        string="Name", 
        help="Name for this plan definition (Computer friendly).")                    
    title = fields.Char(
        string="Title", 
        help="Name for this plan definition (Human friendly).")                    
    type = fields.Selection(
        string="Type", 
        selection=[
            ("order-set", "Order Set"), 
            ("protocol", "Protocol"), 
            ("eca-rule", "Eca Rule")], 
        help="The type of action to perform (create, update, remove).")                    
    status = fields.Selection(
        string="Status", 
        required="True", 
        selection=[
            ("draft", "Draft"), 
            ("active", "Active"), 
            ("retired", "Retired")], 
        help="The status of this plan definition. Enables tracking the life-cycle of the content.")
    is_experimental = fields.Boolean(
        string="Experimental", 
        help="If for testing purposes, not real usage.")                    
    date = fields.Datetime(
        string="Date", 
        help="Date this was last changed.")                    
    description = fields.Text(
        string="Description", 
        help="Natural language description of the plan definition.")                    
    purpose = fields.Text(
        string="Purpose", 
        help="Why this plan definition is defined.")                    
    usage = fields.Text(
        string="Usage", 
        help="Describes the clinical usage of the asset.")                    
    approval_date = fields.Date(
        string="Approval Date", 
        help="When plan definition approved by publisher.")                    
    last_review_date = fields.Date(
        string="Last Review Date", 
        help="Last review date for the plan definition.")                    
    effective_period_start_date = fields.Datetime(
        string="Effective Period Start Date", 
        help="Start of the effective date range for the plan definition.")                    
    effective_period_end_date = fields.Datetime(
        string="Effective Period End Date", 
        help="End of the effective date range for the service definition.")                    
    use_context_ids = fields.One2many(
        comodel_name="hc.plan.definition.use.context", 
        inverse_name="plan_definition_id", 
        string="Use Contexts", 
        help="Content intends to support these contexts.")                    
    jurisdiction_ids = fields.Many2many(
        comodel_name="hc.vs.jurisdiction", 
        relation="plan_definition_jurisdiction_rel", 
        string="Jurisdictions", 
        help="Intended jurisdiction for plan definition (if applicable).")                    
    topic_ids = fields.Many2many(
        comodel_name="hc.vs.plan.definition.topic", 
        relation="plan_definition_topic_rel", 
        string="Topics", 
        help="Descriptional topics for the asset.")                    
    contributor_ids = fields.One2many(
        comodel_name="hc.plan.definition.contributor", 
        inverse_name="plan_definition_id", 
        string="Contributors", 
        help="A content contributor.")                    
    publisher = fields.Char(
        string="Publisher", 
        help="Name of the publisher (Organization or individual).")                    
    contact_ids = fields.One2many(
        comodel_name="hc.plan.definition.contact", 
        inverse_name="plan_definition_id", 
        string="Contacts", 
        help="Contact details for the publisher.")                    
    copyright = fields.Text(
        string="Copyright", 
        help="Use and/or publishing restrictions.")                    
    related_artifact_ids = fields.One2many(
        comodel_name="hc.plan.definition.related.artifact", 
        inverse_name="plan_definition_id", 
        string="Related Artifacts", 
        help="Related artifacts for the asset.")                    
    library_ids = fields.One2many(
        comodel_name="hc.plan.definition.library", 
        inverse_name="plan_definition_id", 
        string="Libraries", 
        help="Logic used by the plan definition.")                    
    action_definition_ids = fields.One2many(
        comodel_name="hc.plan.definition.action.definition", 
        inverse_name="plan_definition_id", 
        string="Action Definition", 
        help="Content as for PlanDefinition.actionDefinition A sub-action.")                    

class PlanDefinitionActionDefinition(models.Model):    
    _name = "hc.plan.definition.action.definition"    
    _description = "Plan Definition Action Definition"            

    plan_definition_id = fields.Many2one(
        comodel_name="hc.res.plan.definition", 
        string="Plan Definition", 
        help="Plan Definition associated with this Plan Definition Action Definition.")                    
    action_identifier_id = fields.Many2one(
        comodel_name="hc.plan.definition.action.definition.action.identifier", 
        string="Action Identifier", 
        help="Unique identifier.")                    
    label = fields.Char(
        string="Label", 
        help="User-visible label for the action (e.g. 1. or A.).")                    
    title = fields.Char(
        string="Title", 
        help="User-visible title.")                    
    description = fields.Char(
        string="Description", 
        help="Short description of the action.")                    
    text_equivalent = fields.Text(
        string="Text Equivalent", 
        help="Static text equivalent of the action, used if the dynamic aspects cannot be interpreted by the receiving system.")                    
    code_ids = fields.Many2many(
        comodel_name="hc.vs.action.code", 
        relation="plan_definition_action_definition_code_rel", 
        string="Codes", 
        help="The meaning of the action or its sub-actions.")                    
    documentation_ids = fields.One2many(
        comodel_name="hc.plan.definition.action.definition.documentation", 
        inverse_name="action_definition_id", 
        string="Documentation", 
        help="Supporting documentation for the intended performer of the action.")                    
    trigger_definition_ids = fields.One2many(
        comodel_name="hc.plan.definition.action.definition.trigger.definition", 
        inverse_name="action_definition_id", 
        string="Trigger Definitions", 
        help="When the action should be triggered.")                    
    timing_id = fields.Many2one(
        comodel_name="hc.plan.definition.action.definition.timing", 
        string="Timing", 
        help="When the action should take place.")                    
    participant_type_ids = fields.One2many(
        comodel_name="hc.plan.definition.action.definition.participant.type", 
        inverse_name="action_definition_id", 
        string="Participant Types", 
        help="The type of participant in the action.")                    
    type = fields.Selection(
        string="Type", 
        selection=[
            ("create", "Create"), 
            ("update", "Update"), 
            ("remove", "Remove"), 
            ("fire-event", "Fire Event")], 
        help="The type of action to perform (create, update, remove).")                    
    grouping_behavior = fields.Selection(
        string="Grouping Behavior", 
        selection=[
            ("visual-group", "Visual Group"), 
            ("logical-group", "Logical Group"), 
            ("sentence-group", "Sentence Group")], 
        help="Defines the grouping behavior for the action and its children.")
    selection_behavior = fields.Selection(
        string="Selection Behavior", 
        selection=[
            ("any", "Any"), 
            ("all", "All"), 
            ("all-or-none", "All Or None"), 
            ("exactly-one", "Exactly One"), 
            ("at-most-one", "At Most One"), 
            ("one-or-more", "One Or More")], 
        help="Defines the selection behavior for the action and its children.")
    required_behavior = fields.Selection(
        string="Required Behavior", 
        selection=[
            ("must", "Must"), 
            ("could", "Could"), 
            ("must-unless-documented", "Must Unless Documented")], 
        help="Defines the requiredness behavior for the action.")
    precheck_behavior = fields.Selection(
        string="Precheck Behavior", 
        selection=[
            ("yes", "Yes"), 
            ("no", "No")], 
        help="Defines whether the action should usually be preselected.")
    cardinality_behavior = fields.Selection(
        string="Cardinality Behavior", 
        selection=[
            ("single", "Single"), 
            ("multiple", "Multiple")], 
        help="Defines whether the action can be selected multiple times.")
    activity_definition_id = fields.Many2one(
        comodel_name="hc.res.activity.definition", 
        string="Activity Definition", 
        help="Description of the activity to be performed.")                    
    # transform_id = fields.Many2one(
    #     comodel_name="hc.res.structure.map", 
    #     string="Transform", 
    #     help="Transform to apply the template.")                    
    condition_ids = fields.One2many(
        comodel_name="hc.plan.definition.action.definition.condition", 
        inverse_name="action_definition_id", 
        string="Conditions", 
        help="Whether or not the action is applicable.")                    
    related_action_ids = fields.One2many(
        comodel_name="hc.plan.definition.action.definition.related.action", 
        inverse_name="action_definition_id", 
        string="Related Actions", 
        help="Relationship to another action.")                    
    dynamic_value_ids = fields.One2many(
        comodel_name="hc.plan.definition.action.definition.dynamic.value", 
        inverse_name="action_definition_id", 
        string="Dynamic Values", 
        help="Dynamic aspects of the definition.")                    
    action_definition_id = fields.Many2one(
        comodel_name="hc.plan.definition.action.definition", 
        string="Action Definition", 
        help="A sub-action.")                    

class PlanDefinitionActionDefinitionCondition(models.Model):    
    _name = "hc.plan.definition.action.definition.condition"    
    _description = "Plan Definition Action Definition Condition"            

    action_definition_id = fields.Many2one(
        comodel_name="hc.plan.definition.action.definition", 
        string="Action Definition", 
        help="Action Definition associated with this Plan Definition Action Definition Condition.")                    
    kind = fields.Selection(
        string="Kind", 
        required="True", 
        selection=[
            ("applicability", "Applicability"), 
            ("start", "Start"), 
            ("stop", "Stop")], 
        help="The kind of condition.")
    description = fields.Text(
        string="Description", 
        help="Natural language description of the condition.")                    
    language = fields.Char(
        string="Language", 
        help="Language of the expression.")                    
    expression = fields.Char(
        string="Expression", 
        help="Boolean-valued expression.")                    

class PlanDefinitionActionDefinitionRelatedAction(models.Model):    
    _name = "hc.plan.definition.action.definition.related.action"    
    _description = "Plan Definition Action Definition Related Action"            

    action_definition_id = fields.Many2one(
        comodel_name="hc.plan.definition.action.definition", 
        string="Action Definition", 
        help="Action Definition associated with this Plan Definition Action Definition Related Action.")                    
    action_identifier_id = fields.Many2one(
        comodel_name="hc.plan.defn.action.defn.related.action.action.identifier", 
        string="Action Identifier", 
        required="True", 
        help="Identifier of the related action.")
    relationship = fields.Selection(
        string="Relationship", 
        required="True", 
        selection=[
            ("before-start", "Before Start"), 
            ("before", "Before"), ("before-end", "Before End"), 
            ("concurrent-with-start", "Concurrent With Start"), 
            ("concurrent", "Concurrent"), 
            ("concurrent-with-end", "Concurrent With End"), 
            ("after-start", "After-Start"), ("after", "After"), 
            ("after-end", "After End")], 
        help="The relationship of this action to the related action.")
    offset = fields.Float(
        string="Offset", 
        help="Duration time offset for the relationship.")                    

class PlanDefinitionActionDefinitionDynamicValue(models.Model):    
    _name = "hc.plan.definition.action.definition.dynamic.value"    
    _description = "Plan Definition Action Definition Dynamic Value"            

    action_definition_id = fields.Many2one(
        comodel_name="hc.plan.definition.action.definition", 
        string="Action Definition", 
        help="Action Definition associated with this Plan Definition Action Definition Dynamic Value.")                    
    description = fields.Text(
        string="Description", 
        help="Natural language description of the dynamic value.")                    
    path = fields.Char(
        string="Path", 
        help="The path to the element to be set dynamically.")                    
    language = fields.Char(
        string="Language", 
        help="Language of the expression.")                    
    expression = fields.Text(
        string="Expression", 
        help="An expression that provides the dynamic value for the customization.")                    

class PlanDefinitionIdentifier(models.Model):    
    _name = "hc.plan.definition.identifier"    
    _description = "Plan Definition Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]    

    plan_definition_id = fields.Many2one(
        comodel_name="hc.res.plan.definition", 
        string="Plan Definition", 
        help="Plan Definition associated with this Plan Definition Identifier.")                    

class PlanDefinitionUseContext(models.Model):    
    _name = "hc.plan.definition.use.context"    
    _description = "Plan Definition Use Context"        
    _inherit = ["hc.basic.association", "hc.usage.context"]    

    plan_definition_id = fields.Many2one(
        comodel_name="hc.res.plan.definition", 
        string="Plan Definition", 
        help="Plan Definition associated with this Plan Definition Use Context.")                    

class PlanDefinitionContributor(models.Model):    
    _name = "hc.plan.definition.contributor"    
    _description = "Plan Definition Contributor"        
    _inherit = ["hc.basic.association"]    
    _inherits = {"hc.contributor": "contributor_id"}

    contributor_id = fields.Many2one(
        comodel_name="hc.contributor", 
        string="Contributor", 
        ondelete="restrict", 
        required="True", 
        help="Contributor associated with this Plan Definition Contributor.")                    
    plan_definition_id = fields.Many2one(
        comodel_name="hc.res.plan.definition", 
        string="Plan Definition", 
        help="Plan Definition associated with this Plan Definition Contributor.")                    

class PlanDefinitionContact(models.Model):    
    _name = "hc.plan.definition.contact"    
    _description = "Plan Definition Contact"        
    _inherit = ["hc.basic.association"]    
    _inherits = {"hc.contact.detail": "contact_id"}

    contact_id = fields.Many2one(
        comodel_name="hc.contact.detail", 
        string="Contact", 
        ondelete="restrict", 
        required="True", 
        help="Contact Detail associated with this Plan Definition Contact.")                    
    plan_definition_id = fields.Many2one(
        comodel_name="hc.res.plan.definition", 
        string="Plan Definition", 
        help="Plan Definition associated with this Plan Definition Contact.")                    

class PlanDefinitionRelatedArtifact(models.Model):    
    _name = "hc.plan.definition.related.artifact"    
    _description = "Plan Definition Related Artifact"        
    _inherit = ["hc.basic.association", "hc.related.artifact"]    

    plan_definition_id = fields.Many2one(
        comodel_name="hc.res.plan.definition", 
        string="Plan Definition", 
        help="Plan Definition associated with this Plan Definition Related Artifact.")                    

class PlanDefinitionLibrary(models.Model):    
    _name = "hc.plan.definition.library"    
    _description = "Plan Definition Library"        
    _inherit = ["hc.basic.association"]    

    plan_definition_id = fields.Many2one(
        comodel_name="hc.res.plan.definition", 
        string="Plan Definition", 
        help="Plan Definition associated with this Plan Definition Library.")                    
    library_id = fields.Many2one(
        comodel_name="hc.res.library", 
        string="Library", 
        help="Library associated with this Plan Definition Library.")                    

class PlanDefinitionActionDefinitionActionIdentifier(models.Model):    
    _name = "hc.plan.definition.action.definition.action.identifier"    
    _description = "Plan Definition Action Definition Action Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]    

class PlanDefinitionActionDefinitionDocumentation(models.Model):    
    _name = "hc.plan.definition.action.definition.documentation"    
    _description = "Plan Definition Action Definition Documentation"        
    _inherit = ["hc.basic.association", "hc.related.artifact"]    

    action_definition_id = fields.Many2one(
        comodel_name="hc.plan.definition.action.definition", 
        string="Action Definition", 
        help="Action Definition associated with this Plan Definition Action Definition Documentation.")                    

class PlanDefinitionActionDefinitionTriggerDefinition(models.Model):    
    _name = "hc.plan.definition.action.definition.trigger.definition"    
    _description = "Plan Definition Action Definition Trigger Definition"        
    _inherit = ["hc.basic.association", "hc.trigger.definition"]    

    action_definition_id = fields.Many2one(
        comodel_name="hc.plan.definition.action.definition", 
        string="Action Definition", 
        help="Action Definition associated with this Plan Definition Action Definition Trigger Definition.")                    

class PlanDefinitionActionDefinitionTiming(models.Model):    
    _name = "hc.plan.definition.action.definition.timing"    
    _description = "Plan Definition Action Definition Timing"        
    _inherit = ["hc.basic.association", "hc.timing"]    

    action_definition_id = fields.Many2one(
        comodel_name="hc.plan.definition.action.definition", 
        string="Action Definition", 
        help="Action Definition associated with this Plan Definition Action Definition Timing.")                    

class PlanDefinitionActionDefinitionParticipantType(models.Model):    
    _name = "hc.plan.definition.action.definition.participant.type"    
    _description = "Plan Definition Action Definition Participant Type"        
    _inherit = ["hc.basic.association"]    

    action_definition_id = fields.Many2one(
        comodel_name="hc.plan.definition.action.definition", 
        string="Action Definition", 
        help="Action Definition associated with this Plan Definition Action Definition Participant Type.")                    
    participant_type = fields.Selection(
        string="Participant Type", 
        selection=[
            ("patient", "Patient"), 
            ("practitioner", "Practitioner"), 
            ("related-person", "Related Person")], 
        help="The relationship of this action to the related action.")

class PlanDefnActionDefnRelatedActionActionIdentifier(models.Model):    
    _name = "hc.plan.defn.action.defn.related.action.action.identifier" 
    _description = "Plan Definition Action Definition Related Action Action Identifier"     
    _inherit = ["hc.basic.association", "hc.identifier"]
   

class PlanDefinitionTopic(models.Model):    
    _name = "hc.vs.plan.definition.topic"    
    _description = "Plan Definition Topic"        
    _inherit = ["hc.value.set.contains"]    
