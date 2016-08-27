# -*- coding: utf-8 -*-

from openerp import models, fields, api

class DiagnosticRequest(models.Model):    
    _name = "hc.res.diagnostic.request"    
    _description = "Diagnostic Request"

    identifier_ids = fields.One2many(comodel_name="hc.diagnostic.request.identifier", inverse_name="diagnostic_request_id", string="Identifiers", help="Identifiers assigned to this order.")                    
    definition_ids = fields.One2many(comodel_name="hc.diagnostic.request.definition", inverse_name="diagnostic_request_id", string="Definitions", help="Protocol or definition.")                    
    based_on_ids = fields.One2many(comodel_name="hc.diagnostic.request.based.on", inverse_name="diagnostic_request_id", string="Based On", help="What request fulfills.")                    
    replaces_ids = fields.One2many(comodel_name="hc.diagnostic.request.replaces", inverse_name="diagnostic_request_id", string="Replaces", help="What request replaces.")                    
    identifier_ids = fields.One2many(comodel_name="hc.diagnostic.request.identifier", inverse_name="diagnostic_request_id", string="Identifiers", help="Identifier of composite request.")                    
    status = fields.Selection(string="Diagnostic Request Status", selection=[("requested", "Requested"), ("received", "Received"), ("accepted", "Accepted"), ("in progress", "In Progress"), ("review", "Review"), ("completed", "Completed"), ("suspended", "Suspended"), ("rejected", "Rejected"), ("failed", "Failed")], help="The status of the order.")                    
    stage_id = fields.Many2one(comodel_name="hc.vs.diagnostic.request.stage", string="Diagnostic Request Stage", required="True", help="Whether the request is a proposal, plan, an original order or a reflex order.")
    # stage = fields.Selection(string="Diagnostic Request Stage", required="True", selection=[("proposal", "Proposal"), ("plan", "Plan"), ("original-order", "Original-Order"), ("reflex-order", "Reflex-Order")], help="proposal | plan | original-order | reflex-order.")                    
    code_id = fields.Many2one(comodel_name="hc.vs.diagnostic.request", string="Code", required="True", help="What’s being requested/ordered.")                    
    subject_type = fields.Selection(string="Subject Type", required="True", selection=[("patient", "Patient"), ("group", "Group"), ("location", "Location"), ("device", "Device")], help="Type of who and/or what test is about.")                    
    subject_name = fields.Char(string="Subject", compute="compute_subject_name", required="True", help="Who and/or what test is about.")                    
    subject_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Subject Patient", help="Patient who and/or what test is about.")
    subject_group_id = fields.Many2one(comodel_name="hc.res.group", string="Subject Group", help="Group who and/or what test is about.")
    subject_location_id = fields.Many2one(comodel_name="hc.res.location", string="Subject Location", help="Location who and/or what test is about.")
    subject_device_id = fields.Many2one(comodel_name="hc.res.device", string="Subject Device", help="Device who and/or what test is about.")                  
    context_type = fields.Selection(string="Context Type", required="True", selection=[("Encounter", "Encounter"), ("Episode Of Care", "Episode of Care")], help="Encounter or Episode during which request was created.")                    
    context_name = fields.Char(string="Context", compute="compute_context_name", required="True", help="Encounter or Episode during which request was created.")                    
    # context_encounter_id = fields.Many2one(
    #     comodel_name="hc.res.encounter", 
    #     string="Context Encounter", 
    #     help="Encounter during which request was created.")                    
    # context_episode_of_care_id = fields.Many2one(
    #     comodel_name="hc.res.episode.of.care", 
    #     string="Context Episode Of Care", 
    #     help="Episode Of Care during which request was created.")                    
    # encounter_id = fields.Many2one(
    #     comodel_name="hc.res.encounter", 
    #     string="Encounter", 
    #     help="The encounter that this diagnostic order is associated with.")                    
    occurence_type = fields.Selection(string="Occurence Type", required="True", selection=[("datetime", "Datetime"), ("period", "Period"), ("timing", "Timing")], help="Type of when testing should occur.")                    
    occurrence_name = fields.Char(string="Occurrence", compute="compute_occurrence_name", required="True", help="When testing should occur.")                    
    occurrence_datetime = fields.Datetime(string="Occurrence Datetime", help="dateTime when testing should occur.")                    
    occurence_start_date = fields.Datetime(string="Occurrence Start Date", help="Start of the when testing should occur.")                    
    occurence_end_date = fields.Datetime(string="Occurence End Date", help="End of the when testing should occur.")                    
    occurrence_timing = fields.Datetime(string="Occurrence Timing", help="Timing when testing should occur.")                    
    authored = fields.Datetime(string="Authored Date", help="Request signed.")                    
    requester_type = fields.Selection(string="Requester Type", required="True", selection=[("device", "Device"), ("practitioner", "Practitioner"), ("organization", "Organization")], help="Type of who/what is requesting diagnostics.")                    
    requester_name = fields.Char(string="Requester", compute="compute_requester_name", required="True", help="Who/what is requesting diagnostics.")                    
    requester_device_id = fields.Many2one(comodel_name="hc.res.device", string="Requester Device", help="Who/what is requesting diagnostics.")                    
    requester_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Requester Practitioner", help="Practitioner who/what is requesting diagnostics.")                    
    requester_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Requester Organization", help="Organization who/what is requesting diagnostics.")                    
    performer_type_id = fields.Many2one(comodel_name="hc.vs.participant.role", string="Performer Type", help="Performer role.")                    
    performer_type = fields.Selection(string="Performer Type", required="True", selection=[("Practitioner", "Practitioner"), ("Organization", "Organization"), ("Patient", "Patient"), ("Device", "Device"), ("RelatedPerson", "Relatedperson")], help="Type of requested perfomer.")                    
    performer_name = fields.Char(string="Performer", compute="compute_performer_name", required="True", help="Requested perfomer.")                    
    performer_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Performer Practitioner", help="Requested perfomer.")                    
    performer_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Performer Organization", help="Organization requested perfomer.")                    
    performer_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Performer Patient", help="Patient requested perfomer.")                    
    performer_device_id = fields.Many2one(comodel_name="hc.res.device", string="Performer Device", help="Device requested perfomer.")                    
    performer_related_person_id = fields.Many2one(comodel_name="hc.res.related.person", string="Performer Related Person", help="Related Person requested perfomer.")                    
    reason_ids = fields.One2many(comodel_name="hc.diagnostic.request.reason", inverse_name="diagnostic_request_id", string="Reasons", help="Explanation/Justification for test.")                    
    supporting_info_ids = fields.One2many(comodel_name="hc.diagnostic.request.supporting.info", inverse_name="diagnostic_request_id", string="Supporting Info", help="Additional clinical information.")     
    note_ids = fields.One2many(comodel_name="hc.diagnostic.request.note", inverse_name="diagnostic_request_id", string="Notes", help="Comments.")                    
    relevant_history_ids = fields.One2many(comodel_name="hc.diagnostic.request.relevant.history", inverse_name="diagnostic_request_id", string="Relevant Histories", help="Request provenance.")                    

