# -*- coding: utf-8 -*-

from openerp import models, fields, api

class RequestGroup(models.Model):    
    _name = "hc.res.request.group"    
    _description = "Request Group"        

    identifier_id = fields.Many2one(
        comodel_name="hc.request.group.identifier", 
        string="Identifier", 
        help="Business identifier.")                
    subject_type = fields.Selection(
        string="Subject Type", 
        selection=[
            ("Patient", "Patient"), 
            ("Group", "Group")], 
        help="Type of subject of the request group.")                
    subject_name = fields.Char(
        string="Subject", 
        compute="_compute_subject_name", 
        store="True", 
        help="Subject of the request group.")                
    subject_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Subject Patient", 
        help="Patient subject of the request group.")                
    subject_group_id = fields.Many2one(
        comodel_name="hc.res.group", 
        string="Subject Group", 
        help="Group subject of the request group.")                
    context_type = fields.Selection(
        string="Context Type", 
        selection=[
            ("Encounter", "Encounter"), 
            ("Episode Of Care", "Episode Of Care")], 
        help="Type of Encounter or Episode for the request group.")                
    context_name = fields.Char(
        string="Context", 
        compute="_compute_context_name", 
        store="True", 
        help="Encounter or Episode for the request group.")                
    context_encounter_id = fields.Many2one(
        comodel_name="hc.res.encounter", 
        string="Context Encounter", 
        help="Encounter for the request group.")                
    context_episode_of_care_id = fields.Many2one(
        comodel_name="hc.res.episode.of.care", 
        string="Context Episode Of Care", 
        help="Episode Of Care for the request group.")                
    occurrence_date_time = fields.Datetime(
        string="Occurrence Date Time", 
        help="When the request group was authored.")                
    author_type = fields.Selection(
        string="Author Type", 
        selection=[
            ("Device", "Device"), 
            ("Practitioner", "Practitioner")], 
        help="Type of device or practitioner that authored the request group.")                
    author_name = fields.Char(
        string="Author", 
        compute="_compute_author_name", 
        store="True", 
        help="Device or practitioner that authored the request group.")                
    author_device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Author Device", 
        help="Device that authored the request group.")                
    author_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Author Practitioner", 
        help="Practitioner that authored the request group.")                
    reason_type = fields.Selection(
        string="Reason Type", 
        selection=[
            ("code", "Code"), 
            ("string", "String"),
            ("Resource Type", "Resource Type")], 
        help="Type of reason for the request group.")                
    reason_name = fields.Char(
        string="Reason", 
        compute="_compute_reason_name", 
        store="True", help="Reason for the request group.")                
    reason_code_id = fields.Many2one(
        comodel_name="hc.vs.request.group.reason", 
        string="Reason Code", 
        help="Code of reason for the request group.")                
    reason_string = fields.Char(
        string="Reason String", 
        help="String of reason for the request group.")                
    reason_resource_id = fields.Many2one(
        comodel_name="hc.vs.resource.type", 
        string="Reason Resource", 
        help="Resource type of reason for the request group.")

    note_ids = fields.One2many(
        comodel_name="hc.request.group.note", 
        inverse_name="request_group_id", 
        string="Notes", 
        help="Additional notes about the response.")                
    action_ids = fields.One2many(
        comodel_name="hc.request.group.action", 
        inverse_name="request_group_id", 
        string="Action", 
        help="Proposed actions, if any.")                

