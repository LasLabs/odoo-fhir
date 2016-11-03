# -*- coding: utf-8 -*-

from openerp import models, fields, api

class DiagnosticRequest(models.Model):    
    _name = "hc.res.diagnostic.request"    
    _description = "Diagnostic Request"

    identifier_ids = fields.One2many(
        comodel_name="hc.diagnostic.request.identifier", 
        inverse_name="diagnostic_request_id", 
        string="Identifiers", 
        help="Identifiers assigned to this order.")                    
    definition_ids = fields.One2many(
        comodel_name="hc.diagnostic.request.definition", 
        inverse_name="diagnostic_request_id", 
        string="Definitions", 
        help="Protocol or definition.")                    
    based_on_ids = fields.One2many(
        comodel_name="hc.diagnostic.request.based.on", 
        inverse_name="diagnostic_request_id", 
        string="Based On", 
        help="What request fulfills.")                    
    replaces_ids = fields.One2many(
        comodel_name="hc.diagnostic.request.replaces", 
        inverse_name="diagnostic_request_id", 
        string="Replaces", 
        help="What request replaces.")                    
    requisition_id = fields.Many2one(
        comodel_name="hc.diagnostic.request.requisition", 
        string="Requisition Identifier", 
        help="Identifier of composite request.")                    
    status = fields.Selection(
        string="Diagnostic Request Status", 
        selection=[
            ("requested", "Requested"), 
            ("received", "Received"), 
            ("accepted", "Accepted"), 
            ("in progress", "In Progress"), 
            ("review", "Review"), 
            ("completed", "Completed"), 
            ("suspended", "Suspended"), 
            ("rejected", "Rejected"), 
            ("failed", "Failed")], 
        help="The status of the order.")                    
    stage_id = fields.Many2one(
        comodel_name="hc.vs.diagnostic.request.stage", 
        string="Diagnostic Request Stage", 
        required="True", 
        help="Whether the request is a proposal, plan, an original order or a reflex order.")
    # stage = fields.Selection(string="Diagnostic Request Stage", required="True", selection=[("proposal", "Proposal"), ("plan", "Plan"), ("original-order", "Original-Order"), ("reflex-order", "Reflex-Order")], help="proposal | plan | original-order | reflex-order.")                    
    code_id = fields.Many2one(
        comodel_name="hc.vs.diagnostic.request", 
        string="Code", 
        required="True", 
        help="What's being requested/ordered.")                    
    subject_type = fields.Selection(
        string="Subject Type", 
        required="True", 
        selection=[
            ("patient", "Patient"), 
            ("group", "Group"), 
            ("location", "Location"), 
            ("device", "Device")], 
        help="Type of who and/or what test is about.")                    
    subject_name = fields.Char(
        string="Subject", 
        compute="compute_subject_name", 
        help="Who and/or what test is about.")                    
    subject_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Subject Patient", 
        help="Patient who and/or what test is about.")
    subject_group_id = fields.Many2one(
        comodel_name="hc.res.group", 
        string="Subject Group", 
        help="Group who and/or what test is about.")
    subject_location_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Subject Location", 
        help="Location who and/or what test is about.")
    subject_device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Subject Device", 
        help="Device who and/or what test is about.")                  
    context_type = fields.Selection(
        string="Context Type", 
        selection=[
            ("Encounter", "Encounter"), 
            ("Episode Of Care", "Episode of Care")], 
        help="Encounter or Episode during which request was created.")                    
    context_name = fields.Char(
        string="Context", 
        compute="compute_context_name", 
        help="Encounter or Episode during which request was created.")
    context_encounter_id = fields.Many2one(
        comodel_name="hc.res.encounter", 
        string="Context Encounter", 
        help="Encounter during which request was created.")                    
    context_episode_of_care_id = fields.Many2one(
        comodel_name="hc.res.episode.of.care", 
        string="Context Episode Of Care", 
        help="Episode Of Care during which request was created.")                                       
    occurence_type = fields.Selection(
        string="Occurence Type", 
        selection=[
            ("datetime", "Datetime"), 
            ("period", "Period"), 
            ("timing", "Timing")], 
        help="Type of when testing should occur.")                    
    occurrence_name = fields.Char(
        string="Occurrence", 
        compute="compute_occurrence_name", 
        help="When testing should occur.")             
    occurrence_datetime = fields.Datetime(
        string="Occurrence Datetime", 
        help="dateTime when testing should occur.")                    
    occurence_start_date = fields.Datetime(
        string="Occurrence Start Date", 
        help="Start of the when testing should occur.")                    
    occurence_end_date = fields.Datetime(
        string="Occurence End Date", 
        help="End of the when testing should occur.")                    
    occurrence_timing_id = fields.Many2one(
        comodel_name="hc.diagnostic.request.occurrence.timing", 
        string="Occurrence Timing", 
        help="Timing when testing should occur.")             
    authored = fields.Datetime(string="Authored Date", 
        help="Date request signed.")                   
    requester_type = fields.Selection(
        string="Requester Type", 
        selection=[
            ("device", "Device"), 
            ("practitioner", "Practitioner"), 
            ("organization", "Organization")], 
        help="Type of who/what is requesting diagnostics.")                    
    requester_name = fields.Char(
        string="Requester", 
        compute="compute_requester_name", 
        help="Who/what is requesting diagnostics.")                    
    requester_device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Requester Device", 
        help="Device who/what is requesting diagnostics.")
    requester_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Requester Practitioner", 
        help="Practitioner who/what is requesting diagnostics.")                    
    requester_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Requester Organization", 
        help="Organization who/what is requesting diagnostics.")                     
    performer_type_id = fields.Many2one(
        comodel_name="hc.vs.participant.role", 
        string="Performer Type", 
        help="Performer role.")                    
    requested_performer_type = fields.Selection(
        string="Requested Performer Type", 
        selection=[
            ("Practitioner", "Practitioner"), 
            ("Organization", "Organization"), 
            ("Patient", "Patient"), 
            ("Device", "Device"), 
            ("Related Person", "Related Person")], 
        help="Type of requested perfomer.")
    requested_performer_name = fields.Char(
        string="Requested Performer", 
        compute="_compute_requested_performer_name", 
        store="True", 
        help="Requested perfomer.")
    requested_performer_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Requested Performer Practitioner", 
        help="Practitioner requested perfomer.")
    requested_performer_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Requested Performer Organization", 
        help="Organization requested perfomer.")
    requested_performer_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Requested Performer Patient", 
        help="Patient requested perfomer.")
    requested_performer_device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Requested Performer Device", 
        help="Device requested perfomer.")
    requested_performer_related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Requested Performer Related Person", 
        help="Related Person requested perfomer.")
    reason_ids = fields.One2many(
        comodel_name="hc.diagnostic.request.reason", 
        inverse_name="diagnostic_request_id", 
        string="Reasons", 
        help="Explanation/Justification for test.")                    
    supporting_info_ids = fields.One2many(
        comodel_name="hc.diagnostic.request.supporting.info", 
        inverse_name="diagnostic_request_id", 
        string="Supporting Info", 
        help="Additional clinical information.")     
    note_ids = fields.One2many(
        comodel_name="hc.diagnostic.request.note", 
        inverse_name="diagnostic_request_id", 
        string="Notes", 
        help="Comments.")                    
    relevant_history_ids = fields.One2many(
        comodel_name="hc.diagnostic.request.relevant.history", 
        inverse_name="diagnostic_request_id", 
        string="Relevant Histories", 
        help="Request provenance.")                    

