# -*- coding: utf-8 -*-

from openerp import models, fields, api

class DeviceUseRequest(models.Model):    
    _name = "hc.res.device.use.request"    
    _description = "Device Use Request"        

    identifier_ids = fields.One2many(comodel_name="hc.device.use.request.identifier", inverse_name="device_use_request_id", string="Identifiers", help="Request identifier.")                
    definition_ids = fields.One2many(comodel_name="hc.device.use.request.definition", inverse_name="device_use_request_id", string="Definitions", help="Protocol or definition.")                
    based_on_ids = fields.One2many(comodel_name="hc.device.use.request.based.on", inverse_name="device_use_request_id", string="Based On", help="What request fulfills.")                
    replaces_ids = fields.One2many(comodel_name="hc.device.use.request.replaces", inverse_name="device_use_request_id", string="Replaces", help="What request replaces.")                
    requisition_identifier_id = fields.Many2one(comodel_name="hc.device.use.request.requisition.identifier", string="Requisition Identifier", help="Identifier of composite request.")                
    status = fields.Selection(string="Device Use Request Status", selection=[("proposed", "Proposed"), ("planned", "Planned"), ("requested", "Requested"), ("received", "Received"), ("accepted", "Accepted"), ("in-progress", "In-Progress"), ("completed", "Completed"), ("suspended", "Suspended"), ("rejected", "Rejected") ], help="The status of the request.")                
    stage_id = fields.Many2one(comodel_name="hc.vs.request.stage", string="Device Use Request Stage", required="True", help="Whether the request is a proposal, plan, an original order or a reflex order.")                
    device_type = fields.Selection(string="Device Type", required="True", selection=[("Device", "Device"), ("Codeable Concept", "Codeable Concept")], help="Type of device requested.")                
    device_name = fields.Char(string="Device", compute="_compute_device_name", store="True", help="Device requested.")                
    device_id = fields.Many2one(comodel_name="hc.res.device", string="Device", help="Device requested.")                
    device_code_id = fields.Many2one(comodel_name="hc.vs.device.kind", string="Device Code", help="Code of device requested.")                
    subject_type = fields.Selection(string="Subject Type", required="True", selection=[("Patient", "Patient"), ("Group", "Group"), ("Location", "Location"), ("Device", "Device")], help="Type of focus of request.")                
    subject_name = fields.Char(string="Subject", compute="_compute_subject_name", store="True", help="Focus of request.")                
    subject_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Subject Patient", help="Patient focus of request.")                
    subject_group_id = fields.Many2one(comodel_name="hc.res.group", string="Subject Group Date", help="Group focus of request.")                
    subject_location_id = fields.Many2one(comodel_name="hc.res.location", string="Subject Location Date", help="Location focus of request.")                
    subject_device_id = fields.Many2one(comodel_name="hc.res.device", string="Subject Device Date", help="Device focus of request.")                
    context_type = fields.Selection(string="Context Type", selection=[("Encounter", "Encounter"), ("Episode Of Care", "Episode Of Care")], help="Encounter or Episode motivating request.")                
    context_name = fields.Char(string="Context", compute="_compute_context_name", store="True", help="Encounter or Episode motivating request.")                
    context_encounter_id = fields.Many2one(comodel_name="hc.res.encounter", string="Context Encounter", help="Encounter motivating request.")                
    body_site_id = fields.Many2one(comodel_name="hc.res.body.site", string="Body Site", help="BodySite motivating request.")                
    occurence_type = fields.Selection(string="Occurence Type", selection=[("dateTime", "Datetime"), ("Period", "Period"), ("Timing", "Timing")], help="Type of desired time or schedule for use.")                
    occurrence_name = fields.Char(string="Occurrence", compute="_compute_occurrence_name", store="True", help="Desired time or schedule for use.")                
    occurrence_datetime = fields.Datetime( string="Occurrence Datetime", help="dateTime desired time or schedule for use.")                
    occurrence_start_date = fields.Datetime(string="Occurrence Start Date", help="Start of the desired time or schedule for use.")                
    occurrence_end_date = fields.Datetime(string="Occurrence End Date", help="End of the desired time or schedule for use.")                
    occurrence_timing_id = fields.Many2one(comodel_name="hc.device.use.request.occurrence.timing", string="Occurrence Timing", help="Timing desired time or schedule for use.")                
    authored = fields.Datetime(string="Authored Date", help="When recorded.")                
    requester_type = fields.Selection(string="Requester Type", selection=[("Device", "Device"), ("Practitioner", "Practitioner"), ("Organization", "Organization")], help="Type of who/what is requesting device.")                
    requester_name = fields.Char(string="Requester", compute="_compute_requester_name", store="True", help="Who/what is requesting device.")                
    requester_device_id = fields.Many2one(comodel_name="hc.res.device", string="Requester Device", help="Who/what is requesting device.")                
    requester_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Requester Practitioner", help="Practitioner who/what is requesting device.")                
    requester_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Requester Organization", help="Organization who/what is requesting device.")                
    performer_type_id = fields.Many2one(comodel_name="hc.vs.participant.role", string="Performer Type", help="Fille role.")                
    performer_type = fields.Selection(string="Performer Type", selection=[("Practitioner", "Practitioner"), ("Organization", "Organization"), ("Patient", "Patient"), ("Device", "Device"), ("Related Person", "Related Person")], help="Type of requested filler.")                
    performer_name = fields.Char(string="Performer", compute="_compute_performer_name", store="True", help="Requested Filler.")                
    requested_performer_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Requested Performer Practitioner", help="Practitioner requested filler.")                
    requested_performer_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Requested Performer Organization", help="Organization requested filler.")                
    requested_performer_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Requested Performer Patient", help="Patient requested filler.")                
    requested_performer_device_id = fields.Many2one(comodel_name="hc.res.device", string="Requested Performer Device", help="Device requested filler.")                
    requested_performer_related_person_id = fields.Many2one(comodel_name="hc.res.related.person", string="Requested Performer Related Person", help="Related Person requested filler.")                
    reason_code_ids = fields.Many2many(comodel_name="hc.vs.condition.code", string="Reason Codes", help="Coded Reason for request.")                
    reason_reference_ids = fields.One2many(comodel_name="hc.device.use.request.reason.reference", inverse_name="device_use_request_id", string="Reason References", help="Linked Reason for request.")                
    supporting_info_ids = fields.One2many(comodel_name="hc.device.use.request.supporting.info", inverse_name="device_use_request_id", string="Supporting Info", help="Additional clinical information.")                
    note_ids = fields.One2many(comodel_name="hc.device.use.request.note", inverse_name="device_use_request_id", string="Notes", help="Notes or comments.")                
    relevant_history_ids = fields.One2many(comodel_name="hc.device.use.request.relevant.history", inverse_name="device_use_request_id", string="Relevant Histories", help="Request provenance.")                