class RequestGroupAction(models.Model):    
    _name = "hc.request.group.action"    
    _description = "Request Group Action"        

    request_group_id = fields.Many2one(
        comodel_name="hc.res.request.group", 
        string="Request Group", 
        help="Request Group associated with this Request Group Action.")                
    action_identifier_id = fields.Many2one(
        comodel_name="hc.request.group.action.action.identifier", 
        string="Action Identifier", 
        help="Unique identifier.")                
    label = fields.Char(
        string="Label", 
        help="User-visible label for the action (e.g. 1. or A.).")                
    title = fields.Char(
        string="Title", 
        help="User-visible title.")                
    description = fields.Text(
        string="Description", 
        help="Short description of the action.")                
    text_equivalent = fields.Text(
        string="Text Equivalent", 
        help="Static text equivalent of the action, used if the dynamic aspects cannot be interpreted by the receiving system.")                
    code_ids = fields.Many2many(
        comodel_name="hc.vs.action.code", 
        relation="request_group_action_code_rel", 
        string="Codes", 
        help="The meaning of the action or its sub-actions.")                
    documentation_ids = fields.One2many(
        comodel_name="hc.request.group.action.documentation", 
        inverse_name="action_id", 
        string="Documentation", 
        help="Supporting documentation for the intended performer of the action.")                
    timing_type = fields.Selection(
        string="Timing Type", selection=[
            ("dateTime", "Datetime"), 
            ("Period", "Period"), 
            ("Duration", "Duration"), 
            ("Range", "Range"), 
            ("Timing", "Timing")], 
        help="Type of when the action should take place.")              
    timing_name = fields.Char(
        string="Timing", 
        compute="_compute_timing_name", 
        store="True", 
        help="When the action should take place.")                
    timing_datetime = fields.Datetime(
        string="Timing Datetime", 
        help="When the action should take place.")                
    timing_start_date = fields.Datetime(
        string="Timing Start Date", 
        help="Start of when the action should take place.")                
    timing_end_date = fields.Datetime(
        string="Timing End Date", 
        help="End of when the action should take place.")                
    timing_duration = fields.Float(
        string="Timing Duration", 
        help="Duration when the action should take place.")                
    timing_duration_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Timing Duration UOM", 
        help="Timing unit of measure.")                
    timing_range_low = fields.Float(
        string="Timing Range Low", 
        help="Low limit of when the action should take place.")                
    timing_range_high = fields.Float(
        string="Timing Range High", 
        help="High limit of when the action should take place.")                
    timing_range_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Timing Range UOM", 
        help="Timing unit of measure.")                
    timing_id = fields.Many2one(
        comodel_name="hc.request.group.action.timing", 
        string="Timing", 
        help="When the action should take place.")                
    participant_ids = fields.One2many(
        comodel_name="hc.request.group.action.participant", 
        inverse_name="action_id", 
        string="Participants", 
        help="Participant.")                
    type = fields.Selection(
        string="Type", 
        selection=[
            ("create", "Create"), 
            ("update", "Update"), 
            ("remove", "Remove"), 
            ("fire-event", "Fire-Event")], 
        help="The type of action to perform (create, update, remove).")                
    grouping_behavior = fields.Selection(
        string="Grouping Behavior", 
        selection=[
            ("visual-group", "Visual-Group"), 
            ("logical-group", "Logical-Group"), 
            ("sentence-group", "Sentence-Group")], 
        help="Defines the grouping behavior for the action and its children.")                
    selection_behavior = fields.Selection(
        string="Selection Behavior", 
        selection=[
            ("any", "Any"), 
            ("all", "All"), 
            ("all-or-none", "All-Or-None"), 
            ("exactly-one", "Exactly-One"), 
            ("at-most-one", "At-Most-One"), 
            ("one-or-more", "One-Or-More")], 
        help="Defines the selection behavior for the action and its children.")                
    required_behavior = fields.Selection(
        string="Required Behavior", 
        selection=[
            ("must", "Must"), 
            ("could", "Could"), 
            ("must-unless-documented", "Must-Unless-Documented")], 
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
    resource_string = fields.Char(
        string="Resource String", 
        help="String of the target of the action.")                
    resource_code_id = fields.Many2one(
        comodel_name="hc.vs.resource.type", 
        string="Resource Code", 
        help="Code of the target of the action.")                
    condition_ids = fields.One2many(
        comodel_name="hc.request.group.action.condition", 
        inverse_name="action_id", 
        string="Condition", 
        help="Whether or not the action is applicable.")
    related_action_ids = fields.One2many(
        comodel_name="hc.request.group.action.related.action", 
        inverse_name="action_id", 
        string="Related Action", 
        help="Relationship to another action.")
                
class RequestGroupActionCondition(models.Model):    
    _name = "hc.request.group.action.condition"    
    _description = "Request Group Action Condition"        

    action_id = fields.Many2one(
        comodel_name="hc.request.group.action", 
        string="Action", 
        help="Proposed actions, if any.")                
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
    language = fields.Text(
        string="Language", 
        help="Language of the expression.")                
    expression = fields.Text(
        string="Expression", 
        help="Boolean-valued expression.")                

class RequestGroupActionRelatedAction(models.Model):    
    _name = "hc.request.group.action.related.action"    
    _description = "Request Group Action Related Action"        

    action_id = fields.Many2one(
        comodel_name="hc.request.group.action", 
        string="Action", 
        help="Proposed actions, if any.")                
    action_identifier_id = fields.Many2one(
        comodel_name="hc.request.group.action.related.action.action.identifier", 
        string="Action Identifier", required="True", 
        help="Identifier of the related action.")                
    relationship = fields.Selection(
        string="Relationship", 
        required="True", 
        selection=[
            ("before-start", "Before-Start"), 
            ("before", "Before"), 
            ("before-end", "Before-End"), 
            ("concurrent-with-start", "Concurrent-With-Start"), 
            ("concurrent", "Concurrent"), 
            ("concurrent-with-end", "Concurrent-With-End"), 
            ("after-start", "After-Start"), 
            ("after", "After"), 
            ("after-end", "After-End")], 
            help="The relationship of this action to the related action.")                
    offset_type = fields.Selection(
        string="Offset Type", 
        selection=[
            ("Duration", "Duration"), 
            ("Range", "Range")], 
            help="Type of time offset for the relationship.")                
    offset_name = fields.Char(
        string="Offset", 
        compute="_compute_offset_name", 
        store="True", 
        help="Time offset for the relationship.")                
    offset_duration = fields.Float(
        string="Offset Duration", 
        help="Duration time offset for the relationship.")                
    offset_duration_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Offset Duration UOM", 
        help="Offset unit of measure.")                
    offset_range_low = fields.Float(
        string="Offset Range Low", 
        help="Low limit of time offset for the relationship.")                
    offset_range_high = fields.Float(
        string="Offset Range High", 
        help="High limit of time offset for the relationship.")                
    offset_range_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Offset Range UOM", 
        help="Offset unit of measure.")                