class DiagnosticRequestIdentifier(models.Model):    
    _name = "hc.diagnostic.request.identifier"    
    _description = "Diagnostic Request Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]    

    diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Diagnostic Request", 
        help="Diagnostic Request associated with this Diagnostic Request Identifier.")                    

class DiagnosticRequestRequisition(models.Model): 
    _name = "hc.diagnostic.request.requisition"  
    _description = "Diagnostic Request Requisition"      
    _inherit = ["hc.basic.association", "hc.identifier"]

    diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Diagnostic Request", 
        help="Diagnostic Request associated with this Diagnostic Request Requisition." )              

class DiagnosticRequestBasedOn(models.Model):    
    _name = "hc.diagnostic.request.based.on"    
    _description = "Diagnostic Request Based On"        
    _inherit = ["hc.basic.association"]    
    
    diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Diagnostic Request", 
        help="Diagnostic Request associated with this Diagnostic Request Based On.")                    
    based_on_type = fields.Selection(
        string="Based On Type", 
        selection=[
            ("string", "String"), 
            ("code", "Code")], 
        help="Type of what request fulfills.")                    
    based_on_name = fields.Char(
        string="Based On", 
        compute="compute_based_on_name", 
        help="What request fulfills.")                    
    based_on_string = fields.Char(
        string="Based On String", 
        help="String of what request fulfills.")
    based_on_code_id = fields.Many2one(
        comodel_name="hc.vs.resource.type", 
        string="Based On Code", 
        help="Resource type of what request fulfills.")

class DiagnosticRequestDefinition(models.Model):    
    _name = "hc.diagnostic.request.definition"    
    _description = "Diagnostic Request Definition"        
    _inherit = ["hc.basic.association"]    
    
    diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Diagnostic Request", 
        help="Diagnostic Request associated with this Diagnostic Request Definition.")                    
    definition_type = fields.Selection(
        string="Definition Type", 
        selection=[
            ("string", "String"), 
            ("code", "Code")], 
        help="Type of protocol or definition.")                    
    definition_name = fields.Char(
        string="Definition", 
        compute="compute_definition_name", 
        help="Protocol or definition.")                    
    definition_string = fields.Char(
        string="Definition String", 
        help="String of protocol or definition.")
    definition_code_id = fields.Many2one(
        comodel_name="hc.vs.resource.type", 
        string="Definition Code", 
        help="Resource type of protocol or definition.")