class DiagnosticRequestIdentifier(models.Model):    
    _name = "hc.diagnostic.request.identifier"    
    _description = "Diagnostic Request Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]    

    diagnostic_request_id = fields.Many2one(comodel_name="hc.res.diagnostic.request", string="Diagnostic Request", help="Diagnostic Request associated with this diagnostic request identifier." )                    

class DiagnosticRequestBasedOn(models.Model):    
    _name = "hc.diagnostic.request.based.on"    
    _description = "Diagnostic Request Based On"        
    _inherit = ["hc.basic.association"]    
    
    diagnostic_request_id = fields.Many2one(comodel_name="hc.res.diagnostic.request", string="Diagnostic Request", help="Diagnostic Request associated with this diagnostic request based on." )                    
    based_on_type = fields.Selection(string="Based On Type", required="True", selection=[("string", "String"), ("code", "Code")], help="Type of what request fulfills.")                    
    based_on_name = fields.Char(string="Based On", compute="compute_based_on_name", required="True", help="What request fulfills.")                    
    based_on_string = fields.Char(string="Based On String", help="String what request fulfills.")                    
    based_on_diagnostic_request_id = fields.Many2one(comodel_name="hc.res.diagnostic.request", string="Based On Diagnostic Request", help="Diagnostic Request what request fulfills.")                    

class DiagnosticRequestDefinition(models.Model):    
    _name = "hc.diagnostic.request.definition"    
    _description = "Diagnostic Request Definition"        
    _inherit = ["hc.basic.association"]    
    
    diagnostic_request_id = fields.Many2one(comodel_name="hc.res.diagnostic.request", string="Diagnostic Request", help="Diagnostic Request associated with this diagnostic request definition." )                    
    definition_type = fields.Selection(string="Definition Type", required="True", selection=[("string", "String"), ("Diagnostic Request", "Diagnostic Request")], help="Type of protocol or definition.")                    
    definition_name = fields.Char(string="Definition", compute="compute_definition_name", required="True", help="Protocol or definition.")                    
    definition_string = fields.Char(string="Definition String", help="String protocol or definition.")                    
    definition_diagnostic_request_id = fields.Many2one(comodel_name="hc.res.diagnostic.request", string="Definition Diagnostic Request", help="Diagnostic Request protocol or definition.")     