class RequestGroupNote(models.Model):    
    _name = "hc.request.group.note"    
    _description = "Request Group Note"        
    _inherit = ["hc.basic.association", "hc.annotation"]

    request_group_id = fields.Many2one(
        comodel_name="hc.res.request.group", 
        string="Request Group", 
        help="Request Group associated with this Request Group Note.")                

class RequestGroupActionDocumentation(models.Model):    
    _name = "hc.request.group.action.documentation"    
    _description = "Request Group Action Documentation"        
    _inherit = ["hc.basic.association", "hc.related.artifact"]

    action_id = fields.Many2one(
        comodel_name="hc.request.group.action", 
        string="Action", 
        help="Action associated with this Request Group Action Documentation.")                

class RequestGroupActionParticipant(models.Model):    
    _name = "hc.request.group.action.participant"    
    _description = "Request Group Action Participant"        
    _inherit = ["hc.basic.association"]

    action_id = fields.Many2one(
        comodel_name="hc.request.group.action", 
        string="Action", 
        help="Action associated with this Request Group Action Participant.")                
    participant_type = fields.Selection(
        string="Participant Type", 
        selection=[
            ("Patient", "Patient"), 
            ("Group", "Group")], 
        help="Type of Participant.")                
    participant_name = fields.Char(
        string="Participant", 
        compute="_compute_participant_name", 
        store="True", 
        help="Participant.")                
    participant_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Participant Patient", 
        help="Patient that authored the request group.")                
    participant_person_id = fields.Many2one(
        comodel_name="hc.res.person", 
        string="Participant Person", 
        help="Person that authored the request group.")                
    participant_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Participant Practitioner", 
        help="Practitioner that authored the request group.")                
    participant_related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Participant Related Person", 
        help="Related Person that authored the request group.")                

class RequestGroupIdentifier(models.Model):    
    _name = "hc.request.group.identifier"    
    _description = "Request Group Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

class RequestGroupActionActionIdentifier(models.Model):    
    _name = "hc.request.group.action.action.identifier"    
    _description = "Request Group Action Action Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

class RequestGroupActionTiming(models.Model):    
    _name = "hc.request.group.action.timing"    
    _description = "Request Group Action Timing"        
    _inherit = ["hc.basic.association", "hc.timing"]

class RequestGroupActionRelatedActionActionIdentifier(models.Model):    
    _name = "hc.request.group.action.related.action.action.identifier"    
    _description = "Request Group Action Related Action Action Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

class ActionCode(models.Model):    
    _name = "hc.vs.action.code"    
    _description = "Action Code"        
    _inherit = ["hc.value.set.contains"]

class RequestGroupReason(models.Model):    
    _name = "hc.vs.request.group.reason"    
    _description = "Request Group Reason"        
    _inherit = ["hc.value.set.contains"]