class DiagnosticRequestNote(models.Model):    
    _name = "hc.diagnostic.request.note"    
    _description = "Diagnostic Request Note"        
    _inherit = ["hc.basic.association", "hc.annotation"]    
    
    diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Diagnostic Request", 
        help="Diagnostic Request associated with this Diagnostic Request Note.")                    

class DiagnosticRequestRelevantHistory(models.Model):    
    _name = "hc.diagnostic.request.relevant.history"   
    _description = "Diagnostic Request Relevant History"        
    _inherit = ["hc.basic.association"]    
    
    diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Diagnostic Request", 
        help="Diagnostic Request associated with this Diagnostic Request Relevant History.")                    
    relevant_history_id = fields.Many2one(
        comodel_name="hc.res.provenance", 
        string="Relevant History", 
        help="Provenance associated with this Diagnostic Request Relevant History.")                    

class DiagnosticRequestReplaces(models.Model):    
    _name = "hc.diagnostic.request.replaces"    
    _description = "Diagnostic Request Replaces"        
    _inherit = ["hc.basic.association"]

    diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Diagnostic Request", 
        help="Diagnostic Request associated with this Diagnostic Request Replaces.")                    
    replaces_type = fields.Selection(
        string="Replaces Type", 
        selection=[
            ("string", "String"), 
            ("code", "Code")], 
        help="Type of what request replaces.")                    
    replaces_name = fields.Char(
        string="Replaces", 
        compute="compute_replaces_name", 
        help="What request replaces.")                    
    replaces_string = fields.Char(
        string="Replaces String", 
        help="String of what request replaces.")
    replaces_code_id = fields.Many2one(
        comodel_name="hc.vs.resource.type", 
        string="Replaces Code", 
        help="Resource type of what request replaces.")
                   
class DiagnosticRequestSupportingInfo(models.Model):    
    _name = "hc.diagnostic.request.supporting.info"    
    _description = "Diagnostic Request Supporting Information"        
    _inherit = ["hc.basic.association"]    

    diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Diagnostic Request", 
        help="Diagnostic Request associated with this Diagnostic Request Supporting Information.")                    
    supporting_info_type = fields.Selection(
        string="Supporting Info Type", 
        selection=[
            ("string", "String"), 
            ("code", "Code")], 
        help="Type of additional clinical information.")                    
    supporting_info_name = fields.Char(
        string="Supporting Info", 
        compute="compute_supporting_info_name", 
        help="Additional clinical information.")                    
    supporting_info_string = fields.Char(
        string="Supporting Info String", 
        help="String of additional clinical information.")
    supporting_info_code_id = fields.Many2one(
        comodel_name="hc.vs.resource.type", 
        string="Supporting Info Code", 
        help="Resource type of additional clinical information.")

class DiagnosticRequestReason(models.Model): 
    _name = "hc.diagnostic.request.reason"  
    _description = "Diagnostic Request Reason"      
    _inherit = ["hc.basic.association"]

    diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Diagnostic Request", 
        help="Diagnostic Request associated with this Diagnostic Request Reason.")                    
    reason_id = fields.Many2one(
        comodel_name="hc.vs.condition.code", 
        string="Reason", 
        help="Explanation/Justification for test.")                    

class DiagnosticRequestOccurrenceTiming(models.Model):  
    _name = "hc.diagnostic.request.occurrence.timing"    
    _description = "Diagnostic Request Occurrence Timing"       
    _inherit = ["hc.basic.association", "hc.timing"]

class DiagnosticRequest(models.Model):    
    _name = "hc.vs.diagnostic.request"    
    _description = "Diagnostic Request"        
    _inherit = ["hc.value.set.contains"]      
  
class DiagnosticRequestStage(models.Model): 
    _name = "hc.vs.diagnostic.request.stage"    
    _description = "Diagnostic Request Stage"       
    _inherit = ["hc.value.set.contains"]

# External Reference

# class Procedure(models.Model):  
#     _inherit = "hc.res.procedure"

#     request_diagnostic_request_id = fields.Many2one(
#         comodel_name="hc.res.diagnostic.request", 
#         string="Request Diagnostic Request", 
#         help="Diagnostic Request for this procedure.")

# class SpecimenRequest(models.Model):    
#     _inherit = "hc.specimen.request"
    
#     request_diagnostic_request_id = fields.Many2one(
#         comodel_name="hc.res.diagnostic.request", 
#         string="Request Diagnostic Request", 
#         help="Diagnostic Request why the specimen was collected.")