class DiagnosticRequestNote(models.Model):    
    _name = "hc.diagnostic.request.note"    
    _description = "Diagnostic Request Note"        
    _inherit = ["hc.basic.association", "hc.annotation"]    
    
    diagnostic_request_id = fields.Many2one(comodel_name="hc.res.diagnostic.request", string="Diagnostic Request", help="Diagnostic Request associated with this diagnostic request note." )                    

class DiagnosticRequestRelevantHistory(models.Model):    
    _name = "hc.diagnostic.request.relevant.history"   
    _description = "Diagnostic Request Relevant History"        
    _inherit = ["hc.basic.association"]    
    
    diagnostic_request_id = fields.Many2one(comodel_name="hc.res.diagnostic.request", string="Diagnostic Request", help="Diagnostic Request associated with this diagnostic request relevant history." )                    
    # relevant_history_id = fields.Many2one(
    #     comodel_name="hc.res.provenance", 
    #     string="Relevant History", 
    #     help="Provenance associated with this diagnostic request relevant history." )                    

class DiagnosticRequestReplaces(models.Model):    
    _name = "hc.diagnostic.request.replaces"    
    _description = "Diagnostic Request Replaces"        
    _inherit = ["hc.basic.association"]

    diagnostic_request_id = fields.Many2one(comodel_name="hc.res.diagnostic.request", string="Diagnostic Request", help="Diagnostic Request associated with this diagnostic request replaces." )                    
    replaces_type = fields.Selection(string="Replaces Type", required="True", selection=[("string", "String"), ("Diagnostic Request", "Diagnostic Request")], help="Type of what request replaces.")                    
    replaces_name = fields.Char(string="Replaces", compute="compute_replaces_name", required="True", help="What request replaces.")                    
    replaces_string = fields.Char(string="Replaces String", help="String what request replaces.")                    
    replaces_diagnostic_request_id = fields.Many2one(comodel_name="hc.res.diagnostic.request", string="Replaces Diagnostic Request", help="Diagnostic Request what request replaces.")                    

class DiagnosticRequestSupportingInfo(models.Model):    
    _name = "hc.diagnostic.request.supporting.info"    
    _description = "Diagnostic Request Supporting Information"        
    _inherit = ["hc.basic.association"]    

    diagnostic_request_id = fields.Many2one(comodel_name="hc.res.diagnostic.request", string="Diagnostic Request", help="Diagnostic Request associated with this diagnostic request supporting information." )                    
    supporting_info_type = fields.Selection(string="Supporting Info Type", required="True", selection=[("string", "String"), ("Diagnostic Request", "Diagnostic Request")], help="Type of additional clinical information.")                    
    supporting_info_name = fields.Char(string="Supporting Info", compute="compute_supporting_info_name", required="True", help="Additional clinical information.")                    
    supporting_info_string = fields.Char(string="Supporting Info String", help="String additional clinical information.")                    
    supporting_info_diagnostic_request_id = fields.Many2one(comodel_name="hc.res.diagnostic.request", string="Supporting Info Diagnostic Request", help="Diagnostic Request additional clinical information.")                    

class DiagnosticRequestReason(models.Model): 
    _name = "hc.diagnostic.request.reason"  
    _description = "Diagnostic Request Reason"      
    _inherit = ["hc.basic.association"]

    diagnostic_request_id = fields.Many2one(comodel_name="hc.res.diagnostic.request", string="Diagnostic Request", help="Diagnostic Request associated with this diagnostic request reason." )                    
    reason_id = fields.Many2one(comodel_name="hc.vs.condition.code", string="Reason", help="Explanation/Justification for test.")                    

class DiagnosticRequest(models.Model):    
    _name = "hc.vs.diagnostic.request"    
    _description = "Diagnostic Request"        
    _inherit = ["hc.value.set.contains"]      
  
class DiagnosticRequestStage(models.Model): 
    _name = "hc.vs.diagnostic.request.stage"    
    _description = "Diagnostic Request Stage"       
    _inherit = ["hc.value.set.contains"]