class DeviceUseRequestIdentifier(models.Model):    
    _name = "hc.device.use.request.identifier"    
    _description = "Device Use Request Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    device_use_request_id = fields.Many2one(comodel_name="hc.res.device.use.request", string="Device Use Request", help="Device Use Request associated with this Device Use Request Identifier.")                

class DeviceUseRequestDefinition(models.Model):    
    _name = "hc.device.use.request.definition"    
    _description = "Device Use Request Definition"        
    _inherit = ["hc.basic.association"]

    device_use_request_id = fields.Many2one(comodel_name="hc.res.device.use.request", string="Device Use Request", help="Device Use Request associated with this Device Use Request Definition.")                
    definition_type = fields.Selection(string="Definition Type", selection=[("string", "String"), ("Device Use Request", "Device Use Request")], help="Type of definition or protocol.")                
    definition_name = fields.Char(string="Definition", compute="_compute_definition_name", store="True", help="Protocol or definition.")                
    definition_string = fields.Char(string="Definition String", help="String of protocol or definition.")                
    definition_device_use_request_id = fields.Many2one(comodel_name="hc.res.device.use.request", string="Definition Device Use Request", help="Device Use Request protocol or definition.")                

class DeviceUseRequestBasedOn(models.Model):    
    _name = "hc.device.use.request.based.on"    
    _description = "Device Use Request Based On"        
    _inherit = ["hc.basic.association"]

    device_use_request_id = fields.Many2one(comodel_name="hc.res.device.use.request", string="Device Use Request", help="Device Use Request associated with this Device Use Request Based On.")                
    based_on_type = fields.Selection(string="Based On Type", selection=[("string", "String"), ("Device Use Request", "Device Use Request")], help="Type of what request fulfills.")                
    based_on_name = fields.Char(string="Based On", compute="_compute_based_on_name", store="True", help="What request fulfills.")                
    based_on_string = fields.Char(string="Based On String", help="String of what request fulfills.")                
    based_on_device_use_request_id = fields.Many2one(comodel_name="hc.res.device.use.request", string="Based On Device Use Request", help="Device Use Request what request fulfills.")                

class DeviceUseRequestReplaces(models.Model):    
    _name = "hc.device.use.request.replaces"    
    _description = "Device Use Request Replaces"        
    _inherit = ["hc.basic.association"]

    device_use_request_id = fields.Many2one(comodel_name="hc.res.device.use.request", string="Device Use Request", help="Device Use Request associated with this Device Use Request Replaces.")                
    replaces_type = fields.Selection(string="Replaces Type", selection=[("string", "String"), ("Device Use Request", "Device Use Request")], help="Type of what request replaces.")                
    replaces_name = fields.Char(string="Replaces", compute="_compute_replaces_name", store="True", help="What request replaces.")                
    replaces_string = fields.Char(string="Replaces String", help="String of what request replaces.")                
    replaces_device_use_request_id = fields.Many2one(comodel_name="hc.res.device.use.request", string="Replaces Device Use Request", help="Device Use Request what request replaces.")                   

class DeviceUseRequestReasonReference(models.Model):    
    _name = "hc.device.use.request.reason.reference"    
    _description = "Device Use Request Reason Reference"        
    _inherit = ["hc.basic.association"]

    device_use_request_id = fields.Many2one(comodel_name="hc.res.device.use.request", string="Device Use Request", help="Device Use Request associated with this Device Use Request Reason Reference.")                
    reason_refererence_type = fields.Selection(string="Reason Refererence Type", selection=[("string", "String"), ("Device Use Request", "Device Use Request")], help="Type of linked reason for request.")                
    reason_refererence_name = fields.Char(string="Reason Refererence", compute="_compute_reason_refererence_name", store="True", help="Linked Reason for request.")                
    reason_reference_string = fields.Char(string="Reason Reference String", help="String of linked reason for request.")                
    reason_reference_device_use_request_id = fields.Many2one(comodel_name="hc.res.device.use.request", string="Reason Reference Device Use Request", help="Device Use Request linked reason for request.")                

class DeviceUseRequestSupportingInfo(models.Model):    
    _name = "hc.device.use.request.supporting.info"    
    _description = "Device Use Request Supporting Info"        
    _inherit = ["hc.basic.association"]

    device_use_request_id = fields.Many2one(comodel_name="hc.res.device.use.request", string="Device Use Request", help="Device Use Request associated with this Device Use Request Supporting Info.")                
    supporting_info_type = fields.Selection(string="Supporting Info Type", selection=[("string", "String"), ("Device Use Request", "Device Use Request")], help="Type of additional clinical information.")                
    supporting_info_name = fields.Char(string="Supporting Info", compute="_compute_supporting_info_name", store="True", help="Additional clinical information.")                
    supporting_info_string = fields.Char(string="Supporting Info String", help="String of additional clinical information.")                
    supporting_info_device_use_request_id = fields.Many2one(comodel_name="hc.res.device.use.request", string="Supporting Info Device Use Request", help="Device Use Request additional clinical information.")                

class DeviceUseRequestNote(models.Model):    
    _name = "hc.device.use.request.note"    
    _description = "Device Use Request Note"        
    _inherit = ["hc.basic.association", "hc.annotation"]

    device_use_request_id = fields.Many2one(comodel_name="hc.res.device.use.request", string="Device Use Request", help="Device Use Request associated with this Device Use Request Note.")                

class DeviceUseRequestRelevantHistory(models.Model):    
    _name = "hc.device.use.request.relevant.history"    
    _description = "Device Use Request Relevant History"        
    _inherit = ["hc.basic.association"]

    device_use_request_id = fields.Many2one(comodel_name="hc.res.device.use.request", string="Device Use Request", help="Device Use Request associated with this Device Use Request Relevant History.")                
    relevant_history_id = fields.Many2one(comodel_name="hc.res.provenance", string="Relevant History", help="Request provenance.")                

class DeviceUseRequestRequisitionIdentifier(models.Model):    
    _name = "hc.device.use.request.requisition.identifier"    
    _description = "Device Use Request Requisition Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

class DeviceUseRequestOccurrenceTiming(models.Model):    
    _name = "hc.device.use.request.occurrence.timing"    
    _description = "Device Use Request Occurrence Timing"        
    _inherit = ["hc.basic.association", "hc.timing"]

class RequestStage(models.Model):    
    _name = "hc.vs.request.stage"    
    _description = "Request Stage"        
    _inherit = ["hc.value.set.contains"]

class DeviceKind(models.Model):    
    _name = "hc.vs.device.kind"    
    _description = "Device Kind"        
    _inherit = ["hc.value.set.contains"]
